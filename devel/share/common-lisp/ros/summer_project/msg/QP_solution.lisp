; Auto-generated. Do not edit!


(cl:in-package summer_project-msg)


;//! \htmlinclude QP_solution.msg.html

(cl:defclass <QP_solution> (roslisp-msg-protocol:ros-message)
  ((v
    :reader v
    :initarg :v
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64)))
)

(cl:defclass QP_solution (<QP_solution>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <QP_solution>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'QP_solution)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name summer_project-msg:<QP_solution> is deprecated: use summer_project-msg:QP_solution instead.")))

(cl:ensure-generic-function 'v-val :lambda-list '(m))
(cl:defmethod v-val ((m <QP_solution>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader summer_project-msg:v-val is deprecated.  Use summer_project-msg:v instead.")
  (v m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <QP_solution>) ostream)
  "Serializes a message object of type '<QP_solution>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'v) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <QP_solution>) istream)
  "Deserializes a message object of type '<QP_solution>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'v) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<QP_solution>)))
  "Returns string type for a message object of type '<QP_solution>"
  "summer_project/QP_solution")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'QP_solution)))
  "Returns string type for a message object of type 'QP_solution"
  "summer_project/QP_solution")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<QP_solution>)))
  "Returns md5sum for a message object of type '<QP_solution>"
  "004449d08fcee3db1c37ac92b523792c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'QP_solution)))
  "Returns md5sum for a message object of type 'QP_solution"
  "004449d08fcee3db1c37ac92b523792c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<QP_solution>)))
  "Returns full string definition for message of type '<QP_solution>"
  (cl:format cl:nil "std_msgs/Float64 v~%~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'QP_solution)))
  "Returns full string definition for message of type 'QP_solution"
  (cl:format cl:nil "std_msgs/Float64 v~%~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <QP_solution>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'v))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <QP_solution>))
  "Converts a ROS message object to a list"
  (cl:list 'QP_solution
    (cl:cons ':v (v msg))
))
