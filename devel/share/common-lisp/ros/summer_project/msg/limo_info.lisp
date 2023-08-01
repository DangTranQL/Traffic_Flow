; Auto-generated. Do not edit!


(cl:in-package summer_project-msg)


;//! \htmlinclude limo_info.msg.html

(cl:defclass <limo_info> (roslisp-msg-protocol:ros-message)
  ((ID
    :reader ID
    :initarg :ID
    :type std_msgs-msg:Int64
    :initform (cl:make-instance 'std_msgs-msg:Int64))
   (x
    :reader x
    :initarg :x
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (y
    :reader y
    :initarg :y
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64))
   (vel
    :reader vel
    :initarg :vel
    :type std_msgs-msg:Float64
    :initform (cl:make-instance 'std_msgs-msg:Float64)))
)

(cl:defclass limo_info (<limo_info>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <limo_info>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'limo_info)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name summer_project-msg:<limo_info> is deprecated: use summer_project-msg:limo_info instead.")))

(cl:ensure-generic-function 'ID-val :lambda-list '(m))
(cl:defmethod ID-val ((m <limo_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader summer_project-msg:ID-val is deprecated.  Use summer_project-msg:ID instead.")
  (ID m))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <limo_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader summer_project-msg:x-val is deprecated.  Use summer_project-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <limo_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader summer_project-msg:y-val is deprecated.  Use summer_project-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'vel-val :lambda-list '(m))
(cl:defmethod vel-val ((m <limo_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader summer_project-msg:vel-val is deprecated.  Use summer_project-msg:vel instead.")
  (vel m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <limo_info>) ostream)
  "Serializes a message object of type '<limo_info>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'ID) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'x) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'y) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'vel) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <limo_info>) istream)
  "Deserializes a message object of type '<limo_info>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'ID) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'x) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'y) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'vel) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<limo_info>)))
  "Returns string type for a message object of type '<limo_info>"
  "summer_project/limo_info")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'limo_info)))
  "Returns string type for a message object of type 'limo_info"
  "summer_project/limo_info")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<limo_info>)))
  "Returns md5sum for a message object of type '<limo_info>"
  "17b3f4eca66f36408d5e8a3e901190f6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'limo_info)))
  "Returns md5sum for a message object of type 'limo_info"
  "17b3f4eca66f36408d5e8a3e901190f6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<limo_info>)))
  "Returns full string definition for message of type '<limo_info>"
  (cl:format cl:nil "std_msgs/Int64 ID~%std_msgs/Float64 x~%std_msgs/Float64 y~%std_msgs/Float64 vel~%~%================================================================================~%MSG: std_msgs/Int64~%int64 data~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'limo_info)))
  "Returns full string definition for message of type 'limo_info"
  (cl:format cl:nil "std_msgs/Int64 ID~%std_msgs/Float64 x~%std_msgs/Float64 y~%std_msgs/Float64 vel~%~%================================================================================~%MSG: std_msgs/Int64~%int64 data~%================================================================================~%MSG: std_msgs/Float64~%float64 data~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <limo_info>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'ID))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'x))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'y))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'vel))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <limo_info>))
  "Converts a ROS message object to a list"
  (cl:list 'limo_info
    (cl:cons ':ID (ID msg))
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':vel (vel msg))
))
