(setq user-full-name "Galih Wicaksono"
      user-mail-address "galihwicaksono90@gmail.com")

(setq doom-font (font-spec :family "Cascadia Code" :size 13 :weight 'regular)
   doom-variable-pitch-font (font-spec :family "Fira Code" :size 13))

(after! doom-themes
  (setq doom-themes-enable-bold t
        doom-themes-enable-italic t))
(custom-set-faces!
  '(font-lock-comment-face :slant italic)
  '(font-lock-keyword-face :slant italic))

(setq display-line-numbers-type `relative)

(setq doom-theme 'doom-oceanic-next)

(setq org-directory "~/Documents/org/")
(setq org-agenda-files "~/Documents/org/todos.org")
(setq org-log-done 'note)

(after! org
  (require 'org-superstar)
  (add-hook 'org-mode-hook (lambda () (org-superstar-mode 1))))

    (add-to-list 'auto-mode-alist '("\\.js\\'" . rjsx-mode))

(map! :leader
      (:prefix-map ("i" . "insert")
       (:prefix ("l" . "Lorem Ipsum")
        :desc "Insert List" "l" #'lorem-ipsum-insert-list
        :desc "Insert Sentence" "s" #'lorem-ipsum-insert-sentences
        :desc "Insert Paragraph" "p" #'lorem-ipsum-insert-paragraphs)))
