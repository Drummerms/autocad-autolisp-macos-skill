;;; ENTITY-CREATOR.LSP
;;; Template for creating entities using entmake (Mac-compatible)
;;; Compatibility: AutoCAD for Windows and Mac
;;;
;;; Description: Create various entities without using ActiveX
;;; Author: Your Name
;;; Version: 1.0.0
;;;
;;; Usage:
;;;   Load: (load "entity-creator.lsp")
;;;   Commands: DRAWLINE, DRAWCIRCLE, DRAWARC, DRAWTEXT, DRAWRECT

;; ============================================================
;; UTILITY FUNCTIONS
;; ============================================================

;;; Get current layer
(defun get-current-layer ()
  (getvar "CLAYER")
)

;;; Create line entity
(defun make-line (start end layer color / data)
  (setq data
    (list
      '(0 . "LINE")
      '(100 . "AcDbEntity")
      (cons 8 (if layer layer (get-current-layer)))
      (if color (cons 62 color))
      '(100 . "AcDbLine")
      (cons 10 start)
      (cons 11 end)
    )
  )
  ;; Remove nil entries
  (entmake (vl-remove nil data))
)

;;; Create circle entity
(defun make-circle (center radius layer color / data)
  (setq data
    (list
      '(0 . "CIRCLE")
      '(100 . "AcDbEntity")
      (cons 8 (if layer layer (get-current-layer)))
      (if color (cons 62 color))
      '(100 . "AcDbCircle")
      (cons 10 center)
      (cons 40 radius)
    )
  )
  (entmake (vl-remove nil data))
)

;;; Create arc entity
(defun make-arc (center radius start-angle end-angle layer color / data)
  (setq data
    (list
      '(0 . "ARC")
      '(100 . "AcDbEntity")
      (cons 8 (if layer layer (get-current-layer)))
      (if color (cons 62 color))
      '(100 . "AcDbCircle")
      (cons 10 center)
      (cons 40 radius)
      '(100 . "AcDbArc")
      (cons 50 start-angle)
      (cons 51 end-angle)
    )
  )
  (entmake (vl-remove nil data))
)

;;; Create text entity
(defun make-text (point height content rotation layer color / data)
  (setq data
    (list
      '(0 . "TEXT")
      '(100 . "AcDbEntity")
      (cons 8 (if layer layer (get-current-layer)))
      (if color (cons 62 color))
      '(100 . "AcDbText")
      (cons 10 point)
      (cons 40 height)
      (cons 1 content)
      '(100 . "AcDbText")
      (cons 50 (if rotation rotation 0.0))
    )
  )
  (entmake (vl-remove nil data))
)

;;; Create rectangle (closed polyline)
(defun make-rectangle (corner1 corner2 layer color / x1 y1 x2 y2 data)
  (setq x1 (car corner1)
        y1 (cadr corner1)
        x2 (car corner2)
        y2 (cadr corner2)
  )
  (setq data
    (list
      '(0 . "LWPOLYLINE")
      '(100 . "AcDbEntity")
      (cons 8 (if layer layer (get-current-layer)))
      (if color (cons 62 color))
      '(100 . "AcDbPolyline")
      (cons 90 4)           ; Number of vertices
      (cons 70 1)           ; Closed flag
      (list 10 x1 y1 0.0)
      (list 10 x2 y1 0.0)
      (list 10 x2 y2 0.0)
      (list 10 x1 y2 0.0)
    )
  )
  (entmake (vl-remove nil data))
)

;;; Create layer
(defun make-layer (name color linetype / data)
  (setq data
    (list
      '(0 . "LAYER")
      '(100 . "AcDbSymbolTableRecord")
      '(100 . "AcDbLayerTableRecord")
      (cons 2 name)
      (cons 70 0)
      (cons 62 (if color color 7))
      (cons 6 (if linetype linetype "CONTINUOUS"))
    )
  )
  (entmake data)
)

;; ============================================================
;; COMMAND DEFINITIONS
;; ============================================================

;;; Draw a line by picking two points
(defun c:DRAWLINE (/ p1 p2)
  (setq p1 (getpoint "\nStart point: "))
  (if p1
    (progn
      (setq p2 (getpoint p1 "\nEnd point: "))
      (if p2
        (make-line p1 p2 nil nil)
        (princ "\nNo end point specified.")
      )
    )
    (princ "\nNo start point specified.")
  )
  (princ)
)

;;; Draw a circle by picking center and radius
(defun c:DRAWCIRCLE (/ center radius)
  (setq center (getpoint "\nCenter point: "))
  (if center
    (progn
      (setq radius (getdist center "\nRadius: "))
      (if radius
        (make-circle center radius nil nil)
        (princ "\nNo radius specified.")
      )
    )
    (princ "\nNo center point specified.")
  )
  (princ)
)

;;; Draw an arc by picking center, radius, and angles
(defun c:DRAWARC (/ center radius start-angle end-angle)
  (setq center (getpoint "\nCenter point: "))
  (if center
    (progn
      (setq radius (getdist center "\nRadius: "))
      (if radius
        (progn
          (setq start-angle (getangle center "\nStart angle: "))
          (if start-angle
            (progn
              (setq end-angle (getangle center "\nEnd angle: "))
              (if end-angle
                (make-arc center radius start-angle end-angle nil nil)
                (princ "\nNo end angle specified.")
              )
            )
            (princ "\nNo start angle specified.")
          )
        )
        (princ "\nNo radius specified.")
      )
    )
    (princ "\nNo center point specified.")
  )
  (princ)
)

;;; Draw text by picking point and entering content
(defun c:DRAWTEXT (/ point height content)
  (setq point (getpoint "\nInsertion point: "))
  (if point
    (progn
      (setq height (getdist "\nText height <2.5>: "))
      (if (not height) (setq height 2.5))
      (setq content (getstring T "\nText content: "))
      (if (and content (/= content ""))
        (make-text point height content 0.0 nil nil)
        (princ "\nNo text content specified.")
      )
    )
    (princ "\nNo insertion point specified.")
  )
  (princ)
)

;;; Draw a rectangle by picking two corners
(defun c:DRAWRECT (/ corner1 corner2)
  (setq corner1 (getpoint "\nFirst corner: "))
  (if corner1
    (progn
      (setq corner2 (getcorner corner1 "\nOpposite corner: "))
      (if corner2
        (make-rectangle corner1 corner2 nil nil)
        (princ "\nNo opposite corner specified.")
      )
    )
    (princ "\nNo first corner specified.")
  )
  (princ)
)

;; ============================================================
;; LOAD MESSAGE
;; ============================================================

(princ "\nEntity creator loaded. Commands: DRAWLINE, DRAWCIRCLE, DRAWARC, DRAWTEXT, DRAWRECT")
(princ)
