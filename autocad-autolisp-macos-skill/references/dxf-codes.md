# DXF Codes Reference for AutoCAD Mac

DXF (Drawing Exchange Format) codes are essential for using `entmake` and `entmod` on Mac, since ActiveX (`vlax-*`) functions are not available.

## Common DXF Codes

### Entity Header Codes

| Code | Description | Example |
|------|-------------|---------|
| 0 | Entity type | `"LINE"`, `"CIRCLE"`, `"TEXT"` |
| 2 | Block name | `"Model Space"` |
| 5 | Handle | `"1A2"` |
| 6 | Linetype name | `"CONTINUOUS"` |
| 8 | Layer name | `"0"` |
| 62 | Color (negative = off) | `1` (red), `256` (bylayer) |
| 67 | Paper space flag | `0` (model), `1` (paper) |
| 100 | Subclass marker | `"AcDbEntity"` |
| 410 | Layout tab name | `"Model"` |

### Coordinate Codes

| Code | Description | Example |
|------|-------------|---------|
| 10 | Start point / Center | `'(0.0 0.0 0.0)` |
| 11 | End point / Alignment | `'(10.0 0.0 0.0)` |
| 12 | Displacement / Other | `'(5.0 5.0 0.0)` |
| 13 | Third point | `'(0.0 10.0 0.0)` |
| 14 | Fourth point | `'(10.0 10.0 0.0)` |

### Text and Dimension Codes

| Code | Description | Example |
|------|-------------|---------|
| 1 | Text content | `"Hello World"` |
| 40 | Text height | `2.5` |
| 41 | Width factor | `0.75` |
| 50 | Rotation angle | `0.0` |
| 7 | Text style name | `"Standard"` |
| 72 | Horizontal alignment | `0` (left) to `4` (fit) |
| 73 | Vertical alignment | `0` (baseline) to `3` (bottom) |

### Arc and Circle Codes

| Code | Description | Example |
|------|-------------|---------|
| 40 | Radius | `5.0` |
| 50 | Start angle | `0.0` |
| 51 | End angle | `3.14159` |

### Polyline Codes

| Code | Description | Example |
|------|-------------|---------|
| 41 | Start width | `0.0` |
| 42 | Bulge (arc) | `0.5` |
| 43 | Constant width | `0.5` |
| 70 | Flags | `1` (closed), `8` (3D) |
| 90 | Number of vertices | `4` |
| 210 | Extrusion direction | `'(0.0 0.0 1.0)` |

## Creating Entities with entmake

### Line

```lisp
(entmake
  (list
    '(0 . "LINE")
    '(100 . "AcDbEntity")
    '(8 . "0")           ; Layer
    '(62 . 1)            ; Color (1=red)
    '(100 . "AcDbLine")
    '(10 0.0 0.0 0.0)    ; Start point
    '(11 10.0 10.0 0.0)  ; End point
  )
)
```

### Circle

```lisp
(entmake
  (list
    '(0 . "CIRCLE")
    '(100 . "AcDbEntity")
    '(8 . "0")
    '(100 . "AcDbCircle")
    '(10 5.0 5.0 0.0)    ; Center
    (cons 40 2.5)        ; Radius
  )
)
```

### Arc

```lisp
(entmake
  (list
    '(0 . "ARC")
    '(100 . "AcDbEntity")
    '(8 . "0")
    '(100 . "AcDbCircle")
    '(10 5.0 5.0 0.0)    ; Center
    (cons 40 3.0)        ; Radius
    '(100 . "AcDbArc")
    (cons 50 0.0)        ; Start angle
    (cons 51 (* pi 0.5)) ; End angle (90 degrees)
  )
)
```

### Text

```lisp
(entmake
  (list
    '(0 . "TEXT")
    '(100 . "AcDbEntity")
    '(8 . "0")
    '(100 . "AcDbText")
    '(10 0.0 0.0 0.0)           ; Insertion point
    (cons 40 2.5)               ; Height
    (cons 1 "Hello World")      ; Text content
    '(100 . "AcDbText")
    (cons 50 0.0)               ; Rotation
  )
)
```

### LWPolyline (Lightweight Polyline)

```lisp
(entmake
  (list
    '(0 . "LWPOLYLINE")
    '(100 . "AcDbEntity")
    '(8 . "0")
    '(100 . "AcDbPolyline")
    (cons 90 4)           ; Number of vertices
    (cons 70 1)           ; Closed flag
    '(10 0.0 0.0)
    '(10 10.0 0.0)
    '(10 10.0 10.0)
    '(10 0.0 10.0)
  )
)
```

### Layer

```lisp
(entmake
  (list
    '(0 . "LAYER")
    '(100 . "AcDbSymbolTableRecord")
    '(100 . "AcDbLayerTableRecord")
    (cons 2 "MYLAYER")    ; Layer name
    (cons 70 0)           ; Flags
    (cons 62 3)           ; Color (3=green)
    (cons 6 "CONTINUOUS") ; Linetype
  )
)
```

## Modifying Entities with entmod

### Change Color

```lisp
(defun change-color (ename new-color)
  (entmod
    (subst
      (cons 62 new-color)
      (assoc 62 (entget ename))
      (entget ename)
    )
  )
)
```

### Change Layer

```lisp
(defun change-layer (ename new-layer)
  (entmod
    (subst
      (cons 8 new-layer)
      (assoc 8 (entget ename))
      (entget ename)
    )
  )
)
```

### Change Text Content

```lisp
(defun change-text (ename new-text)
  (entmod
    (subst
      (cons 1 new-text)
      (assoc 1 (entget ename))
      (entget ename)
    )
  )
)
```

### Move Entity

```lisp
(defun move-entity (ename new-point / data)
  (setq data (entget ename))
  (entmod
    (subst
      (cons 10 new-point)
      (assoc 10 data)
      data
    )
  )
)
```

## Replacing vlax-get with DXF

| ActiveX Property | DXF Code |
|-----------------|----------|
| `Center` | 10 |
| `Radius` | 40 |
| `StartPoint` | 10 |
| `EndPoint` | 11 |
| `TextString` | 1 |
| `Height` | 40 |
| `Layer` | 8 |
| `Color` | 62 |
| `Linetype` | 6 |
| `Rotation` | 50 |
| `Handle` | 5 |
| `ObjectName` | 0 |

### Example Conversion

**Windows (ActiveX):**
```lisp
(vl-load-com)
(setq circle-obj (vlax-ename->vla-object (car (entsel))))
(setq radius (vlax-get circle-obj 'Radius))
(vlax-put circle-obj 'Radius (* radius 2))
```

**Mac Compatible:**
```lisp
(setq circle-ent (car (entsel)))
(setq data (entget circle-ent))
(setq radius (cdr (assoc 40 data)))
(entmod (subst (cons 40 (* radius 2)) (assoc 40 data) data))
```

## Utility Functions

### Get Entity Property

```lisp
(defun get-property (ename dxf-code)
  (cdr (assoc dxf-code (entget ename)))
)
```

### Set Entity Property

```lisp
(defun set-property (ename dxf-code value / data)
  (setq data (entget ename))
  (if (assoc dxf-code data)
    (entmod (subst (cons dxf-code value) (assoc dxf-code data) data))
    (entmod (append data (list (cons dxf-code value))))
  )
)
```

### Get All Properties

```lisp
(defun dump-entity (ename)
  (foreach item (entget ename)
    (princ (strcat "\n" (itoa (car item)) ": " (vl-princ-to-string (cdr item))))
  )
  (princ)
)
```
