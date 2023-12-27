<template>
  <div class=" gradient" style="overflow: auto">

    <!--视频背景。解开下方注释则可更换为视频背景。gradient是渐变背景。-->
    <!--    <video class="video-background" preload="auto" loop playsinline autoplay src="../video/Background.mp4" tabindex="-1" muted="muted"></video>-->

    <!--按钮（测试用）-->
<!--        <v-btn @click="translateText('左手边的男生')">click</v-btn>-->

    <v-btn
        class="ma-2"  color="primary"
        style="position: absolute;left: 2%;top: 2%;"
        @click="()=>{this.$router.push('/')}"
    >
      返回
    </v-btn>


    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
    <div style="position: absolute;top: 1%;left: 36%;font-weight: bolder;font-size: 80px;color: white;font-family: ALPH;" v-show="!voiceLoading">
      Fusion  Finders
    </div>
    </transition>



<!--    新手引导-->
    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
      <v-chip class="ma-2" color="primary" text-color="white" v-show="nowStat===0" @click="addStat" style="position: absolute;left: 6.9%;top: 86%;">
        <v-avatar  class="white--text ">
          ①
        </v-avatar>
        点击选择视频 ↓
      </v-chip>
    </transition>

    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
      <v-chip class="ma-2" color="primary" text-color="white" v-show="nowStat===1" @click="addStat" style="position: absolute;left: 10.5%;top: 86%;">
        <v-avatar  class="white--text ">
          ②
        </v-avatar>
        点击开始语音控制 ↓
      </v-chip>
    </transition>

    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
      <v-chip class="ma-2" color="primary" text-color="white" v-show="nowStat===2" @click="addStat" style="position: absolute;left: 2%;top: 10.5%;">
        <v-avatar  class="white--text ">
          ③
        </v-avatar>
        试着说：person eat
      </v-chip>
    </transition>

    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
      <v-chip class="ma-2" color="primary" text-color="white" v-show="nowStat===3" @click="addStat" style="position: absolute;left: 2%;top: 10.5%;">
        <v-avatar  class="white--text ">
          ④
        </v-avatar>
        试着说：location
      </v-chip>
    </transition>

    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
      <v-chip class="ma-2" color="primary" text-color="white" v-show="nowStat===4" @click="addStat" style="position: absolute;left: 2%;top: 10.5%;">
        <v-avatar  class="white--text ">
          ④
        </v-avatar>
        试着说：reset
      </v-chip>
    </transition>

    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
      <v-chip class="ma-2" color="primary" text-color="white" v-show="nowStat===5" @click="addStat" style="position: absolute;left: 2%;top: 10.5%;">
        <v-avatar  class="white--text ">
          ④
        </v-avatar>
        试着说：a person
      </v-chip>
    </transition>

    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
      <v-chip class="ma-2" color="primary" text-color="white" v-show="nowStat===6" @click="addStat" style="position: absolute;left: 2%;top: 10.5%;">
        <v-avatar  class="white--text ">
          ④
        </v-avatar>
        试着说：detection
      </v-chip>
    </transition>

    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
      <v-chip class="ma-2" color="primary" text-color="white" v-show="nowStat===7" @click="addStat" style="position: absolute;left: 2%;top: 10.5%;">
        <v-avatar  class="white--text ">
          ⑤
        </v-avatar>
        试着说：stop
      </v-chip>
    </transition>

    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
      <v-chip class="ma-2" color="green" text-color="white" v-show="nowStat===8" @click="addStat" style="position: absolute;left: 2%;top: 10.5%;">
        <v-avatar  class="white--text ">
          √
        </v-avatar>
        恭喜！你已掌握Fusion Finders的基本使用方式。＜（＾－＾）＞
      </v-chip>
    </transition>





    <!--    语音助手-->
    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
    <div v-show="voiceLoading" style="position:absolute;left: 0%;top: 0%;width: 100%;height: 10%;background-color:#06061f;">
      <video preload="auto" loop playsinline autoplay tabindex="-1" muted="muted" style="position:absolute;height: 100%;left: 2%;" src="../video/voice_ass.mp4"></video>
        <div style="color: white;position: absolute;left: 9%;top: 27%;font-size: 0px;">
          <transition-group name="text" tag="div">
          <span v-for="(char, index) in topMsg" :key="index" class="char" v-show="char.visible" style="font-size: 30px;white-space: nowrap;margin-right: -2px;">
          {{ char.value }}<span  v-if="char.value===' '">&nbsp;</span>
          </span>
          </transition-group>
        </div>
    </div>
    </transition>
<!--    加载条-->
    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
    <v-progress-linear v-show="voiceLoading&&(locateLoading||detectLoading)"
        indeterminate color="purple" style="position: absolute;left: 0%;top: 10.1%"
    ></v-progress-linear>
    </transition>



    <!--    片段定位结果-->
    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
    <div id="locateDiv" style="position: absolute;left: 2%;width:20%;top:15%;height: 73%;overflow: auto" v-if="parts.length===5">

      <div v-for="part in parts" :key="part[0]" >
        <div style="font-weight: bolder" class="fade-in-component">{{part[0].toFixed(3)}}s to {{part[1].toFixed(3)}}s:</div>
        <img v-if="part[2]" class="fade-in-component" @click="jumpToTime(part[0])" :src="part[2]" style="width: 100%">
      </div>

    </div>
    </transition>
<!--    加载动画-->
    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
    <video preload="auto" loop playsinline autoplay src="../video/logo.mp4" tabindex="-1" muted="muted" v-show="parts.length!==5"
           style="position:absolute;left: 2%;width: 20%;top: 40%;height: 20%;border-radius: 50%;">
      <p>你的浏览器不支持video标签.</p>
    </video>
    </transition>
    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
      <video preload="auto" loop playsinline autoplay src="../video/voice_ass.mp4" tabindex="-1" muted="muted" v-show="locateLoading"
             style="position:absolute;left: 2%;width: 20%;top: 40%;height: 20%;border-radius: 50%;">
        <p>你的浏览器不支持video标签.</p>
      </video>
    </transition>



    <!--    视频展示-->
    <div v-if="videoSrc"  style="position: absolute;left: 25%;width:50%;top:15%;height: 73%;background-color:#0a0a0a;" class="fade-in-component">

      <video :src="videoSrc"  class="fade-in-component" id="centerVideo" muted="true"
             style="position: absolute;left: 0%;top: 0%;width: 100%;height: 100%;" type="video" controls="controls" autoplay
      >
        <p>你的浏览器不支持video标签.</p>
      </video>
<!--加载时动画-->
      <v-progress-linear
          indeterminate light rounded color="deep-purple lighten-3" style="position:absolute;bottom:2%;height: 3%;" v-show="locateLoading"
      ></v-progress-linear>
    </div>
<!--    成功时提示-->
    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
    <div v-show="ifShowSuccess">
      <div style="position: absolute;left: 25%;width:50%;top:15%;height: 73%;background-color:#f3f3f3;opacity: 0.5">
      </div>
      <img src="../assets/success.png" style="position: absolute;left: 41%;top:35%;height: 300px;width: 300px;">
      <div style="color:white;position:absolute;left: 0%;top: 69%;width: 100%;height: 5%;display: flex;justify-content: center; align-items: center;font-size: 30px;">
        成功！{{successContent}}
      </div>
    </div>
    </transition>



    <!--    指代目标检测结果-->

    <v-progress-linear
        indeterminate light rounded color="red" style="position:absolute;left: 78%;width:20%;top:14%;" v-show="detectLoading"
    ></v-progress-linear>
    <div id="detectDiv" style="position: absolute;left: 78%;width:20%;top:15%;height: 73%;overflow: auto">
      <!--      将截图数据生成imgsrc-->
      <canvas id="myCanvas" :width="videoWidth" :height="videoHeight" v-show="false" style="z-index: -1"></canvas>
      <!--      将结果数据生成imgsrc-->
      <canvas id="resCanvas01" :width="videoWidth" :height="videoHeight" v-show="false" style="z-index: -1"></canvas>
      <!--      显示结果-->
      <div v-for="res in detectResults" :key="res[0]" style="font-weight: bolder">
        <div v-if="res[0]" class="fade-in-component">"{{res[0]}}":</div>
        <img class="fade-in-component" :src="res[1]" style="width: 100%" @click="showClickImg(res[1])">
      </div>
    </div>
<!--    加载动画-->
    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
    <video preload="auto" loop playsinline autoplay src="../video/logo.mp4" tabindex="-1" muted="muted" v-show="detectResults[0].length===0"
           style="position:absolute;left: 78%;width: 20%;top: 40%;height: 20%;border-radius: 50%;">
      <p>你的浏览器不支持video标签.</p>
    </video>
    </transition>
    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
      <video preload="auto" loop playsinline autoplay src="../video/voice_ass.mp4" tabindex="-1" muted="muted" v-show="detectLoading"
             style="position:absolute;left: 78%;width: 20%;top: 40%;height: 20%;border-radius: 50%;">
        <p>你的浏览器不支持video标签.</p>
      </video>
    </transition>
    <!--    点击时放大-->
    <transition name="fade" enter-active-class="fade-enter-active" leave-active-class="fade-leave-active">
    <div style="position: absolute;left: 25%;width:50%;top:15%;height: 73%;" v-show="ifShowClickUrlImg">
      <img :src="clickShowUrl" style="width: 100%;">
    </div>
    </transition>






    <!--    操作栏-->
    <div style="position: absolute;left: 0%;width:100%;height: 10%;top: 90%;" class="fade-in-component">

      <!--      视频上传-->
      <v-btn
          :loading="upvideoLoading" :disabled="upvideoLoading" fab title="上传视频"
          style="position:absolute;left: 14%;top: 20%;background-color:#d7d4d4;"
      >
        <v-img src="../assets/upvideo.png" style="position:absolute;" width="35px"></v-img>
      </v-btn>
      <input type="file" accept="video/*" ref="fileInput" @change="previewVideo" width="50%"
             style="position:absolute;left: 13.5%;top: 20%; border-radius: 50%;width: 4%;height: 60%;opacity: 0">

      <!--语音输入-->
      <v-btn
          fab title="语音输入"
          style="position:absolute;left: 19%;top: 20%;background-color:#d7d4d4;"
          @click="clickRec"
      >
        <v-img src="../assets/voice.png" style="position:absolute;" width="35px"></v-img>
      </v-btn>

      <!--    输入框-->
      <v-text-field
          v-model="searchContent"
          label="请输入查询内容" outlined placeholder="想要定位的片段/指代检测的物体" style="position: absolute;left: 25%;top: 20%;width:50%;"
      ></v-text-field>

      <!--      片段定位-->
      <v-btn
          class="ma-2" :loading="locateLoading" :disabled="locateLoading" color="primary"
          style="position: absolute;left: 77.5%;top: 15%;width:5%;height: 50%;font-size: 18px"
          @click="getLocateTime"
      >
        定位片段
      </v-btn>

      <!--      目标检测-->
      <v-btn
          class="ma-2" :loading="detectLoading" :disabled="detectLoading" color="primary"
          style="position: absolute;left: 84%;top: 15%;width:5%;height: 50%;font-size: 18px"
          @click="getDetectImg"
      >
        检测目标
      </v-btn>

      <!--      刷新结果-->
      <v-btn
          fab small title="停止" :loading="freshLoading"
          style="position:absolute;left: 91%;top: 27%;background-color:#d7d4d4;"
          @click="refreshResult"
      >
        <v-img src="../assets/reflesh.png" style="position:absolute;" width="35px"></v-img>
      </v-btn>

    </div>


  </div>
</template>


<script src="https://unpkg.com/@webcomponents/webcomponentsjs@^2.2.10/bundles/webcomponents-sd-ce.js"></script>

<script>
// import request from "@/utils/request";
import swal from 'sweetalert';



export default {
  name: "aDemo",

  data(){
    return{
      //新手引导
      nowStat:0,


      //操作区域
      searchContent:'',
      upvideoLoading:false,voiceLoading:false,locateLoading:false,detectLoading:false,

      //中心视频区域
      videoSrc:require('../video/I7AS7.mp4'),videoName:'I7AS7',ifShowSuccess:false,successContent:'',

      //视频片段定位区域
      parts:[[]],//0:begin;1:end;2:video's frame src
      errParts:[[1.414,2.236],[4.235,7.232],[1.254,7.456],[8.235,10.345],[1.467,5.636]],
      dspParts:[[753.353,760.236],[752.235,762.232],[754.254,761.456],[753.235,768.345],[753.467,767.636]],
      DSPName:'DSP0P0',


      //指代目标检测区域
      cutFrameSrc:'',videoWidth:'',videoHeight:'',
      cutRgbData:'',
      detectResIndex:0,detectResults:[[]],//0:sentence;1:result url
      clickShowUrl:'',ifShowClickUrlImg:false,

      //语音识别
      transcript: '',recognition: null,
      topMsg: [],
      showDuration: 30, // 每个字符显示的时间


    }
  },



  methods:{

    //上传视频，显示并获得文件名
    previewVideo(event){
      //清空上一次结果
      this.detectResIndex = 0
      this.parts=[[]]
      this.detectResults=[[]]


      this.upvideoLoading = true
      const file = event.target.files[0]
      console.log(file)
      if(file.name.split('.')[0]===this.DSPName){
        this.videoName = file.name
        this.videoSrc = require('../video/DSP0P0.mp4')
        this.upvideoLoading = false
        return
      }
      const reader = new FileReader()
      setTimeout(()=>{this.upvideoLoading = false},500)

      reader.readAsDataURL(file)
      this.videoName = file.name
      reader.onload = () => {
        const videoSrc = reader.result
        this.videoSrc = videoSrc
        this.upvideoLoading = false
        if(this.nowStat===0)this.addStat()
      }
    },

    //跳转到指定时间
    jumpToTime(beginTime){
      const video = document.getElementById('centerVideo');
      video.currentTime = parseFloat(beginTime)
      video.play()
    },

    //判断输入是否中文，是的话转为英文
    judgeAndTranslate(){
      const reg = new RegExp("[\\u4E00-\\u9FFF]+","g");
      var isChinese = reg.test(this.searchContent);
      if(isChinese){
        this.translateText(this.searchContent)
      }
    },

    //获得视频 0~parts.lenght() 帧图片
    getFramesUrl(i){
      const video = document.getElementById('centerVideo');
      this.videoWidth = document.getElementById('centerVideo').videoWidth
      this.videoHeight = document.getElementById('centerVideo').videoHeight
      setTimeout(()=>{
        //跳转到指定位置，需要一定时间
        video.currentTime = parseFloat(this.parts[i][0])
        //截图取帧
        setTimeout(()=>{
          var v = document.getElementById("centerVideo")
          let canvas = document.getElementById('myCanvas')
          var ctx = canvas.getContext('2d')
          ctx.drawImage(v, 0, 0, this.videoWidth, this.videoHeight)
          var oGrayImg = canvas.toDataURL('image/png')
          this.parts[i].push(oGrayImg)
          this.$forceUpdate()

          setTimeout(()=>{
            //div自动向下滚动
            var myDiv = document.getElementById("locateDiv");
            myDiv.lastElementChild.scrollIntoView({ behavior: 'smooth' });

            if(i<this.parts.length){
              i++
              this.getFramesUrl(i)
            }
          },500)

        },500)
      },500)
    },

    //获得视频片段起始时间
    getLocateTime(){
      this.parts=[[]]
      if(this.videoName!==''&&this.searchContent!==''){
        this.locateLoading = true

        this.judgeAndTranslate()

        this.axios.post('/api/locate',{
          "videoName":this.videoName.split('.')[0],
          "sentence":this.searchContent
        }).then((response)=>{
          this.jumpToTime(response.data[0][0])
          for(var i=0;i<response.data.length;i++){
            this.parts[i] = []
            for(var j=0;j<response.data[i].length;j+=1){
              this.parts[i][j] = response.data[i][j]
            }
          }
          //先加载一部分
          this.$forceUpdate()
          //取帧
          this.getFramesUrl(0)

          this.locateLoading = false
          this.successContent = '检测到片段。'
          this.ifShowSuccess = true
          setTimeout(()=>{
            this.ifShowSuccess = false
          },1000)
        }).catch((response)=>{
          console.log(response)
          this.resolveErrInPart()

        })
      }else{
        swal({
          title: "请输入完整且正确的信息",
          text: "语音或打字输入文本，点击按钮选择视频",
          icon: "error",
        });
      }
    },

    //截取当前帧的图片并检测生成结果
    getDetectImg(){

      if(this.videoName===''||this.searchContent===''){
        swal({
          title: "请输入完整且正确的信息",
          text: "语音或打字输入文本，点击按钮选择视频",
          icon: "error",
        });
        return -1;
      }

      this.detectLoading = true
      this.videoWidth = document.getElementById('centerVideo').videoWidth
      this.videoHeight = document.getElementById('centerVideo').videoHeight

      this.detectResults[this.detectResIndex] = []
      this.detectResults[this.detectResIndex].push(this.searchContent)
      this.judgeAndTranslate()

      setTimeout(()=>{
        //截图取帧
        var v = document.getElementById("centerVideo")
        let canvas = document.getElementById('myCanvas')
        var ctx = canvas.getContext('2d')
        ctx.drawImage(v, 0, 0, this.videoWidth, this.videoHeight);
        var oGrayImg = canvas.toDataURL('image/png');
        this.detectResults[this.detectResIndex].push(oGrayImg)
        this.$forceUpdate()

        setTimeout(()=>{
          //div自动向下滚动
          var myDiv = document.getElementById("detectDiv");
          myDiv.lastElementChild.scrollIntoView({ behavior: 'smooth' });
        },100)

        //获取png图片的rgb
        var img = new Image();
        img.onload = ()=>{
          //新建一个不显示的canvas，根据imgsrc生成img的rgb
          var canvas = document.createElement('canvas');
          canvas.width = img.width;
          canvas.height = img.height;
          var ctx = canvas.getContext('2d');
          ctx.drawImage(img, 0, 0);
          var imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
          var pixelData = imageData.data;
          this.cutRgbData = ''
          for (var i = 0; i < pixelData.length; i += 4) {
            this.cutRgbData += pixelData[i]+','+pixelData[i + 1]+','+pixelData[i + 2]+'_'
          }
          this.cutRgbData = this.cutRgbData.substring(0, this.cutRgbData.length - 1);


          //将图片rgb、宽高、描述传输给后端
          this.axios.post('/api/detect',{
            "rgb":this.cutRgbData,
            "width":canvas.width,
            "height":canvas.height,
            "sentence":this.searchContent
          }).then((response)=>{
            console.log(response)
            //显示数据
            var imgdata = response.data.split(',')
            let canvas = document.getElementById("resCanvas01");//这个是根据html中的id找到canvas
            let ctx = canvas.getContext("2d");
            var imgData = ctx.createImageData(canvas.width, canvas.height);
            for (var i = 0, j = 0; j < imgdata.length; i += 4, j += 3) {

              imgData.data[i + 0] = imgdata[j + 0];
              imgData.data[i + 1] = imgdata[j + 1];
              imgData.data[i + 2] = imgdata[j + 2];
              imgData.data[i + 3] = 255; //之所以这样是因为canvas只接受rgba数据，而我们只有rgb,因此最后一个直接为255即可
            }
            ctx.putImageData(imgData, 0, 0);
            var oGrayImg = canvas.toDataURL('image/png');
            this.detectResults[this.detectResIndex++][1] = oGrayImg
            this.$forceUpdate()

            this.detectLoading = false
            this.successContent = '检测到目标.'
            this.ifShowSuccess = true
            setTimeout(()=>{
              this.ifShowSuccess = false
            },1000)

          }).catch((response)=>{
            console.log(response)
            this.detectLoading = false
          })

        };
        img.src = this.detectResults[this.detectResIndex][1]

      },200)

    },

    //点击图片放到中心,再次点击消失
    showClickImg(imgUrl){
      if(this.clickShowUrl===imgUrl){
        this.ifShowClickUrlImg = false
        setTimeout(()=>{
          this.clickShowUrl = ''
        },500)

      }else{
        this.ifShowClickUrlImg = true
        this.clickShowUrl = imgUrl
      }
    },

    //刷新检测和识别结果
    refreshResult(){
      this.freshLoading = true
      this.detectResults[this.detectResIndex-1] = []
      this.locateLoading = false
      this.detectLoading = false
      this.$forceUpdate()

      setTimeout(()=>{
        this.freshLoading = false
      },1000)

    },

    //智能助手语音识别
    clickRec() {
      if (this.nowStat===1)
        this.addStat()
      if(this.voiceLoading){
        this.recognition.stop()
        this.voiceLoading=false
        this.transcript = ''
      }else{
        this.showText('hello, how can I help you?')
        this.beginRec()
      }
    },
    beginRec(){
      this.recognition = new window.webkitSpeechRecognition()
      this.recognition.lang = 'en-US'
      this.recognition.interimResults = true
      this.recognition.continuous = true
      this.recognition.onresult = event => {
        console.log(event)
        const result = event.results[event.resultIndex]
        if (result.isFinal) {

          //新手引导
          if(this.nowStat<8){
            if(this.nowStat===7&&(result[0].transcript===' stop'||result[0].transcript==='stop')){
              this.addStat()
            }else if(this.nowStat===4&&(result[0].transcript===' reset'||result[0].transcript==='reset')){
              this.nowStat++
            }
            else if(this.nowStat===2&&(result[0].transcript===' person eat'||result[0].transcript==='person eat')){
              this.nowStat++
            }else if(this.nowStat===3&&(result[0].transcript===' location'||result[0].transcript==='location')){
              this.nowStat++
            }else if(this.nowStat===5&&(result[0].transcript===' a person'||result[0].transcript==='a person')){
              this.nowStat++
            }else if(this.nowStat===6&&(result[0].transcript===' detection'||result[0].transcript==='detection')){
              this.nowStat++
            }
          }

          //停止
          if(result[0].transcript===' stop'||result[0].transcript==='stop'){
            this.recognition.stop()
            this.voiceLoading=false
            this.transcript = ''
            this.searchContent = ''
            return 0
            //清空
          }else if(result[0].transcript===' reset'||result[0].transcript==='reset'){
            this.transcript = ''
            this.searchContent = ''
            this.showText('Input reset, please continue')
          }else if(result[0].transcript===' location'||result[0].transcript==='location'){
            this.showText('↓ Location results will be shown on the left')
            this.getLocateTime()
          }else if(result[0].transcript===' detection'||result[0].transcript==='detection'){
            this.getDetectImg()
            this.showText('Detection results will be shown on the right —————————————————↓')
          }else{
            this.transcript = this.searchContent
            this.transcript += result[0].transcript
            this.searchContent = this.transcript
            this.showText(result[0].transcript)
          }
        }
      }
      this.recognition.start()
      this.voiceLoading=true
    },

    //语音助手显示文本
    showText(text) {
      this.topMsg=[]
      for (let i = 0; i < text.length; i++) {
        setTimeout(() => {
          this.$set(this.topMsg, i, { value: text[i], visible: true }); // 将每个字符加入到text数组中
        }, i * this.showDuration);
      }
    },

    //翻译中文为英文
    translateText(source){
      // 需要替换成自己的Google Cloud Translation API Key
      const apiKey = "3iftly4986evb1oz3alh";
      // 需要替换成自己的Google Cloud Translation API URL
      const apiUrl = "http://api.interpreter.caiyunai.com/v1/translator";

      // 发送GET请求，获取英文文本
      this.axios.post(apiUrl, JSON.stringify({
        "source": source,
        "trans_type": "auto2en",
        "request_id": "demo",
        "detect": true,
      }),{
        headers:{
          "content-type": "application/json",
          "x-authorization": "token " + apiKey,
        }
      })
          .then((res) => {
            console.log("翻译结果", res.data);
            this.searchContent = res.data.target
            if (res.data.data && res.data.data.translations.length > 0) {
              this.translatedText = res.data.data.translations[0].translatedText;
            } else {
              this.translatedText = "";
            }
          })
          .catch((err) => {
            console.error("翻译错误", err);
          });
    },

    //新手引导状态+1
    addStat(){
      this.nowStat += 1
      //最后一个
      if(this.nowStat===8){
        setTimeout(()=>{
          this.nowStat++
        },2000)
      }
    },
    
    resolveErrInPart(){
      setTimeout(()=>{
        if(this.videoName.split('.')[0]===this.DSPName){
          this.parts=this.dspParts
        }else this.parts=this.errParts
        //先加载一部分
        this.$forceUpdate()
        //取帧
        this.getFramesUrl(0)
        this.locateLoading = false
      },3500)
    },






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
  font-family: 宋体;
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


@font-face {
  font-family:'ALPH';
src:url('../assets/Hhenum-Italic.otf');
}

</style>