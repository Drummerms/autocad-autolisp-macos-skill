;;; SELECTION-PROCESSOR.LSP
;;; Template for processing selected entities
;;; Compatibility: AutoCAD for Windows and Mac
;;;
;;; Description: Process a selection of entities with Mac-compatible code
;;; Author: Your Name
;;; Version: 1.0.0
;;;
;;; Usage:
;;;   Load: (load "selection-processor.lsp")
;;;   Run: PROCESS

(defun c:PROCESS (/ ss i ename data count)
  ;; ============================================================
  ;; INITIALIZATION
  ;; ============================================================

  (vl-load-all)
  (setvar "CMDECHO" 0)
  (setq count 0)

  ;; ============================================================
  ;; GET SELECTION
  ;; ============================================================

  ;; Option 1: Let user select
  (princ "\nSelect entities to process: ")
  (setq ss (ssget))

  ;; Option 2: Filter selection (uncomment to use)
  ;; (setq ss (ssget '((0 . "LINE,CIRCLE,ARC"))))

  ;; Option 3: Select all in drawing
  ;; (setq ss (ssget "X"))

  (if ss
    (progn
      ;; ============================================================
      ;; PROCESS EACH ENTITY
      ;; ============================================================

      (setq i 0)
      (repeat (sslength ss)
        (setq ename (ssname ss i))
        (setq data (entget ename))

        ;; Get entity type
        (princ (strcat "\nProcessing: " (cdr (assoc 0 data))))

        ;; Get entity layer
        (princ (strcat " on layer " (cdr (assoc 8 data))))

        ;; ============================================================
        ;; MODIFY ENTITY (Example: Change color)
        ;; ============================================================

        ;; Check if color exists in entity data
        (if (assoc 62 data)
          ;; Color exists - modify it
          (entmod (subst (cons 62 3) (assoc 62 data) data))
          ;; No color - add it
          (entmod (append data (list (cons 62 3))))
        )

        (setq count (1+ count))
        (setq i (1+ i))
      )

      (princ (strcat "\nProcessed " (itoa count) " entities."))
    )
    (princ "\nNo entities selected.")
  )

  ;; ============================================================
  ;; CLEANUP
  ;; ============================================================

  (setvar "CMDECHO" 1)
  (princ)
)

(princ "\nSelection processor loaded. Type PROCESS to run.")
(princ)
