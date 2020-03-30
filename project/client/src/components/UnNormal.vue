<template>
  <el-table
    :data="unNormallist"
    height="250"
    style="width: 100%"
    :row-class-name="tableRowClassName"
  >
    <el-table-column type="index" width="100"></el-table-column>
    <el-table-column prop="room" label="影厅号"></el-table-column>
    <el-table-column prop="seat" label="座位号"></el-table-column>
    <el-table-column prop="uname" label="姓名"></el-table-column>
    <el-table-column prop="tel_number" label="电话"></el-table-column>
    <el-table-column prop="temperature" label="体温"></el-table-column>
    <el-table-column prop="date" label="看影时间"></el-table-column>
  </el-table>
</template>

<script>
import $ from "jquery";
import { mapGetters } from "vuex";
export default {
  name: "UnNormal",
  methods: {
    tableRowClassName({ row, rowIndex }) {
      if (row.temperature >= 37.0) {
        return "warning-row";
      } else {
        return "success-row";
      }
      return "";
    }
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters(["unNormallist"])
  },
  mounted() {
    var list = [];
    var obj;
    $.ajax({
      url: "http://127.0.0.1:8000/getUnNormalUser/",
      methods: "get",
      async: false,
      success: function(data) {
        obj = JSON.parse(data); //由JSON字符串转换为JSON对象
      }
    });
    //将JSON对象转化为数组
    for (var i = 0, l = obj.length; i < l; i++) {
      list.push(obj[i]);
    }
    this.$store.commit("changeUnNormalUser", list);
    // console.log(this.$store);
  }
};
</script>

<style>
.el-table .warning-row {
  background: #f56c6c;
}

.el-table .success-row {
  background: #f0f9eb;
}
</style>