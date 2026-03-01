# Mac-Safe Alternatives Reference

Detailed guide for replacing Windows-only AutoLISP functions with Mac-compatible alternatives.

## ActiveX → entget/entmod Conversion

### Getting Properties

**Windows (ActiveX):**
```lisp
(vl-load-com)
(setq obj (vlax-ename->vla-object (car (entsel))))
(setq radius (vlax-get obj 'Radius))
```

**Mac Compatible:**
```lisp
(setq ent (car (entsel)))
(setq radius (cdr (assoc 40 (entget ent))))
```

### Setting Properties

**Windows (ActiveX):**
```lisp
(vlax-put obj 'Radius 10.0)
```

**Mac Compatible:**
```lisp
(setq data (entget ent))
(entmod (subst (cons 40 10.0) (assoc 40 data) data))
```

### Property Mapping Table

| ActiveX Property | DXF Code | Type |
|-----------------|----------|------|
| `ObjectName` | 0 | String |
| `Handle` | 5 | String |
| `Layer` | 8 | String |
| `Linetype` | 6 | String |
| `Color` | 62 | Integer |
| `Lineweight` | 370 | Integer |
| `Visible` | 60 | Integer (0/1) |
| `Center` (Circle/Arc) | 10 | Point |
| `Radius` (Circle/Arc) | 40 | Real |
| `StartAngle` (Arc) | 50 | Real |
| `EndAngle` (Arc) | 51 | Real |
| `StartPoint` (Line) | 10 | Point |
| `EndPoint` (Line) | 11 | Point |
| `TextString` (Text/MText) | 1 | String |
| `Height` (Text) | 40 | Real |
| `Rotation` (Text) | 50 | Real |
| `InsertionPoint` (Block) | 10 | Point |
| `Name` (Block) | 2 | String |

## Reactor Alternatives

Reactors (`vlr-*`) are not available on Mac. Here are alternatives:

### Command Wrapper Pattern

```lisp
;;; Instead of a command reactor, wrap commands
(defun c:MYCOMMAND (/ ss)
  ;; Pre-command logic
  (setq ss (ssget))

  ;; Execute original command
  (command "._MOVE" ss "" pause pause)

  ;; Post-command logic (reactor-like behavior)
  (alert "Move completed!")

  (princ)
)
```

### Polling Pattern

```lisp
;;; Poll for changes at intervals
(defun poll-for-changes (/ last-count current-count)
  (setq last-count (sslength (ssget "X")))

  (defun check-changes ()
    (setq current-count (sslength (ssget "X")))
    (if (/= current-count last-count)
      (progn
        (princ "\nEntities changed!")
        (setq last-count current-count)
      )
    )
  )

  ;; Call check-changes periodically (e.g., from a timer or menu)
)
```

### UNDO Group Pattern

```lisp
;;; Track changes via UNDO groups
(defun track-changes (func / result)
  (command "._UNDO" "_Begin")
  (setq result (func))
  (command "._UNDO" "_End")
  result
)
```

## Dialog Alternatives

### Color Dialog Replacement

**Windows:**
```lisp
(acad_colordlg 1)
```

**Mac:**
```lisp
(defun get-color-mac (/ color colors)
  (setq colors '("1=Red" "2=Yellow" "3=Green" "4=Cyan" "5=Blue" "6=Magenta" "7=White"))
  (initget "1 2 3 4 5 6 7")
  (setq color (getkword (strcat "\nColor [" (vl-string-translate " " "/" (apply 'strcat (mapcar '(lambda (x) (strcat x " ")) colors))) "]: ")))
  (if color (atoi color) 256)
)
```

### Simple Dialog Alternative

Instead of DCL (which has limited Mac support), use command-line prompts:

```lisp
(defun get-user-input-mac (/ option)
  (initget "Option1 Option2 Option3")
  (setq option (getkword "\nChoose [Option1/Option2/Option3]: "))
  (cond
    ((= option "Option1") (do-option1))
    ((= option "Option2") (do-option2))
    ((= option "Option3") (do-option3))
  )
)
```

## Registry Alternatives

### Config File Approach

**Windows:**
```lisp
(vl-registry-write "HKEY_CURRENT_USER\\Software\\MyApp" "Setting" "Value")
```

**Mac (JSON config):**
```lisp
;;; Read config from JSON file
(defun read-config ( / file line data)
  (setq file (open (findfile "myconfig.json") "r"))
  (if file
    (progn
      (setq data (read-line file))
      (close file)
      ;; Parse JSON (simple implementation)
      data
    )
  )
)

;;; Write config to LSP file
(defun write-config (key value / file path)
  (setq path (strcat (getvar "ROAMABLEROOTPREFIX") "myapp-config.lsp"))
  (setq file (open path "w"))
  (if file
    (progn
      (write-line (strcat "(setq " key " " (vl-princ-to-string value) ")") file)
      (close file)
      T
    )
  )
)
```

### LSP-based Config

```lisp
;;; Save settings to a LSP file
(defun save-settings (settings-file settings / file)
  (setq file (open settings-file "w"))
  (if file
    (progn
      (write-line ";;; User Settings - Auto-generated" file)
      (foreach setting settings
        (write-line
          (strcat "(setq "
                  (car setting)
                  " "
                  (vl-princ-to-string (cdr setting))
                  ")")
          file)
      )
      (close file)
      T
    )
  )
)

;;; Load settings from LSP file
(defun load-settings (settings-file)
  (if (findfile settings-file)
    (load settings-file)
  )
)
```

## Express Tools Alternatives

### acet-str-replace

**Windows:**
```lisp
(acet-str-replace "old" "new" "old string with old text")
```

**Mac:**
```lisp
(defun str-replace (old new str / pos result)
  (setq result str)
  (while (setq pos (vl-string-search old result))
    (setq result (strcat
      (substr result 1 pos)
      new
      (substr result (+ pos (strlen old) 1))
    ))
  )
  result
)
```

### acet-ss-drag-move

**Windows:**
```lisp
(acet-ss-drag-move ss pt "Move objects")
```

**Mac:**
```lisp
(defun ss-drag-move-mac (ss prompt / pt)
  (setq pt (getpoint (strcat "\n" prompt ": ")))
  (if pt
    (command "._MOVE" ss "" (list 0 0 0) pt)
  )
)
```

## Object Selection Alternatives

### Getting Object by Handle

**Windows:**
```lisp
(vlax-ename->vla-object (handent "1A2"))
```

**Mac:**
```lisp
(handent "1A2")  ; This works directly on Mac
```

### Selection Set Filtering

Both Windows and Mac support `ssget` with filters:

```lisp
;;; Select all circles on layer "0"
(ssget "X" '((0 . "CIRCLE") (8 . "0")))

;;; Select all text with specific content
(ssget "X" '((0 . "TEXT") (1 . "*specific*")))
```

## Common Pattern: Generic Property Getter/Setter

```lisp
;;; Generic property getter (Mac-compatible)
(defun get-dxf (ename code)
  (cdr (assoc code (entget ename)))
)

;;; Generic property setter (Mac-compatible)
(defun set-dxf (ename code value / data)
  (setq data (entget ename))
  (if (assoc code data)
    (entmod (subst (cons code value) (assoc code data) data))
    (entmod (append data (list (cons code value))))
  )
)

;;; Usage examples:
;;; (get-dxf ent 40)      ; Get radius
;;; (set-dxf ent 62 3)    ; Set color to green
;;; (set-dxf ent 8 "0")   ; Set layer
```

## Migration Checklist

When migrating Windows AutoLISP to Mac:

1. [ ] Remove all `vlax-*` function calls
2. [ ] Remove all `vlr-*` reactor calls
3. [ ] Remove all `acet-*` Express Tools calls
4. [ ] Remove `vl-load-com` (not needed on Mac)
5. [ ] Replace `acad_colordlg` with command-line input
6. [ ] Replace registry calls with config files
7. [ ] Convert ActiveX property access to DXF codes
8. [ ] Test DCL dialogs (may work on full AutoCAD Mac)
9. [ ] Remove `.vlx` compilation, distribute `.lsp` source
10. [ ] Update headers with "Compatibility: AutoCAD for Mac"
