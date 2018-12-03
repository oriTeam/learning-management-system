<template>
    <form action="" class="row justify-content-center class-search">
        <div class="col-lg-7 col-sm-12">
            <div class="form-group row justify-content-center">
                <div class="col-lg-10 col-sm-12">
                    <input aria-describedby="addon-right addon-left" placeholder="Tìm kiếm lớp học"
                           class="form-control">
                </div>
                <div class="col-lg-2 col-sm-10 px-3 text-center mt-lg-0 mt-sm-3">
                    <base-button type="white">Tìm kiếm</base-button>
                </div>
            </div>
        </div>
    </form>
</template>
<style lang="scss">
    .class-search {
        padding-top: 150px;
    }
    @media (max-width: 992px) {
        .class-search {
            padding-left: 10%;
            padding-right: 10%;
            button {
                margin-top: 10px
            }
        }
    }
</style>
