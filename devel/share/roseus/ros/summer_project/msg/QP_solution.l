;; Auto-generated. Do not edit!


(when (boundp 'summer_project::QP_solution)
  (if (not (find-package "SUMMER_PROJECT"))
    (make-package "SUMMER_PROJECT"))
  (shadow 'QP_solution (find-package "SUMMER_PROJECT")))
(unless (find-package "SUMMER_PROJECT::QP_SOLUTION")
  (make-package "SUMMER_PROJECT::QP_SOLUTION"))

(in-package "ROS")
;;//! \htmlinclude QP_solution.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass summer_project::QP_solution
  :super ros::object
  :slots (_v ))

(defmethod summer_project::QP_solution
  (:init
   (&key
    ((:v __v) (instance std_msgs::Float64 :init))
    )
   (send-super :init)
   (setq _v __v)
   self)
  (:v
   (&rest __v)
   (if (keywordp (car __v))
       (send* _v __v)
     (progn
       (if __v (setq _v (car __v)))
       _v)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Float64 _v
    (send _v :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Float64 _v
       (send _v :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Float64 _v
     (send _v :deserialize buf ptr-) (incf ptr- (send _v :serialization-length))
   ;;
   self)
  )

(setf (get summer_project::QP_solution :md5sum-) "004449d08fcee3db1c37ac92b523792c")
(setf (get summer_project::QP_solution :datatype-) "summer_project/QP_solution")
(setf (get summer_project::QP_solution :definition-)
      "std_msgs/Float64 v

================================================================================
MSG: std_msgs/Float64
float64 data
")



(provide :summer_project/QP_solution "004449d08fcee3db1c37ac92b523792c")


