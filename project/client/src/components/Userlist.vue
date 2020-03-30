// 观影人员信息页面
<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="10">
        <el-input v-model="input" placeholder="请输入影厅号 或看影时间 或姓名 或体温" maxlength="30" show-word-limit></el-input>
      </el-col>
    </el-row>

    <div>
      <el-table
        ref="multipleTable"
        :data="tables"
        height="550"
        style="width: 100%"
        :row-class-name="tableRowClassName"
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column type="index" width="100"></el-table-column>
        <el-table-column prop="room" label="影厅号"></el-table-column>
        <el-table-column prop="seat" label="座位号"></el-table-column>
        <el-table-column prop="uname" label="姓名"></el-table-column>
        <el-table-column prop="openid" label="微信id"></el-table-column>
        <el-table-column prop="tel_number" label="电话"></el-table-column>
        <el-table-column prop="temperature" label="体温"></el-table-column>
        <el-table-column prop="date" label="看影时间"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" @click="handleEdit(scope.row.openid)">发送短信</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <el-row :gutter="20">
      <el-col :span="10">
        <el-button type="primary" @click="multiSend()">批量发送短信</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
import $ from "jquery";
import { mapGetters } from "vuex";
export default {
  name: "Userlist",
  data() {
    return { multipleSelection: [], input: "" };
  },
  methods: {
    // 处理多选框选中时间
    handleSelectionChange(val) {
      this.multipleSelection = val;
      // console.log(val[0].date);
    },
    // 处理单条发送短信
    handleEdit(openid) {
      // console.log(index, row);
      $.ajax({
        url: "http://127.0.0.1:8000/sendMessage/",
        methods: "get",
        data: { openid: openid },
        async: false,
        success: function(data) {
          alert("发送成功");
        }
      });
    },
    // 批量发送短信
    multiSend() {
      this.multipleSelection.forEach(data => {
        this.handleEdit(data.openid);
      });
    },
    // 根据体温显示表栏的背景色
    tableRowClassName({ row, rowIndex }) {
      if (row.temperature >= 37.0) {
        return "warning-row";
      } else {
        return "success-row";
      }
      return "";
    }
  },
  computed: {
    ...mapGetters(["userList"]),
    tables() {
      const input = this.input;
      if (input) {
        return this.$store.state.userList.filter(data => {
          if (
            String(data.date)
              .toLowerCase()
              .indexOf(input) != -1 ||
            data.room.indexOf(input) != -1 ||
            data.uname.indexOf(input) != -1 ||
            String(data.temperature).indexOf(input) != -1
          ) {
            //此处根据具体需求判断
            return true;
          }
        });
      } else {
        return this.$store.state.userList;
      }
    }
  },
  // 在页面组件加载后调用
  mounted() {
    var list = [];
    var obj;
    $.ajax({
      url: "http://127.0.0.1:8000/userinfo/",
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
    this.$store.commit("changeUserList", list);
    // console.log(this.$store);
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.el-table .warning-row {
  background: #f56c6c;
}

.el-table .success-row {
  background: #f0f9eb;
}
</style>
