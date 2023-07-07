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
      this.x = null;
      this.y = null;
      this.vel = null;
      this.acc = null;
    }
    else {
      if (initObj.hasOwnProperty('ID')) {
        this.ID = initObj.ID
      }
      else {
        this.ID = new std_msgs.msg.Int64();
      }
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('vel')) {
        this.vel = initObj.vel
      }
      else {
        this.vel = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('acc')) {
        this.acc = initObj.acc
      }
      else {
        this.acc = new std_msgs.msg.Float64();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type limo_info
    // Serialize message field [ID]
    bufferOffset = std_msgs.msg.Int64.serialize(obj.ID, buffer, bufferOffset);
    // Serialize message field [x]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.y, buffer, bufferOffset);
    // Serialize message field [vel]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.vel, buffer, bufferOffset);
    // Serialize message field [acc]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.acc, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type limo_info
    let len;
    let data = new limo_info(null);
    // Deserialize message field [ID]
    data.ID = std_msgs.msg.Int64.deserialize(buffer, bufferOffset);
    // Deserialize message field [x]
    data.x = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [vel]
    data.vel = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [acc]
    data.acc = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 40;
  }

  static datatype() {
    // Returns string type for a message object
    return 'summer_project/limo_info';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '326e2462ad523a29cf0e1a6ca744aac8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Int64 ID
    std_msgs/Float64 x
    std_msgs/Float64 y
    std_msgs/Float64 vel
    std_msgs/Float64 acc
    
    ================================================================================
    MSG: std_msgs/Int64
    int64 data
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

    if (msg.x !== undefined) {
      resolved.x = std_msgs.msg.Float64.Resolve(msg.x)
    }
    else {
      resolved.x = new std_msgs.msg.Float64()
    }

    if (msg.y !== undefined) {
      resolved.y = std_msgs.msg.Float64.Resolve(msg.y)
    }
    else {
      resolved.y = new std_msgs.msg.Float64()
    }

    if (msg.vel !== undefined) {
      resolved.vel = std_msgs.msg.Float64.Resolve(msg.vel)
    }
    else {
      resolved.vel = new std_msgs.msg.Float64()
    }

    if (msg.acc !== undefined) {
      resolved.acc = std_msgs.msg.Float64.Resolve(msg.acc)
    }
    else {
      resolved.acc = new std_msgs.msg.Float64()
    }

    return resolved;
    }
};

module.exports = limo_info;
