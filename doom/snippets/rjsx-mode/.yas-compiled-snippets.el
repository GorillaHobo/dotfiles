;;; Compiled snippets and support files for `rjsx-mode'
;;; Snippet definitions:
;;;
(yas-define-snippets 'rjsx-mode
                     '(("rfc" "import React from 'react';\n\nconst ${1:} = ($3) => {\n    return(\n    $5\n)\n}\n\nexport default ${1:$(yas-text)}" "React functional component" nil nil nil "/home/tony/.config/doom/snippets/rjsx-mode/rfc" nil nil)
                       ("rf" "const ${1:`(f-base buffer-file-name)`} = (${2:props}) {\n  return(\n    $0\n  )\n}\n\nexport default $1;" "React functional component short" nil nil nil "/home/tony/.config/doom/snippets/rjsx-mode/functional-component-short" nil nil)
                       ("btnlog" "<button onClick={ () => console.log(${1:}) }>Check</button>" "buttonLog" nil nil nil "/home/tony/.config/doom/snippets/rjsx-mode/buttonLog" nil nil)
                       ("arrow" "(${1:}) => ${2:}" "arrow" nil nil nil "/home/tony/.config/doom/snippets/rjsx-mode/arrow" nil nil)
                       ("SwitchTransition" "<SwitchTransition>\n    <CSSTransition\n        key={$1}\n        timeout={${2:500}}\n        classNames=\"$3\"\n    >\n      $4\n    </CSSTransition>/>\n</SwitchTransition>" "SwitchTransition" nil nil nil "/home/tony/.config/doom/snippets/rjsx-mode/SwitchTransition" nil nil)
                       ("CSSTransition" "<CSSTransition\n    in={${1:}}\n    timeout={${2:300}}\n    classNames=\"${3:}\"\n    ${3:unmountOnExit}\n>\n    $0\n</CSSTransition>" "CSSTransition" nil nil nil "/home/tony/.config/doom/snippets/rjsx-mode/CSSTransition" nil nil)))


;;; Do not edit! File generated at Tue Dec  1 11:51:32 2020
