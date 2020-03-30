// 主页面
<template>
  <div id="app">
    <Header></Header>
    <router-view />
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
// 组件的嵌套，需要在components中声明
import Header from "./components/Header";
// import store from "./store";
import $ from "jquery";
export default {
  name: "App",
  components: {
    Header
  },
  created() {
    this.myInterval = window.setInterval(() => {
      setTimeout(function() {
        $.ajax({
          url: "http://127.0.0.1:8000/monitor/",
          methods: "get",
          async: false,
          success: function(data) {
            if (data == 0) {
              alert("出现体温异常上报，请立即查看！");
            }
          }
        });
      }, 0);
    }, 300000);
  },
  destroyed() {
    clearInterval(this.myInterval);
  }
};
</script>

<style>
</style>
