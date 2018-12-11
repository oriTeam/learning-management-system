<template>
  <section>
    <div class="row mx-0">
      <div class="col-lg-4 col-sm-12">
        <div class="row" v-for="(img, i) in staticImage" :key="i">
          <img :src="img.src" alt="" class="m-2 w-100">
        </div>
      </div>
      <div class="col-lg-8 col-sm-12">
        <v-carousel class="my-2">
          <v-carousel-item
            v-for="(img,i) in carouselImages"
            :key="i"
            :src="img.src"
          ></v-carousel-item>
        </v-carousel>
        <div class="row w-100">
          <div class="col-lg-3 text-xs-center">
            <button class="btn sale-btn">Siêu giảm giá tháng 12</button>
          </div>
          <div class="col-lg-3 text-xs-center">
            <button class="btn sale-btn">Siêu giảm giá tháng 12</button>
          </div>
          <div class="col-lg-3 text-xs-center">
            <button class="btn sale-btn">Siêu giảm giá tháng 12</button>
          </div>
          <div class="col-lg-3 text-xs-center">
            <button class="btn sale-btn">Siêu giảm giá tháng 12</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
  export default {
    name: 'list',
    data() {
      return {
        staticImage: [
          {
            src: 'https://phongvu.vn/media/banner/pv-banner-390x190-b0f18.jpg'
          },
          {
            src: 'https://phongvu.vn/media/banner/pv-banner-390x190(15).png'
          },
          {
            src: 'https://phongvu.vn/media/banner/pv-banner-390x190-7e8da.jpg'
          },
        ],
        carouselImages: [
          {
            src: "https://phongvu.vn/media/banner/pv-banner-660x390-e7885.jpg",
          },
          {
            src: "https://phongvu.vn/media/banner/pv-banner-635x397-8e65c.jpg",
          },
          {
            src: "https://phongvu.vn/media/banner/pv-banner-635x397-34a51.jpg",
          },
          {
            src: "https://phongvu.vn/media/banner/pv-banner-660x390-21564.png",
          },
        ]
      }
    }
  }
</script>
<style>
  .sale-btn {
    height: 8.5rem;
    font-size: 16px;
    border: 1px solid;
    border-top-left-radius: 0px;
    border-xtop-right-radius: 0px;
  }
</style>
