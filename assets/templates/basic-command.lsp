;;; TEMPLATE.LSP
;;; Basic AutoLISP command template
;;; Compatibility: AutoCAD for Windows and Mac
;;;
;;; Description: Brief description of what this command does
;;; Author: Your Name
;;; Version: 1.0.0
;;;
;;; Usage:
;;;   Load: (load "template.lsp")
;;;   Run: TEMPLATE

(defun c:TEMPLATE (/ var1 var2 var3)
  ;; ============================================================
  ;; INITIALIZATION
  ;; ============================================================

  ;; Load Visual LISP extensions (Mac-compatible)
  (vl-load-all)

  ;; Save system variables that will be modified
  (setvar "CMDECHO" 0)

  ;; ============================================================
  ;; MAIN LOGIC
  ;; ============================================================

  ;; Get user input
  (setq var1 (getpoint "\nSelect point: "))

  (if var1
    (progn
      ;; Do something with the input
      (princ (strcat "\nPoint selected: "
                     (vl-princ-to-string var1)))

      ;; Example: Create an entity
      ;; (entmake ...)

      ;; Example: Run a command
      ;; (command "._CIRCLE" var1 5.0)
    )
    (princ "\nNo point selected.")
  )

  ;; ============================================================
  ;; CLEANUP
  ;; ============================================================

  ;; Restore system variables
  (setvar "CMDECHO" 1)

  ;; Exit cleanly
  (princ)
)

(princ "\nTemplate loaded. Type TEMPLATE to run.")
(princ)
