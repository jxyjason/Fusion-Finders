<template>
  <div style="overflow: auto;">
<!--    <v-btn @click="turnToDijk">click</v-btn>-->

<!--    展示数据所用背景-->
<!--    <v-parallax style="position: absolute;width: 100%;left: 0%;top:70%;" height="285" dark src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"></v-parallax>-->
<!--    <v-parallax style="position: absolute;width: 100%;left: 0%;top:120%;box-shadow: 0 0 10px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 0, 0, 0.3);" height="475" dark src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg"></v-parallax>-->


    <!--title-->
    <img src="../assets/logo.png" style="position:absolute;left: 40%;width: 20%;top: 5%;border-radius: 50%;">
    <img src="../assets/logo_new.png" style="position:absolute;left: 45%;width: 10%;top: 10%;">
    <div style="position: absolute;left: 0%;top: 43%;width:100%;font-size: 36px;text-align: center;">
      模态探索者——将语音、文本、视频、图片融合起来的一次创新探索
    </div>

    <div style="position: absolute;left: 0%;top: 51%;width:100%;font-size: 15px;text-align: center;">
      所有处理皆在云端，无需消耗本地资源 <br><br>
      四种模态的有机融合
    </div>

<!--    github-->
    <a href="https://gitee.com/jxyjason/fusion-finders.git">
    <v-btn
        fab title="GitHub"
        style="position:absolute;left: 95%;top: 2%;background-color:#ffffff;"
    >
      <v-img src="../assets/github-fill.png" style="position:absolute;" width="58"></v-img>
    </v-btn>
    </a>
    <div style="position: absolute;left: 95.3%;top: 9%;font-size: 15px;text-align: center;">
      GitHub
    </div>



    <!--    四个入口-->
    <v-btn color="primary"  style="font-size:25px;position: absolute;left: 11%;top:63%;width: 12%;height: 6%;"  @click="turnToDemo" >
      <v-icon left size="26">
        mdi-account-outline
      </v-icon>
      新手入门
    </v-btn>

    <v-btn color="primary" style="font-size:25px;position: absolute;left: 28%;top:63%;width: 12%;height: 6%;" @click="turnToSuper">
      <v-icon left size="26">
        mdi-camera
      </v-icon>
      监控检索
    </v-btn>

    <v-btn color="primary" style="font-size:25px;position: absolute;left: 44%;top:63%;width: 12%;height: 6%;" @click="trunToRemote">
      <v-icon left size="26">
        mdi-heart
      </v-icon>
      远程关怀
    </v-btn>

    <v-btn color="primary" style="font-size:25px;position: absolute;left: 61%;top:63%;width: 12%;height: 6%;" @click="turnToAnimal">

        <img src="../assets/animal.png" style="position:relative;width: 9%;height: 9%;left: -2%">

      动物检测
    </v-btn>


    <div @mouseenter="ifShowRebuild=true" @mouseleave="leaveMouse()" >
      <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
      <v-btn color="primary" style="font-size:25px;position: absolute;left: 77%;top:56%;width: 12%;height: 6%;" @click="turnToRebuild" v-show="ifShowRebuild">
        <img src="../assets/rebuild3D.png" style="position:relative;width: 11%;height: 11%;left: -2%">
        场景还原
      </v-btn>
      </transition>
      <v-btn color="primary" style="font-size:25px;position: absolute;left: 77%;top:63%;width: 12%;height: 6%;" @click="trunToAccident">

        <img src="../assets/shigu.png" style="position:relative;width: 11%;height: 11%;left: -2%">

        事故处理
      </v-btn>
    </div>


<!--    数据-->
    <div class="container" style="position:absolute;left: 0%;height: 30%;width: 100%;top: 70%;font-size: 50px;font-weight: bolder">
      <count-to style="position:absolute;left: 13.4%;top: 22%; font-size:60px;color: #99BCAC;" :startVal='0' :endVal='7597' :duration=4000></count-to>
      <div style="position:absolute;left: 12.4%;top: 60%;font-size: 37px;font-weight: lighter;color: #99BCAC;">Line of Code</div>

      <count-to style="position:absolute;left: 45%;top: 22%;font-size:60px;color: #5F4321;" :startVal='0' :endVal='9831' :duration=4000></count-to>
      <div style="position:absolute;left: 39%;top: 60%;font-size: 37px;font-weight: lighter;color: #5F4321;">MegaByte Parameters</div>

      <count-to style="position:absolute;left: 75%;top: 22%;font-size:60px;color: #BA5140;" :startVal='0' :endVal='49627' :duration=4000></count-to>
      <div style="position:absolute;left: 72%;top: 60%;font-size: 37px;font-weight: lighter;color: #BA5140;">MegaByte Dataset</div>
    </div>


<!--    用的技术、四个模态之间的联系、简单介绍-->
    <div style="position:absolute;left: 0%;top: 100%;height: 100%;width: 100%;">

      <v-lazy
          v-model="isActive"
          :options="{
          threshold: .5
        }"
          min-height="200"
          transition="fade-transition"
      >
      <v-hover v-slot="{ hover }" style="position: absolute;left:13%;top: 7%">
        <v-card class="mx-auto" color="grey lighten-4" max-width="600">
          <v-img src="../assets/TAN.png">
            <v-expand-transition>
              <div v-if="hover" class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal text-h2 white--text" style="height: 100%;display: flex;justify-content: center; align-items: center; /* 垂直居中 */;">
                2D-TAN
              </div>
            </v-expand-transition>
          </v-img>
          <v-card-text class="pt-6" style="position: relative;">
            <h3 class="text-h4 font-weight-light orange--text mb-2">2D Temporal Adjacent Networks</h3>
            <div class="font-weight-light grey--text text-h6 mb-2">
              Text: Long Short Term Memory<br>
              Video: Convolutional Neural Network<br>
              Fusion: 2D Temporal Map
            </div>
            <div class="font-weight-light text-h6 mb-2">
              It can locate the video in the 2s according to the text.
            </div>
          </v-card-text>
        </v-card>
      </v-hover>
      </v-lazy>

      <v-lazy
          v-model="isActive"
          :options="{
          threshold: .5
        }"
          min-height="200"
          transition="fade-transition"
      >
      <v-hover v-slot="{ hover }" style="position: absolute;left:52%;top: 7%">
        <v-card class="mx-auto" color="grey lighten-4" max-width="600">
          <v-img src="../assets/LAVT.png">
            <v-expand-transition>
              <div v-if="hover" class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal text-h2 white--text" style="height: 100%;display: flex;justify-content: center; align-items: center; /* 垂直居中 */;">
                LAVT
              </div>
            </v-expand-transition>
          </v-img>
          <v-card-text class="pt-6" style="position: relative;">
            <h3 class="text-h4 font-weight-light orange--text mb-2">Language-Aware Vision Transformer</h3>
            <div class="font-weight-light grey--text text-h6 mb-2">
              Text: Bidirectional Encoder Representation from Transformers<br>
              Video: Transformer <br>
              Fusion: Pixel-Word Attention Module
            </div>
            <div class="font-weight-light text-h6 mb-2">
              It can divide the picture target according to the text.
            </div>
          </v-card-text>
        </v-card>
      </v-hover>
      </v-lazy>

      <v-hover v-slot="{ hover }" style="position: absolute;left:25%;top: 56%">
        <v-card class="mx-auto" color="grey lighten-4" max-width="100">
          <video style="width: 100%;border-radius: 50%" class="video-background" preload="auto" loop playsinline autoplay src="../video/voice_ass.mp4" tabindex="-1" muted="muted"></video>
            <v-expand-transition>
              <div v-if="hover" class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal white--text" style="height: 100%;display: flex;justify-content: center; align-items: center; /* 垂直居中 */;">
                Voice
              </div>
            </v-expand-transition>
        </v-card>
      </v-hover>

      <v-hover v-slot="{ hover }" style="position: absolute;left:40%;top: 56%">
        <v-card class="mx-auto" color="grey lighten-4" max-width="100">
          <video style="width: 100%;border-radius: 50%" class="video-background" preload="auto" loop playsinline autoplay src="../video/textVid.mp4" tabindex="-1" muted="muted"></video>
          <v-expand-transition>
            <div v-if="hover" class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal white--text" style="height: 100%;display: flex;justify-content: center; align-items: center; /* 垂直居中 */;">
              Text
            </div>
          </v-expand-transition>
        </v-card>
      </v-hover>

      <v-hover v-slot="{ hover }" style="position: absolute;left:57%;top: 56%">
        <v-card class="mx-auto" color="grey lighten-4" max-width="100">
          <video style="width: 100%;border-radius: 50%" class="video-background" preload="auto" loop playsinline autoplay src="../video/person_detect.mp4" tabindex="-1" muted="muted"></video>
          <v-expand-transition>
            <div v-if="hover" class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal white--text" style="height: 100%;display: flex;justify-content: center; align-items: center; /* 垂直居中 */;">
              Image
            </div>
          </v-expand-transition>
        </v-card>
      </v-hover>

      <v-hover v-slot="{ hover }" style="position: absolute;left:72%;top: 56%">
        <v-card class="mx-auto" color="grey lighten-4" max-width="100">
          <video style="width: 100%;border-radius: 50%" class="video-background" preload="auto" loop playsinline autoplay src="../video/video_cat_square.mp4" tabindex="-1" muted="muted"></video>
          <v-expand-transition>
            <div v-if="hover" class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal white--text" style="height: 100%;display: flex;justify-content: center; align-items: center; /* 垂直居中 */;">
              Video
            </div>
          </v-expand-transition>
        </v-card>
      </v-hover>






      <v-parallax
          height="285" style="position: absolute;top:70%;left: 0%;width: 100%;"
          src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg"
      ></v-parallax>
      <div class="container" style="position:absolute;left: 0%;height: 30%;width: 100%;top: 70%;font-size: 50px;font-weight: bolder">
        So, Try your video!&nbsp;&nbsp;&nbsp;
        <v-btn fab x-large color="green" style="color:#fff;font-size: 29px"  @click="turnToDetect">GO</v-btn>
      </div>

    </div>



  </div>
</template>

<script>

import countTo from 'vue-count-to';
  export default {

    name: 'Home',
    components: { countTo },
    data(){
      return{
        //展示数据量


        ifShowRebuild:false,






      }
    },



    methods:{

      turnToDetect(){this.$router.push('/detect')},
      turnToDemo(){this.$router.push('/aDemo')},
      turnToSuper(){this.$router.push('/supervisoryRetrieval')},
      trunToRemote(){this.$router.push('/remoteCare')},
      turnToAnimal(){this.$router.push('/animalDetect')},
      trunToAccident(){this.$router.push('/accidentDetect')},
      turnToRebuild(){this.$router.push('/submit3D')},
      leaveMouse(){
        setTimeout(()=>{this.ifShowRebuild=false},2000)
      }






    },

    mounted() {

    },


  }


</script>


<style scoped>


* {
  margin: 0;
  padding: 0;
}
/*视频背景*/
.video-box {
  position: relative;
  height: 100vh;
  background-color: #C1CFF7;
  /*进行视频裁剪*/
  overflow: hidden;
}

.video-box .video-background {
  position: absolute;
  left: 50%;
  top: 50%;
  /*保证视频内容始终居中*/
  transform: translate(-50%, -50%);
  width: 100%;
  height: 100%;
  /*保证视频充满屏幕*/
  object-fit: cover;
  min-height: 800px;
}

.gradient {
  /* 设置容器尺寸 - 原理1 */
  position: relative;
  height: 100vh;
  /* 背景渐变色 - 原理2 */
  background: linear-gradient(-45deg, #f4f0ff, #cec9f6, #cbdefa, #f8cef5);
  /* 背景尺寸 - 原理3 */
  background-size: 600% 600%;
  /* 循环动画 - 原理4 */
  animation: gradientBG 10s ease infinite;
}

/* 动画，控制背景 background-position */
@keyframes gradientBG {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}


/*渐变*/
.fade-in-component {
  opacity: 0; /* 初始状态为透明 */
  animation: fadeIn 1s ease-in-out forwards; /* 添加动画效果 */
}
/*逐渐进入和消失*/
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

/*文字依次显示*/
.text-enter-active {
  transition: opacity 0.5s ease-in-out;
}

.text-enter {
  opacity: 0;
}

.text-leave-active {
  transition: opacity 0.5s ease-in-out;
}

.text-leave-to {
  opacity: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0; /* 开始时透明 */
  }
  100% {
    opacity: 1; /* 结束时完全不透明 */
  }
}


/* 隐藏滚动条 */
div::-webkit-scrollbar {
  background-color: #f1f1f1;
  width: 0.5em;
}

div::-webkit-scrollbar-thumb {
  background-color: #f1f1f1;
}

.container {
  display: flex; /* 使用 flex 布局 */
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  border: 1px solid #ccc; /* 用于演示效果，可以去掉 */
  height: 200px; /* 用于演示效果，可以根据实际情况调整 */
}

.text {
  text-align: center; /* 文字水平居中 */
}

</style>