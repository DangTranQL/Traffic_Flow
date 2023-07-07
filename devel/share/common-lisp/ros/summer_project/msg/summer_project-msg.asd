
(cl:in-package :asdf)

(defsystem "summer_project-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "limo_info" :depends-on ("_package_limo_info"))
    (:file "_package_limo_info" :depends-on ("_package"))
    (:file "limo_info_array" :depends-on ("_package_limo_info_array"))
    (:file "_package_limo_info_array" :depends-on ("_package"))
  ))