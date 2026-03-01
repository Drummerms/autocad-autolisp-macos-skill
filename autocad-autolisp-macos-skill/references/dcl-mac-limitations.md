# DCL Support on Mac - Limitations and Guidelines

## Overview

Dialog Control Language (DCL) is **supported on AutoCAD for Mac**, but has important limitations compared to Windows.

## Platform Support

| Platform | DCL Support |
|----------|-------------|
| AutoCAD for Windows | Full support |
| AutoCAD for Mac | Supported with limitations |
| AutoCAD LT for Windows | Supported |
| AutoCAD LT for Mac | **NOT supported** |
| AutoCAD Web | Not supported |

## Known Limitations on Mac

### 1. edit_box allow_accept Attribute

The `allow_accept` attribute is **not supported** for `edit_box` tiles on Mac and Web.

**Windows (works):**
```dcl
: edit_box {
  label = "Enter value:";
  key = "value";
  allow_accept = true;  // Not supported on Mac
}
```

**Mac workaround:**
```dcl
: edit_box {
  label = "Enter value:";
  key = "value";
  // Remove allow_accept for Mac compatibility
}
: button {
  label = "OK";
  key = "accept";
  is_default = true;  // Use this instead
}
```

### 2. Memory Usage

DCL on Mac uses **more memory** than on Windows. This is noted in the official documentation.

**Best practice:**
```lisp
;;; Always unload DCL files when done
(defun my-dialog (/ dcl_id result)
  (setq dcl_id (load_dialog "mydialog.dcl"))
  (new_dialog "mydialog" dcl_id)

  ;; ... dialog setup and interaction ...

  (done_dialog)
  (unload_dialog dcl_id)  ;; IMPORTANT: Unload to free memory
  result
)
```

### 3. Visual Differences

Some DCL tiles may render slightly differently on Mac due to platform-specific UI conventions:

- Button appearance follows macOS style
- Font rendering may differ
- Spacing and sizing may vary slightly

## Fully Supported DCL Tiles on Mac

These tiles work correctly on AutoCAD for Mac:

| Tile | Status |
|------|--------|
| `button` | ✅ Supported |
| `edit_box` | ✅ Supported (without allow_accept) |
| `list_box` | ✅ Supported |
| `popup_list` | ✅ Supported |
| `radio_button` | ✅ Supported |
| `radio_column` | ✅ Supported |
| `radio_row` | ✅ Supported |
| `toggle` | ✅ Supported |
| `slider` | ✅ Supported |
| `image` | ✅ Supported |
| `image_button` | ✅ Supported |
| `text` | ✅ Supported |
| `spacer` | ✅ Supported |
| `boxed_column` | ✅ Supported |
| `boxed_row` | ✅ Supported |
| `column` | ✅ Supported |
| `row` | ✅ Supported |
| `concatenation` | ✅ Supported |
| `paragraph` | ✅ Supported |

## Fully Supported DCL Attributes on Mac

| Attribute | Status |
|-----------|--------|
| `action` | ✅ Supported |
| `alignment` | ✅ Supported |
| `aspect_ratio` | ✅ Supported |
| `big_increment` | ✅ Supported |
| `children_alignment` | ✅ Supported |
| `children_fixed_height` | ✅ Supported |
| `children_fixed_width` | ✅ Supported |
| `color` | ✅ Supported |
| `edit_limit` | ✅ Supported |
| `edit_width` | ✅ Supported |
| `fixed_height` | ✅ Supported |
| `fixed_width` | ✅ Supported |
| `height` | ✅ Supported |
| `initial_focus` | ✅ Supported |
| `is_bold` | ✅ Supported |
| `is_cancel` | ✅ Supported |
| `is_default` | ✅ Supported |
| `is_enabled` | ✅ Supported |
| `is_tab_stop` | ✅ Supported |
| `key` | ✅ Supported |
| `label` | ✅ Supported |
| `layout` | ✅ Supported |
| `list` | ✅ Supported |
| `max_value` | ✅ Supported |
| `min_value` | ✅ Supported |
| `mnemonic` | ✅ Supported |
| `small_increment` | ✅ Supported |
| `tabs` | ✅ Supported |
| `value` | ✅ Supported |
| `width` | ✅ Supported |

## Mac-Compatible DCL Template

```dcl
//: MYDIALOG.DCL
//: A Mac-compatible dialog template
//: Compatibility: AutoCAD for Windows and Mac

mydialog : dialog {
  label = "My Dialog";

  : boxed_column {
    label = "Settings";

    : edit_box {
      label = "Value:";
      key = "value";
      edit_width = 20;
      // Note: allow_accept not supported on Mac for edit_box
    }

    : popup_list {
      label = "Option:";
      key = "option";
    }

    : toggle {
      label = "Enable feature";
      key = "enable";
    }
  }

  : row {
    fixed_width = true;
    alignment = centered;

    : button {
      label = "OK";
      key = "accept";
      is_default = true;
      fixed_width = true;
    }

    : button {
      label = "Cancel";
      key = "cancel";
      is_cancel = true;
      fixed_width = true;
    }
  }
}
```

## Mac-Compatible DCL AutoLISP Driver

```lisp
;;; MYDIALOG.LSP
;;; DCL dialog driver for Mac compatibility
;;; Compatibility: AutoCAD for Windows and Mac

(defun c:MYDIALOG (/ dcl_id value option enable)
  ;; Load the DCL file
  (setq dcl_id (load_dialog "mydialog.dcl"))

  (if (not (new_dialog "mydialog" dcl_id))
    (progn
      (alert "Cannot load dialog")
      (exit)
    )
  )

  ;; Set initial values
  (set_tile "value" "Default value")
  (set_tile "enable" "1")

  ;; Populate popup list
  (start_list "option")
  (add_list "Option 1")
  (add_list "Option 2")
  (add_list "Option 3")
  (end_list)
  (set_tile "option" "0")

  ;; Set tile actions
  (action_tile "accept" "(done_dialog 1)")
  (action_tile "cancel" "(done_dialog 0)")

  ;; Display dialog
  (setq result (start_dialog))

  ;; Unload dialog to free memory (important on Mac)
  (unload_dialog dcl_id)

  ;; Process result
  (if (= result 1)
    (progn
      (setq value (get_tile "value"))
      (setq option (get_tile "option"))
      (setq enable (get_tile "enable"))
      (princ (strcat "\nValue: " value))
      (princ (strcat "\nOption: " option))
      (princ (strcat "\nEnable: " enable))
    )
  )

  (princ)
)
```

## Alternative to DCL: Command-Line Input

For maximum compatibility (including AutoCAD LT for Mac), use command-line input:

```lisp
;;; Command-line alternative to DCL
(defun c:MYCOMMAND (/ value option enable)
  ;; Get string value
  (setq value (getstring T "\nEnter value: "))

  ;; Get keyword option
  (initget "Option1 Option2 Option3")
  (setq option (getkword "\nChoose option [Option1/Option2/Option3]: "))

  ;; Get yes/no
  (initget "Yes No")
  (setq enable (getkword "\nEnable feature? [Yes/No]: "))

  ;; Process values
  (princ (strcat "\nValue: " value))
  (princ (strcat "\nOption: " (if option option "Option1")))
  (princ (strcat "\nEnable: " (if enable enable "Yes")))

  (princ)
)
```

## Recommendations

1. **Always unload DCL** files when done to conserve memory on Mac
2. **Test on Mac** before deploying DCL-based scripts
3. **Avoid `allow_accept`** on `edit_box` tiles
4. **Consider command-line alternatives** for AutoCAD LT compatibility
5. **Keep DCL simple** - complex dialogs may have more issues

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Dialog doesn't display | Check DCL file path with `findfile` |
| Memory errors | Unload DCL files promptly |
| Tiles don't update | Check `set_tile` calls |
| Actions don't trigger | Verify `action_tile` syntax |
| Layout issues | Test on both Windows and Mac |
