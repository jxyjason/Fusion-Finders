<template>
  <div class="page">
    <header class="header">
      <img src="../../assets/logo.png" alt="logo" class="logo" />

      <h1 class="title">
        <span
            v-for="(char, index) in title"
            :key="index"
            :style="{ animationDelay: index * 0.1 + 's' }"
        >{{ char }}</span
        >
      </h1>
    </header>

    <div class="container">
      <p class="tip">上传多角度视频，建模精度更高</p>

      <v-card class="card-container" shadow="hover" >
        <form class="form">
          <div class="form-item">
            <label for="nickname">昵称</label>

            <input type="text" id="nickname" name="nickname" required />
          </div>

          <div class="form-item">
            <label for="email">邮箱</label>

            <input type="email" id="email" name="email" required />
          </div>
          <v-btn
              color="primary"
              size="large"
              @click="selectFile"
          >
            选择文件
          </v-btn>


          <progress-bar :progress="progress"></progress-bar>
        </form>

        <!-- 在这里使用进度条组件，并绑定progress变量 -->

      </v-card>
    </div>

    <div class="footer">

      <v-card class="safe" shadow="hover" style="border: none">
        <img src="./safe.png" style="position:relative;width: 80px;left: 30%;">
        <h5>安全保障</h5>
        <p>
          我们将立即删除已上传的文件，并在 24小时后删除已转换的文件。任何人都无法访问您的文件，我们可确保您的隐私100% 安全。
        </p>
      </v-card>

      <v-card class="app" shadow="hover" style="border: none" >
        <img src="./multy.png" style="position:relative;width: 80px;left: 30%;">
        <h5>多端支持</h5>
        <p>
          FusionFinders 基于浏览器并支持所有平台。您无需下载与安装任何软件。
        </p>
      </v-card>

      <v-card class="cloud" shadow="hover" style="border: none">
        <img src="./cloud.png" style="position:relative;width: 80px;left: 30%;">
        <h5>云端处理</h5>
        <p>所有转换都在云端进行，不会消耗您计算机的资源。</p>
      </v-card>

    </div>
  </div>
</template>

<script>
// 在这里导入进度条组件

import ProgressBar from "./ProgressBar.vue";
import Swal from 'sweetalert2'

export default {
  // 在这里注册进度条组件

  components: {
    ProgressBar,
  },

  data() {
    return {
      title: "上传视频，生成个性化3D模型",

      content: "这是一些文本内容",

      className: "text",

      fileInput: null, // 用来存储一个文件输入元素

      // 在这里定义一个progress变量，初始值为0

      progress: 0,email:'',name:'',
    };
  },

  methods: {
    selectFile() {
      // 获取昵称和邮箱的输入值

      let nickname = document.getElementById("nickname").value;
      this.name = nickname

      let email = document.getElementById("email").value;
      this.email = email

      // 检查昵称和邮箱是否为空

      if (!nickname || !email) {
        // 如果为空，弹出提示信息不完全
        Swal.fire({
          title: 'Error!',
          text: '请将信息输入完整' +
              '\n'+'Please fill in the full information\n',
          icon: 'error',
          confirmButtonText: 'Cool'
        })

        return;
      }

      // 检查邮箱是否符合格式

      let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

      if (!emailRegex.test(email)) {
        // 如果不符合，弹出提示邮箱格式错误
        Swal.fire({
          title: 'Error!',
          text: '请填写正确的邮箱格式' +
              '\n'+'Please fill in the correct mailbox format\n',
          icon: 'error',
          confirmButtonText: 'Cool'
        })
        // 返回，不继续执行后面的代码

        return;
      }

      this.fileInput = document.createElement("input");

      this.fileInput.type = "file";

      this.fileInput.accept = "video/*";

      this.fileInput.addEventListener("change", this.uploadFile);

      this.fileInput.click();
    },

    uploadFile() {
      let file = this.fileInput.files[0];

      if (!file) return;

      // 在这里修改progress的值，让它从0变到100

      this.progress = 100;


      // if(this.file.size<=524288000)
      this.axios.post('211.87.232.86:9093/upload',{
        "email":this.email,
        "name":this.name,
        "video":file
      }).then((response)=>{
        if(response.data===200){
          // 弹出提示信息
          Swal.fire({
            position: 'top-end',
            icon: 'success',
            title: '上传成功，管理员审核后会发送到您指定邮箱内\n' +
                'Upload successfully',
            showConfirmButton: false,
            timer: 1500
          })
        }
      }).catch((response)=>{
        console.log(response)
      })

      // 弹出提示信息
      Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: '上传成功，管理员审核后会发送到您指定邮箱内\n' +
            'Upload successfully',
        showConfirmButton: false,
        timer: 1500
      })



    },

    /*alert(message) {*/
    /*  let alert = document.createElement("div");*/

    /*  alert.className = "alert";*/

    /*  alert.textContent = message;*/

    /*  setTimeout(() => {*/
    /*    document.body.appendChild(alert);*/
    /*  }, 5200);*/

    //   // 把延时时间改为9s
    //
    //   setTimeout(() => {
    //     document.body.removeChild(alert);
    //     window.location.href = "/home";
    //   }, 3000);
    // },
  },
};
</script>

<style>
.page {
  margin: 0;
}

.header {
  background: linear-gradient(to bottom, #ecf1fa, #dfe8fe);

  display: flex;

  align-items: center;

  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);

  width: 100%;

  font-family: hy;

  height: 120px;
}

.logo {
  margin-left: 300px;

  margin-right: 100px;

  width: 120px;

  height: 120px;
}

.title {
  font-size: 150px;

  font-weight: bold;

  color: rgb(0, 0, 0);

  margin-left: 20px;
}

.title span {
  font-family: 钉钉进步体 Regular;
  opacity: 0;

  animation: fade-in 2s forwards;
}

.text {
  color: blue;
}

@keyframes fade-in {
  from {
    opacity: 0;

    transform: translateX(-20px);
  }

  to {
    opacity: 1;

    transform: translateX(0);
  }
}

@keyframes fade-out {
  from {
    opacity: 1;
  }

  to {
    opacity: 0;
  }
}

.container {
  font-family: 阿里妈妈数黑体 Bold;

  display: flex;

  flex-direction: column;

  align-items: center;
}

.tip {
  font-size: 24px;

  margin-top: 20px;

  font-family: 钉钉进步体 Regular;
}

/* .card {
  width: 600px;

  height: 300px;

  border: 2px solid #dfe8fe;

  border-radius: 50px;

  margin-top: 40px;

  display: flex;

  flex-direction: column;

  justify-content: center;

  align-items: center;

  background-image: linear-gradient(
      45deg,
      rgba(0, 0, 0, 0.06) 25%,
      transparent 0
    ),
    linear-gradient(-45deg, rgba(0, 0, 0, 0.06) 25%, transparent 0),
    linear-gradient(45deg, transparent 75%, rgba(0, 0, 0, 0.06) 0),
    linear-gradient(-45deg, transparent 75%, rgba(0, 0, 0, 0.06) 0);

  background-size: auto auto;

  background-repeat: repeat;
} */

/* .upload-button {
  width: 200px;

  height: 50px;

  background-color: #dfe8fe;

  border: none;

  border-radius: 5px;

  font-size: 18px;
} */

.alert {
  position: fixed;

  top: 50%;

  left: 50%;

  transform: translate(-50%, -50%);

  background-color: white;

  border-radius: 10px;

  padding: 20px;

  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);

  width: 400px;

  height: 100px;

  border: 2px solid rgba(0, 0, 0, 0.1);

  animation: fade-out 3s forwards;
}

.form {
  display: flex;

  flex-direction: column;
}

.form-item {
  margin: 10px;
}

.form-item label {
  display: block;

  font-size: 16px;
}

.form-item input {
  width: 300px;

  height: 30px;

  border: 1px solid gray;

  border-radius: 5px;
}

.submit-button {
  width: 100px;

  height: 40px;

  background-color: #dfe8fe;

  border: none;

  border-radius: 5px;
}

.card-container {
  width: 1050px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 4px solid #dfe8fe;
}

.iconfont {
  font-family: "iconfont" !important;
  font-size: 48px;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -webkit-text-stroke-width: 0.2px;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

.footer {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 120px;
}
.safe, .cloud, .app {
  width: 200px;
  height: 300px;
  justify-content: center;
  align-items: center;
  margin-right: 60px;

}
.safe i,
.safe h5 {
  display: block;
  text-align: center;
}

.safe p {
  font-size: 12px;
  color: rgba(0, 0, 0, 0.6);
  word-wrap: break-word;
  white-space: pre-wrap;
}

.app i,
.app h5 {
  display: block;
  text-align: center;
}

.app p {
  font-size: 12px;
  color: rgba(0, 0, 0, 0.6);
  word-wrap: break-word;
  white-space: pre-wrap;
}

.cloud i,
.cloud h5 {
  display: block;
  text-align: center;
}
.cloud p {
  font-size: 12px;
  color: rgba(0, 0, 0, 0.6);
  word-wrap: break-word;
  white-space: pre-wrap;
}

</style>
