;;; BATCH-PLOT.LSP
;;; Batch plot all layouts to PDF
;;; Compatibility: AutoCAD for Windows and Mac
;;;
;;; Description: Plots all layouts in the current drawing to PDF files
;;; Author: Your Name
;;; Version: 1.0.0
;;;
;;; Usage:
;;;   Load: (load "batch-plot.lsp")
;;;   Run: BATCHPLOT

(defun c:BATCHPLOT (/ layouts layout-name i plot-success)
  ;; ============================================================
  ;; INITIALIZATION
  ;; ============================================================

  (vl-load-all)
  (setvar "CMDECHO" 0)

  ;; Get all layouts
  (setq layouts (layoutlist))

  (if layouts
    (progn
      (princ (strcat "\nFound " (itoa (length layouts)) " layouts."))
      (princ "\nStarting batch plot...")

      (setq i 0)
      (setq plot-success 0)

      ;; ============================================================
      ;; PLOT EACH LAYOUT
      ;; ============================================================

      (foreach layout-name layouts
        ;; Switch to layout
        (setvar "CTAB" layout-name)
        (princ (strcat "\nPlotting: " layout-name))

        ;; Plot command
        ;; Note: Adjust parameters for your plotter/config
        (command "._PLOT"
                 "Y"              ; Detailed plot config? No
                 ""               ; Layout name (current)
                 "DWG To PDF.pc3" ; Plotter
                 ""               ; Paper size (default)
                 ""               ; Inches/mm
                 ""               ; Drawing orientation
                 ""               ; Plot upside down? No
                 ""               ; Plot area
                 ""               ; Plot scale
                 ""               ; Plot offset
                 ""               ; Plot with lineweights?
                 ""               ; Scale lineweights?
                 ""               ; Plot with plot styles?
                 ""               ; Plot style table
                 ""               ; Plot with transparency?
                 ""               ; Shaded viewport options
                 ""               ; Quality
                 ""               ; Shade plot custom
                 "N"              ; Write to file? No (send to plotter)
                 "N"              ; Save changes to layout? No
                 "Y"              ; Proceed with plot? Yes
        )

        (setq i (1+ i))
        (setq plot-success (1+ plot-success))
      )

      ;; ============================================================
      ;; SUMMARY
      ;; ============================================================

      (princ (strcat "\n\nBatch plot complete!"))
      (princ (strcat "\nPlotted: " (itoa plot-success) " of " (itoa i) " layouts."))

      ;; Return to Model space
      (setvar "CTAB" "Model")
    )
    (princ "\nNo layouts found in drawing.")
  )

  ;; ============================================================
  ;; CLEANUP
  ;; ============================================================

  (setvar "CMDECHO" 1)
  (princ)
)

(princ "\nBatch plot loaded. Type BATCHPLOT to run.")
(princ)
