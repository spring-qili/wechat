<template>
  <nav class="navbar navbar-inverse">
    <div class="container-fluid">
      <!-- Brand and toggle get grouped for better mobile display -->
      <div class="navbar-header">
        <button
          type="button"
          class="navbar-toggle collapsed"
          data-toggle="collapse"
          data-target="#bs-example-navbar-collapse-1"
          aria-expanded="false"
        >
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
      </div>

      <!-- Collect the nav links, forms, and other content for toggling -->
      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
          <li
            v-for="(item,index) in routers"
            :key="item.id"
            :class="{active:index==currentIndex}"
            @click="activeHandler(index)"
          >
            <router-link :to="item.url">{{item.title}}</router-link>
          </li>
        </ul>

        <!-- <form class="navbar-form navbar-right">
          <div class="form-group">
            <input type="text" class="form-control" placeholder="Search" />
          </div>
          <button type="submit" class="btn btn-default">Submit</button>
        </form>-->
      </div>
      <!-- /.navbar-collapse -->
    </div>
    <!-- /.container-fluid -->
  </nav>
</template>

<script>
import "bootstrap/dist/css/bootstrap.min.css";
export default {
  name: "Header",
  data() {
    return {
      routers: [
        { url: "/", title: "首页" },
        { url: "/user", title: "观影人员" },
        { url: "/unnormal", title: "异常人员" }
      ],
      currentIndex: 0
    };
  },
  methods: {
    activeHandler(index) {
      this.currentIndex = index;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
