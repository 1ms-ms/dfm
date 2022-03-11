variable "instance_count" {
  default = "1"
}

variable "instance_tags" {
  default = ["EC-1"]
}

variable "sub_tags"{
  default = ["SUB-1"]
}

variable "VPC"{
  type = string
  default = "10.0.0.0/16"
}
