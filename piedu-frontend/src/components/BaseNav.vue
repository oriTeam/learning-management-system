<template>
    <nav class="navbar"
         :class="[
            {'navbar-expand-lg': expand},
            {[`navbar-${effect}`]: effect},
            {'navbar-transparent': transparent},
            {[`bg-${type}`]: type},
            {'rounded': round},
            {'nav-fixed' : navFixed}
         ]">
        <div :class="['container',
        {'py-0': navFixed}]">
            <slot name="container-pre"></slot>
            <slot name="brand">
                <a class="navbar-brand" href="#" @click.prevent="onTitleClick">
                    {{title}}
                </a>
            </slot>
            <navbar-toggle-button :toggled="toggled"
                                  :target="contentId"
                                  @click.native.stop="toggled = !toggled">
            </navbar-toggle-button>

            <slot name="contai  ner-after"></slot>

            <div class="collapse navbar-collapse" :class="{show: toggled}" :id="contentId" v-click-outside="closeMenu">
                <div class="navbar-collapse-header">
                    <slot name="content-header" :close-menu="closeMenu"></slot>
                </div>
                <slot :close-menu="closeMenu"></slot>
            </div>
        </div>
    </nav>
</template>
<script>
    import {FadeTransition} from "vue2-transitions";
    import NavbarToggleButton from "./NavbarToggleButton";

    export default {
        name: "base-nav",
        components: {
            FadeTransition,
            NavbarToggleButton
        },
        props: {
            type: {
                type: String,
                default: "primary",
                description: "Navbar type (e.g default, primary etc)"
            },
            title: {
                type: String,
                default: "",
                description: "Title of navbar"
            },
            contentId: {
                type: [String, Number],
                default: Math.random().toString(),
                description:
                    "Explicit id for the menu. By default it's a generated random number"
            },
            effect: {
                type: String,
                default: "dark",
                description: "Effect of the navbar (light|dark)"
            },
            round: {
                type: Boolean,
                default: false,
                description: "Whether nav has rounded corners"
            },
            transparent: {
                type: Boolean,
                default: false,
                description: "Whether navbar is transparent"
            },
            expand: {
                type: Boolean,
                default: false,
                description: "Whether navbar should contain `navbar-expand-lg` class"
            }
        },
        data() {
            return {
                navFixed: false,
                toggled: false
            };
        },
        created() {
            window.addEventListener('scroll', this.isNavFixed);
        },
        destroyed() {
            window.removeEventListener('scroll', this.isNavFixed);
        },
        methods: {
            onTitleClick(evt) {
                this.$emit("title-click", evt);
            },
            closeMenu() {
                this.toggled = false;
            },
            isNavFixed: function (e) {
                let supportPageOffset = window.pageXOffset !== undefined;
                let isCSS1Compat = ((document.compatMode || "") === "CSS1Compat");
                let scrollTop = supportPageOffset ? window.pageYOffset : isCSS1Compat ?
                    document.documentElement.scrollTop : document.body.scrollTop;
                this.navFixed = (scrollTop > 30);
            }
        }
    };
</script>
<style>
    .nav-fixed {
        /*position: fixed !important;*/
        background: linear-gradient(135deg, rgb(134, 120, 210) 0%, rgb(119, 149, 248) 100%);
        box-shadow: 0px 5px 23px 0px rgba(0, 0, 0, 0.1);
        padding-top: 8px !important;
        padding-bottom: 8px !important;
    }
    .navbar-transparent {
        position: fixed !important;
    }
</style>
