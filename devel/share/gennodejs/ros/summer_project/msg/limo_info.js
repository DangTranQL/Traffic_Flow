// Auto-generated. Do not edit!

// (in-package summer_project.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class limo_info {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ID = null;
      this.pose = null;
      this.vel = null;
      this.accel = null;
    }
    else {
      if (initObj.hasOwnProperty('ID')) {
        this.ID = initObj.ID
      }
      else {
        this.ID = new std_msgs.msg.Int64();
      }
      if (initObj.hasOwnProperty('pose')) {
        this.pose = initObj.pose
      }
      else {
        this.pose = new std_msgs.msg.Float64MultiArray();
      }
      if (initObj.hasOwnProperty('vel')) {
        this.vel = initObj.vel
      }
      else {
        this.vel = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('accel')) {
        this.accel = initObj.accel
      }
      else {
        this.accel = new std_msgs.msg.Float64();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type limo_info
    // Serialize message field [ID]
    bufferOffset = std_msgs.msg.Int64.serialize(obj.ID, buffer, bufferOffset);
    // Serialize message field [pose]
    bufferOffset = std_msgs.msg.Float64MultiArray.serialize(obj.pose, buffer, bufferOffset);
    // Serialize message field [vel]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.vel, buffer, bufferOffset);
    // Serialize message field [accel]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.accel, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type limo_info
    let len;
    let data = new limo_info(null);
    // Deserialize message field [ID]
    data.ID = std_msgs.msg.Int64.deserialize(buffer, bufferOffset);
    // Deserialize message field [pose]
    data.pose = std_msgs.msg.Float64MultiArray.deserialize(buffer, bufferOffset);
    // Deserialize message field [vel]
    data.vel = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [accel]
    data.accel = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Float64MultiArray.getMessageSize(object.pose);
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'summer_project/limo_info';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '68fc7bffa679ec42e202fe8ddecc03a6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Int64 ID
    std_msgs/Float64MultiArray pose
    std_msgs/Float64 vel
    std_msgs/Float64 accel
    
    ================================================================================
    MSG: std_msgs/Int64
    int64 data
    ================================================================================
    MSG: std_msgs/Float64MultiArray
    # Please look at the MultiArrayLayout message definition for
    # documentation on all multiarrays.
    
    MultiArrayLayout  layout        # specification of data layout
    float64[]         data          # array of data
    
    
    ================================================================================
    MSG: std_msgs/MultiArrayLayout
    # The multiarray declares a generic multi-dimensional array of a
    # particular data type.  Dimensions are ordered from outer most
    # to inner most.
    
    MultiArrayDimension[] dim # Array of dimension properties
    uint32 data_offset        # padding elements at front of data
    
    # Accessors should ALWAYS be written in terms of dimension stride
    # and specified outer-most dimension first.
    # 
    # multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]
    #
    # A standard, 3-channel 640x480 image with interleaved color channels
    # would be specified as:
    #
    # dim[0].label  = "height"
    # dim[0].size   = 480
    # dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)
    # dim[1].label  = "width"
    # dim[1].size   = 640
    # dim[1].stride = 3*640 = 1920
    # dim[2].label  = "channel"
    # dim[2].size   = 3
    # dim[2].stride = 3
    #
    # multiarray(i,j,k) refers to the ith row, jth column, and kth channel.
    
    ================================================================================
    MSG: std_msgs/MultiArrayDimension
    string label   # label of given dimension
    uint32 size    # size of given dimension (in type units)
    uint32 stride  # stride of given dimension
    ================================================================================
    MSG: std_msgs/Float64
    float64 data
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new limo_info(null);
    if (msg.ID !== undefined) {
      resolved.ID = std_msgs.msg.Int64.Resolve(msg.ID)
    }
    else {
      resolved.ID = new std_msgs.msg.Int64()
    }

    if (msg.pose !== undefined) {
      resolved.pose = std_msgs.msg.Float64MultiArray.Resolve(msg.pose)
    }
    else {
      resolved.pose = new std_msgs.msg.Float64MultiArray()
    }

    if (msg.vel !== undefined) {
      resolved.vel = std_msgs.msg.Float64.Resolve(msg.vel)
    }
    else {
      resolved.vel = new std_msgs.msg.Float64()
    }

    if (msg.accel !== undefined) {
      resolved.accel = std_msgs.msg.Float64.Resolve(msg.accel)
    }
    else {
      resolved.accel = new std_msgs.msg.Float64()
    }

    return resolved;
    }
};

module.exports = limo_info;
