var mLayout = function () {
    var t, e, a, n = function () {
        0 !== $("#m_aside_left_hide_toggle").length && (n = new mToggle("m_aside_left_hide_toggle", {
            target: "body",
            targetState: "m-aside-left--hide",
            togglerState: "m-brand__toggler--active"
        })).on("toggle", function (e) {
            t.pauseDropdownHover(800), Cookies.set("sidebar_hide_state", e.getState())
        })
    };
    return {
        init: function () {
            this.initHeader(), this.initAside()
        },
        initHeader: function () {
            var t, e, a;
            e = mUtil.get("m_header"), a = {
                offset: {},
                minimize: {}
            }, "hide" == mUtil.attr(e, "m-minimize-mobile") ? (a.minimize.mobile = {}, a.minimize.mobile.on = "m-header--hide", a.minimize.mobile.off = "m-header--show") : a.minimize.mobile = !1, "hide" == mUtil.attr(e, "m-minimize") ? (a.minimize.desktop = {}, a.minimize.desktop.on = "m-header--hide", a.minimize.desktop.off = "m-header--show") : a.minimize.desktop = !1, (t = mUtil.attr(e, "m-minimize-offset")) && (a.offset.desktop = t), (t = mUtil.attr(e, "m-minimize-mobile-offset")) && (a.offset.mobile = t), new mHeader("m_header", a), $("#m_aside_header_topbar_mobile_toggle").click(function () {
                $("body").toggleClass("m-topbar--on")
            }), 0 !== $("#m_quicksearch").length && new mQuicksearch("m_quicksearch", {
                mode: mUtil.attr("m_quicksearch", "m-quicksearch-mode"),
                minLength: 1
            }).on("search", function (t) {
                t.showProgress(), $.ajax({
                    url: "https://keenthemes.com/metronic/preview/inc/api/quick_search.php",
                    data: {
                        query: t.query
                    },
                    dataType: "html",
                    success: function (e) {
                        t.hideProgress(), t.showResult(e)
                    },
                    error: function (e) {
                        t.hideProgress(), t.showError("Connection error. Pleae try again later.")
                    }
                })
            }), new mScrollTop("m_scroll_top", {
                offset: 300,
                speed: 600
            })
        },
        initAside: function () {
            var o, i, l, r, s, d, c, m;
            l = mUtil.get("body"), r = mUtil.get("m_aside_left"), s = mUtil.hasClass(r, "m-aside-left--offcanvas-default") ? "m-aside-left--offcanvas-default" : "m-aside-left", e = new mOffcanvas("m_aside_left", {
                baseClass: s,
                overlay: !0,
                closeBy: "m_aside_left_close_btn",
                toggleBy: {
                    target: "m_aside_left_offcanvas_toggle",
                    state: "m-brand__toggler--active"
                }
            }), mUtil.hasClass(l, "m-aside-left--fixed") && (mUtil.addEvent(r, "mouseenter", function () {
                i && (clearTimeout(i), i = null), o = setTimeout(function () {
                    mUtil.hasClass(l, "m-aside-left--minimize") && mUtil.isInResponsiveRange("desktop") && (mUtil.removeClass(l, "m-aside-left--minimize"), mUtil.addClass(l, "m-aside-left--minimize-hover"), t.scrollerUpdate(), t.scrollerTop())
                }, 300)
            }), mUtil.addEvent(r, "mouseleave", function () {
                o && (clearTimeout(o), o = null), i = setTimeout(function () {
                    mUtil.hasClass(l, "m-aside-left--minimize-hover") && mUtil.isInResponsiveRange("desktop") && (mUtil.removeClass(l, "m-aside-left--minimize-hover"), mUtil.addClass(l, "m-aside-left--minimize"), t.scrollerUpdate(), t.scrollerTop())
                }, 500)
            })), c = mUtil.get("m_ver_menu"), m = "1" === mUtil.attr(c, "m-menu-dropdown") ? "dropdown" : "accordion", "1" === mUtil.attr(c, "m-menu-scrollable") && (d = {
                height: function () {
                    return mUtil.getViewPort().height - parseInt(mUtil.css("m_header", "height")) - 60
                }
            }), t = new mMenu("m_ver_menu", {
                scroll: d,
                submenu: {
                    desktop: {
                        default: m,
                        state: {
                            body: "m-aside-left--minimize",
                            mode: "dropdown"
                        }
                    },
                    tablet: "accordion",
                    mobile: "accordion"
                },
                accordion: {
                    autoScroll: !1,
                    expandAll: !1
                }
            }), 0 !== $("#m_aside_left_minimize_toggle").length && (a = new mToggle("m_aside_left_minimize_toggle", {
                target: "body",
                targetState: "m-brand--minimize m-aside-left--minimize",
                togglerState: "m-brand__toggler--active"
            })).on("toggle", function (e) {
                horMenu.pauseDropdownHover(800), t.pauseDropdownHover(800), Cookies.set("sidebar_toggle_state", e.getState())
            }), n(), this.onLeftSidebarToggle(function (t) {
                var e = $(".m-datatable");
                $(e).each(function () {
                    $(this).mDatatable("redraw")
                })
            })
        },
        getAsideMenu: function () {
            return t
        },
        onLeftSidebarToggle: function (t) {
            a && a.on("toggle", t)
        },
        closeMobileAsideMenuOffcanvas: function () {
            mUtil.isMobileDevice() && e.hide()
        }
    }
}();
$(document).ready(function () {
    !1 === mUtil.isAngularVersion() && mLayout.init()
});