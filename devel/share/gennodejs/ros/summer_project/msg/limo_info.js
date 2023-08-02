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
      this.mp_dist = null;
      this.origin_dist = null;
      this.vel = null;
    }
    else {
      if (initObj.hasOwnProperty('ID')) {
        this.ID = initObj.ID
      }
      else {
        this.ID = new std_msgs.msg.Int64();
      }
      if (initObj.hasOwnProperty('mp_dist')) {
        this.mp_dist = initObj.mp_dist
      }
      else {
        this.mp_dist = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('origin_dist')) {
        this.origin_dist = initObj.origin_dist
      }
      else {
        this.origin_dist = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('vel')) {
        this.vel = initObj.vel
      }
      else {
        this.vel = new std_msgs.msg.Float64();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type limo_info
    // Serialize message field [ID]
    bufferOffset = std_msgs.msg.Int64.serialize(obj.ID, buffer, bufferOffset);
    // Serialize message field [mp_dist]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.mp_dist, buffer, bufferOffset);
    // Serialize message field [origin_dist]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.origin_dist, buffer, bufferOffset);
    // Serialize message field [vel]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.vel, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type limo_info
    let len;
    let data = new limo_info(null);
    // Deserialize message field [ID]
    data.ID = std_msgs.msg.Int64.deserialize(buffer, bufferOffset);
    // Deserialize message field [mp_dist]
    data.mp_dist = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [origin_dist]
    data.origin_dist = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [vel]
    data.vel = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'summer_project/limo_info';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '047ef4b8205d6b737a5074a1a08a0dd7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Int64 ID
    std_msgs/Float64 mp_dist
    std_msgs/Float64 origin_dist
    std_msgs/Float64 vel
    
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

    if (msg.mp_dist !== undefined) {
      resolved.mp_dist = std_msgs.msg.Float64.Resolve(msg.mp_dist)
    }
    else {
      resolved.mp_dist = new std_msgs.msg.Float64()
    }

    if (msg.origin_dist !== undefined) {
      resolved.origin_dist = std_msgs.msg.Float64.Resolve(msg.origin_dist)
    }
    else {
      resolved.origin_dist = new std_msgs.msg.Float64()
    }

    if (msg.vel !== undefined) {
      resolved.vel = std_msgs.msg.Float64.Resolve(msg.vel)
    }
    else {
      resolved.vel = new std_msgs.msg.Float64()
    }

    return resolved;
    }
};

module.exports = limo_info;
