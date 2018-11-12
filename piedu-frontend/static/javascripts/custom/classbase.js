var aside = `<div>
            <button class="m-aside-left-close  m-aside-left-close--skin-light " id="m_aside_left_close_btn"><i class="la la-close"></i></button>
            <div id="m_aside_left" class="m-grid__item	m-aside-left  m-aside-left--skin-light w-100 h-100">
                        <!-- BEGIN: Aside Menu -->
                        <div id="m_ver_menu"
                             class="m-aside-menu  m-aside-menu--skin-light m-aside-menu--submenu-skin-light "
                             m-menu-vertical="1" m-menu-scrollable="0" m-menu-dropdown-timeout="500">
                            <ul class="m-menu__nav  m-menu__nav--dropdown-submenu-arrow ">
                                <li class="m-menu__section m-menu__section--first">
                                    <h4 class="m-menu__section-text">Departments</h4>
                                    <i class="m-menu__section-icon flaticon-more-v3"></i>
                                </li>
                                <li class="m-menu__item m-menu__item--submenu" aria-haspopup="true"
                                    m-menu-submenu-toggle="hover"><a href="javascript:;"
                                                                     class="m-menu__link m-menu__toggle"><i
                                        class="m-menu__link-icon flaticon-layers"></i><span
                                        class="m-menu__link-text">Resources</span><i
                                        class="m-menu__ver-arrow la la-angle-right"></i></a>
                                    <div class="m-menu__submenu "><span class="m-menu__arrow"></span>
                                        <ul class="m-menu__subnav">
                                            <li class="m-menu__item  m-menu__item--parent" aria-haspopup="true"><span
                                                    class="m-menu__link"><span
                                                    class="m-menu__link-text">Resources</span></span>
                                            </li>
                                            <li class="m-menu__item " aria-haspopup="true"><a href="inner.html"
                                                                                              class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Timesheet</span></a></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Payroll</span></a></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Contacts</span></a></li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-suitcase"></i><span
                                        class="m-menu__link-text">Finance</span></a></li>
                                <li class="m-menu__item m-menu__item--submenu" aria-haspopup="true"
                                    m-menu-submenu-toggle="hover" m-menu-link-redirect="1"><a href="javascript:;"
                                                                                              class="m-menu__link m-menu__toggle"><i
                                        class="m-menu__link-icon flaticon-graphic-1"></i><span
                                        class="m-menu__link-title">  <span class="m-menu__link-wrap">      <span
                                        class="m-menu__link-text">Support</span>      <span
                                        class="m-menu__link-badge"><span
                                        class="m-badge m-badge--accent">3</span></span>  </span></span><i
                                        class="m-menu__ver-arrow la la-angle-right"></i></a>
                                    <div class="m-menu__submenu "><span class="m-menu__arrow"></span>
                                        <ul class="m-menu__subnav">
                                            <li class="m-menu__item  m-menu__item--parent" aria-haspopup="true"
                                                m-menu-link-redirect="1"><span class="m-menu__link"><span
                                                    class="m-menu__link-title">  <span
                                                    class="m-menu__link-wrap">      <span
                                                    class="m-menu__link-text">Support</span>      <span
                                                    class="m-menu__link-badge"><span
                                                    class="m-badge m-badge--accent">3</span></span>  </span></span></span>
                                            </li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><span
                                                    class="m-menu__link-text">Reports</span></a>
                                            </li>
                                            <li class="m-menu__item  m-menu__item--submenu" aria-haspopup="true"
                                                m-menu-submenu-toggle="hover" m-menu-link-redirect="1"><a
                                                    href="javascript:;"
                                                    class="m-menu__link m-menu__toggle"><span
                                                    class="m-menu__link-text">Cases</span><i
                                                    class="m-menu__ver-arrow la la-angle-right"></i></a>
                                                <div class="m-menu__submenu "><span class="m-menu__arrow"></span>
                                                    <ul class="m-menu__subnav">
                                                        <li class="m-menu__item " aria-haspopup="true"
                                                            m-menu-link-redirect="1">
                                                            <a href="inner.html" class="m-menu__link "><span
                                                                    class="m-menu__link-text">Pending</span></a></li>
                                                        <li class="m-menu__item " aria-haspopup="true"
                                                            m-menu-link-redirect="1">
                                                            <a href="inner.html" class="m-menu__link "><span
                                                                    class="m-menu__link-text">Urgent</span></a></li>
                                                        <li class="m-menu__item " aria-haspopup="true"
                                                            m-menu-link-redirect="1">
                                                            <a href="inner.html" class="m-menu__link "><span
                                                                    class="m-menu__link-text">Done</span></a></li>
                                                        <li class="m-menu__item " aria-haspopup="true"
                                                            m-menu-link-redirect="1">
                                                            <a href="inner.html" class="m-menu__link "><span
                                                                    class="m-menu__link-text">Archive</span></a></li>
                                                    </ul>
                                                </div>
                                            </li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><span
                                                    class="m-menu__link-text">Clients</span></a>
                                            </li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><span
                                                    class="m-menu__link-text">Audit</span></a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-light"></i><span class="m-menu__link-text">Administration</span></a>
                                </li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-share"></i><span
                                        class="m-menu__link-text">Management</span></a></li>
                                <li class="m-menu__section ">
                                    <h4 class="m-menu__section-text">Reports</h4>
                                    <i class="m-menu__section-icon flaticon-more-v3"></i>
                                </li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-graphic"></i><span class="m-menu__link-text">Accounting</span></a>
                                </li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-network"></i><span
                                        class="m-menu__link-text">Products</span></a></li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-network"></i><span
                                        class="m-menu__link-text">Sales</span></a></li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-alert"></i><span class="m-menu__link-title">  <span
                                        class="m-menu__link-wrap">      <span class="m-menu__link-text">Bills</span>      <span
                                        class="m-menu__link-badge"><span
                                        class="m-badge m-badge--danger">12</span></span>  </span></span></a></li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-technology"></i><span
                                        class="m-menu__link-text">IPO</span></a></li>
                                <li class="m-menu__section ">
                                    <h4 class="m-menu__section-text">System</h4>
                                    <i class="m-menu__section-icon flaticon-more-v3"></i>
                                </li>
                                <li class="m-menu__item  m-menu__item--submenu" aria-haspopup="true"
                                    m-menu-submenu-toggle="hover"><a href="javascript:;"
                                                                     class="m-menu__link m-menu__toggle"><i
                                        class="m-menu__link-icon flaticon-clipboard"></i><span
                                        class="m-menu__link-text">Applications</span><i
                                        class="m-menu__ver-arrow la la-angle-right"></i></a>
                                    <div class="m-menu__submenu "><span class="m-menu__arrow"></span>
                                        <ul class="m-menu__subnav">
                                            <li class="m-menu__item  m-menu__item--parent" aria-haspopup="true"><span
                                                    class="m-menu__link"><span
                                                    class="m-menu__link-text">Applications</span></span></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Audit</span></a></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Notifications</span></a></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Messages</span></a></li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="m-menu__item  m-menu__item--submenu" aria-haspopup="true"
                                    m-menu-submenu-toggle="hover"><a href="javascript:;"
                                                                     class="m-menu__link m-menu__toggle"><i
                                        class="m-menu__link-icon flaticon-computer"></i><span
                                        class="m-menu__link-text">Modules</span><i
                                        class="m-menu__ver-arrow la la-angle-right"></i></a>
                                    <div class="m-menu__submenu "><span class="m-menu__arrow"></span>
                                        <ul class="m-menu__subnav">
                                            <li class="m-menu__item  m-menu__item--parent" aria-haspopup="true"><span
                                                    class="m-menu__link"><span class="m-menu__link-text">Modules</span></span>
                                            </li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Logs</span></a></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Errors</span></a></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Configuration</span></a></li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-cogwheel"></i><span
                                        class="m-menu__link-text">Files</span></a></li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-lifebuoy"></i><span
                                        class="m-menu__link-text">Security</span></a></li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-settings"></i><span
                                        class="m-menu__link-text">Options</span></a></li>
                            </ul>
                        </div>
                        <!-- END: Aside Menu -->
                    </div><button class="m-aside-left-close  m-aside-left-close--skin-light " id="m_aside_left_close_btn"><i class="la la-close"></i></button>
                    <div id="m_aside_left" class="m-grid__item	m-aside-left  m-aside-left--skin-light w-100 h-100">
                        <!-- BEGIN: Aside Menu -->
                        <div id="m_ver_menu"
                             class="m-aside-menu  m-aside-menu--skin-light m-aside-menu--submenu-skin-light "
                             m-menu-vertical="1" m-menu-scrollable="0" m-menu-dropdown-timeout="500">
                            <ul class="m-menu__nav  m-menu__nav--dropdown-submenu-arrow ">
                                <li class="m-menu__section m-menu__section--first">
                                    <h4 class="m-menu__section-text">Departments</h4>
                                    <i class="m-menu__section-icon flaticon-more-v3"></i>
                                </li>
                                <li class="m-menu__item m-menu__item--submenu" aria-haspopup="true"
                                    m-menu-submenu-toggle="hover"><a href="javascript:;"
                                                                     class="m-menu__link m-menu__toggle"><i
                                        class="m-menu__link-icon flaticon-layers"></i><span
                                        class="m-menu__link-text">Resources</span><i
                                        class="m-menu__ver-arrow la la-angle-right"></i></a>
                                    <div class="m-menu__submenu "><span class="m-menu__arrow"></span>
                                        <ul class="m-menu__subnav">
                                            <li class="m-menu__item  m-menu__item--parent" aria-haspopup="true"><span
                                                    class="m-menu__link"><span
                                                    class="m-menu__link-text">Resources</span></span>
                                            </li>
                                            <li class="m-menu__item " aria-haspopup="true"><a href="inner.html"
                                                                                              class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Timesheet</span></a></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Payroll</span></a></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Contacts</span></a></li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-suitcase"></i><span
                                        class="m-menu__link-text">Finance</span></a></li>
                                <li class="m-menu__item m-menu__item--submenu" aria-haspopup="true"
                                    m-menu-submenu-toggle="hover" m-menu-link-redirect="1"><a href="javascript:;"
                                                                                              class="m-menu__link m-menu__toggle"><i
                                        class="m-menu__link-icon flaticon-graphic-1"></i><span
                                        class="m-menu__link-title">  <span class="m-menu__link-wrap">      <span
                                        class="m-menu__link-text">Support</span>      <span
                                        class="m-menu__link-badge"><span
                                        class="m-badge m-badge--accent">3</span></span>  </span></span><i
                                        class="m-menu__ver-arrow la la-angle-right"></i></a>
                                    <div class="m-menu__submenu "><span class="m-menu__arrow"></span>
                                        <ul class="m-menu__subnav">
                                            <li class="m-menu__item  m-menu__item--parent" aria-haspopup="true"
                                                m-menu-link-redirect="1"><span class="m-menu__link"><span
                                                    class="m-menu__link-title">  <span
                                                    class="m-menu__link-wrap">      <span
                                                    class="m-menu__link-text">Support</span>      <span
                                                    class="m-menu__link-badge"><span
                                                    class="m-badge m-badge--accent">3</span></span>  </span></span></span>
                                            </li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><span
                                                    class="m-menu__link-text">Reports</span></a>
                                            </li>
                                            <li class="m-menu__item  m-menu__item--submenu" aria-haspopup="true"
                                                m-menu-submenu-toggle="hover" m-menu-link-redirect="1"><a
                                                    href="javascript:;"
                                                    class="m-menu__link m-menu__toggle"><span
                                                    class="m-menu__link-text">Cases</span><i
                                                    class="m-menu__ver-arrow la la-angle-right"></i></a>
                                                <div class="m-menu__submenu "><span class="m-menu__arrow"></span>
                                                    <ul class="m-menu__subnav">
                                                        <li class="m-menu__item " aria-haspopup="true"
                                                            m-menu-link-redirect="1">
                                                            <a href="inner.html" class="m-menu__link "><span
                                                                    class="m-menu__link-text">Pending</span></a></li>
                                                        <li class="m-menu__item " aria-haspopup="true"
                                                            m-menu-link-redirect="1">
                                                            <a href="inner.html" class="m-menu__link "><span
                                                                    class="m-menu__link-text">Urgent</span></a></li>
                                                        <li class="m-menu__item " aria-haspopup="true"
                                                            m-menu-link-redirect="1">
                                                            <a href="inner.html" class="m-menu__link "><span
                                                                    class="m-menu__link-text">Done</span></a></li>
                                                        <li class="m-menu__item " aria-haspopup="true"
                                                            m-menu-link-redirect="1">
                                                            <a href="inner.html" class="m-menu__link "><span
                                                                    class="m-menu__link-text">Archive</span></a></li>
                                                    </ul>
                                                </div>
                                            </li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><span
                                                    class="m-menu__link-text">Clients</span></a>
                                            </li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><span
                                                    class="m-menu__link-text">Audit</span></a>
                                            </li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-light"></i><span class="m-menu__link-text">Administration</span></a>
                                </li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-share"></i><span
                                        class="m-menu__link-text">Management</span></a></li>
                                <li class="m-menu__section ">
                                    <h4 class="m-menu__section-text">Reports</h4>
                                    <i class="m-menu__section-icon flaticon-more-v3"></i>
                                </li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-graphic"></i><span class="m-menu__link-text">Accounting</span></a>
                                </li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-network"></i><span
                                        class="m-menu__link-text">Products</span></a></li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-network"></i><span
                                        class="m-menu__link-text">Sales</span></a></li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-alert"></i><span class="m-menu__link-title">  <span
                                        class="m-menu__link-wrap">      <span class="m-menu__link-text">Bills</span>      <span
                                        class="m-menu__link-badge"><span
                                        class="m-badge m-badge--danger">12</span></span>  </span></span></a></li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-technology"></i><span
                                        class="m-menu__link-text">IPO</span></a></li>
                                <li class="m-menu__section ">
                                    <h4 class="m-menu__section-text">System</h4>
                                    <i class="m-menu__section-icon flaticon-more-v3"></i>
                                </li>
                                <li class="m-menu__item  m-menu__item--submenu" aria-haspopup="true"
                                    m-menu-submenu-toggle="hover"><a href="javascript:;"
                                                                     class="m-menu__link m-menu__toggle"><i
                                        class="m-menu__link-icon flaticon-clipboard"></i><span
                                        class="m-menu__link-text">Applications</span><i
                                        class="m-menu__ver-arrow la la-angle-right"></i></a>
                                    <div class="m-menu__submenu "><span class="m-menu__arrow"></span>
                                        <ul class="m-menu__subnav">
                                            <li class="m-menu__item  m-menu__item--parent" aria-haspopup="true"><span
                                                    class="m-menu__link"><span
                                                    class="m-menu__link-text">Applications</span></span></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Audit</span></a></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Notifications</span></a></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Messages</span></a></li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="m-menu__item  m-menu__item--submenu" aria-haspopup="true"
                                    m-menu-submenu-toggle="hover"><a href="javascript:;"
                                                                     class="m-menu__link m-menu__toggle"><i
                                        class="m-menu__link-icon flaticon-computer"></i><span
                                        class="m-menu__link-text">Modules</span><i
                                        class="m-menu__ver-arrow la la-angle-right"></i></a>
                                    <div class="m-menu__submenu "><span class="m-menu__arrow"></span>
                                        <ul class="m-menu__subnav">
                                            <li class="m-menu__item  m-menu__item--parent" aria-haspopup="true"><span
                                                    class="m-menu__link"><span class="m-menu__link-text">Modules</span></span>
                                            </li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Logs</span></a></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Errors</span></a></li>
                                            <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                                    href="inner.html" class="m-menu__link "><i
                                                    class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                                    class="m-menu__link-text">Configuration</span></a></li>
                                        </ul>
                                    </div>
                                </li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-cogwheel"></i><span
                                        class="m-menu__link-text">Files</span></a></li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-lifebuoy"></i><span
                                        class="m-menu__link-text">Security</span></a></li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html"
                                        class="m-menu__link "><i
                                        class="m-menu__link-icon flaticon-settings"></i><span
                                        class="m-menu__link-text">Options</span></a></li>
                            </ul>
                        </div>
                        <!-- END: Aside Menu -->
                    </div>
             </div>`;
var search = `<form action=""><div class="inner-form"><div class="input-field"><input id="search" type="text" placeholder="Tìm kiếm khóa học ..." class="form-control"></div></div></form>`;
var class_box = `<div class="col-lg-4 p-0">
<div class="m-portlet m-portlet--bordered-semi m-portlet--full-height m-portlet--rounded-force p-3 mx-lg-2">
    <div class="course-item-pic-text">
        <div class="course-pic relative-position m--margin-bottom-25">
            <img src="{% static 'images/code.jpg' %}" alt="">
        </div>
        <div class="course-item-text">
            <div class="course-meta">
                <span class="course-category bold-font"><a href="#">CNTT</a></span>
                <span class="course-author bold-font"><a
                        href="#">Hoàng Xuân Tùng</a></span>
                <span class="mr-0"><p class="font-weight-bold">INT3306 4</p></span>
            </div>
            <div class="course-title m--padding-top-10 headline m--padding-bottom-15 relative-position">
                <h3>
                    Phát triển ứng dụng Web
                    <!--<span class="trend-badge text-uppercase bold-font"><i class="fas fa-bolt"></i> TRENDING</span>-->
                </h3>
                <a class="m--pull-right m--margin-bottom-20 mt-1"
                   href="/course/1"><em>Xem khóa học &nbsp; <i
                        class="fa fa-arrow-right"></i></em></a>
            </div>
            <div class="course-viewer ul-li d-inline-block">
                <ul>
                    <li><p class="m-0"><i class="fas fa-user"></i> 1.220</p></li>
                    <!--<li><p><i class="fas fa-comment-dots"></i> 1.015</p></li>-->
                    <li><p class="m-0">125k Unrolled</p></li>
                </ul>
            </div>
        </div>
    </div>
</div>
</div>`;
var new_class_modal = `<div class="modal fade" id="m_modal_4" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" style="display: none;" aria-hidden="true">
<div class="modal-dialog w-75" role="document">
    <div class="modal-content">
        <div class="m-portlet m-portlet--full-height">

<!--begin: Portlet Head-->
<div class="m-portlet__head">
    <div class="m-portlet__head-caption">
        <div class="m-portlet__head-title">
            <h3 class="m-portlet__head-text">
                Form Wizard
            </h3>
        </div>
    </div>
    <div class="m-portlet__head-tools">
        <ul class="m-portlet__nav">
            <li class="m-portlet__nav-item">
                <a href="#" data-toggle="m-tooltip" class="m-portlet__nav-link m-portlet__nav-link--icon" data-direction="left" data-width="auto" title="" data-original-title="Get help with filling up this form">
                    <i class="flaticon-info m--icon-font-size-lg3"></i>
                </a>
            </li>
        </ul>
    </div>
</div>

<!--end: Portlet Head-->

<!--begin: Portlet Body-->
<div class="m-portlet__body m-portlet__body--no-padding">

    <!--begin: Form Wizard-->
    <div class="m-wizard m-wizard--3 m-wizard--success m-wizard--step-first" id="m_wizard">

        <!--begin: Message container -->
        <div class="m-portlet__padding-x">

            <!-- Here you can put a message or alert -->
        </div>

        <!--end: Message container -->
        <div class="row m-row--no-padding">
            <div class="col-xl-3 col-lg-12">

                <!--begin: Form Wizard Head -->
                <div class="m-wizard__head">

                    <!--begin: Form Wizard Progress -->
                    <div class="m-wizard__progress">
                        <div class="progress">
                            <div class="progress-bar" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 25%;"></div>
                        </div>
                    </div>

                    <!--end: Form Wizard Progress -->

                    <!--begin: Form Wizard Nav -->
                    <div class="m-wizard__nav">
                        <div class="m-wizard__steps">
                            <div class="m-wizard__step m-wizard__step--current" m-wizard-target="m_wizard_form_step_1">
                                <div class="m-wizard__step-info">
                                    <a href="#" class="m-wizard__step-number">
                                        <span>
                                            <span>1</span>
                                        </span>
                                    </a>
                                    <div class="m-wizard__step-line">
                                        <span></span>
                                    </div>
                                    <div class="m-wizard__step-label">
                                        Thông tin cơ bảm
                                    </div>
                                </div>
                            </div>
                            <div class="m-wizard__step" m-wizard-target="m_wizard_form_step_2">
                                <div class="m-wizard__step-info">
                                    <a href="#" class="m-wizard__step-number">
                                        <span>
                                            <span>2</span>
                                        </span>
                                    </a>
                                    <div class="m-wizard__step-line">
                                        <span></span>
                                    </div>
                                    <div class="m-wizard__step-label">
                                        Lịch học
                                    </div>
                                </div>
                            </div>
                            <div class="m-wizard__step" m-wizard-target="m_wizard_form_step_3">
                                <div class="m-wizard__step-info">
                                    <a href="#" class="m-wizard__step-number">
                                        <span>
                                            <span>3</span>
                                        </span>
                                    </a>
                                    <div class="m-wizard__step-line">
                                        <span></span>
                                    </div>
                                    <div class="m-wizard__step-label">
                                        Giáo trình
                                    </div>
                                </div>
                            </div>
                            <div class="m-wizard__step" m-wizard-target="m_wizard_form_step_4">
                                <div class="m-wizard__step-info">
                                    <a href="#" class="m-wizard__step-number">
                                        <span>
                                            <span>4</span>
                                        </span>
                                    </a>
                                    <div class="m-wizard__step-line">
                                        <span></span>
                                    </div>
                                    <div class="m-wizard__step-label">
                                        Xác nhận
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!--end: Form Wizard Nav -->
                </div>

                <!--end: Form Wizard Head -->
            </div>
            <div class="col-xl-9 col-lg-12">

                <!--begin: Form Wizard Form-->
                <div class="m-wizard__form">

                    <!--
1) Use m-form--label-align-left class to alight the form input lables to the right
2) Use m-form--state class to highlight input control borders on form validation
-->
                    <form class="m-form m-form--label-align-left- m-form--state-" id="m_form" novalidate="novalidate">

                        <!--begin: Form Body -->
                        <div class="m-portlet__body m-portlet__body--no-padding">

                            <!--begin: Form Wizard Step 1-->
                            <div class="m-wizard__form-step m-wizard__form-step--current" id="m_wizard_form_step_1">
                                <div class="m-form__section m-form__section--first">
                                    <div class="m-form__heading">
                                        <h3 class="m-form__heading-title">Thông tin cơ bản của lớp học mới</h3>
                                    </div>
                                    <div class="form-group m-form__group row">
                                        <label class="col-xl-3 col-lg-3 col-form-label">Loại lớp học: </label>
                                        <div class="col-xl-9 col-lg-9">
                                            <select name="country" class="form-control m-input">
                                                <option value="">Toán</option>
                                                <option value="AF">CNTT</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="form-group m-form__group row">
                                        <label class="col-xl-3 col-lg-3 col-form-label">Môn học: </label>
                                        <div class="col-xl-9 col-lg-9">
                                            <select name="country" class="form-control m-input">
                                                <option value="">Phát triển ƯD Web </option>
                                                <option value="AF">An Toàn an ninh mạng</option>
                                            </select>
                                        </div>
                                    </div>
                                  
                                    <div class="form-group m-form__group row">
                                        <label class="col-xl-3 col-lg-3 col-form-label">Tên lớp :</label>
                                        <div class="col-xl-9 col-lg-9">
                                            <input type="text" name="name" class="form-control m-input" placeholder="" value="Nick Stone">
                                            <span class="m-form__help">Điền Tên</span>
                                        </div>
                                    </div>
                                    <div class="form-group m-form__group row">
                                        <label class="col-xl-3 col-lg-3 col-form-label">Mã lớp: </label>
                                        <div class="col-xl-9 col-lg-9">
                                            <input type="email" name="email" class="form-control m-input" placeholder="" value="nick.stone@gmail.com">
                                            <span class="m-form__help">Mã lớp </span>
                                        </div>
                                    </div>
                                    <div class="form-group m-form__group row">
                                        <label class="col-xl-3 col-lg-3 col-form-label">Mô tả lớp học</label>
                                        <div class="col-xl-9 col-lg-9">
                                            <textarea name="description" class="form-control m-input" placeholder="" value="1-541-754-3010"></textarea>
                                            <span class="m-form__help">Enter your valid phone in US phone format. E.g: 1-541-754-3010</span>
                                        </div>
                                    </div>
                                </div>
                                
                            </div>

                            <!--end: Form Wizard Step 1-->

                            <!--begin: Form Wizard Step 2-->
                            <div class="m-wizard__form-step" id="m_wizard_form_step_2">
                                <div class="m-form__section m-form__section--first">
                                    <div class="m-form__heading">
                                        <h3 class="m-form__heading-title">Account Details</h3>
                                    </div>
                                    <div class="form-group m-form__group row">
                                        <div class="col-lg-12">
                                            <label class="form-control-label">* URL:</label>
                                            <input type="url" name="account_url" class="form-control m-input" placeholder="" value="http://sinortech.vertoffice.com">
                                            <span class="m-form__help">Please enter your preferred URL to your dashboard</span>
                                        </div>
                                    </div>
                                    <div class="form-group m-form__group row">
                                        <div class="col-lg-6 m-form__group-sub">
                                            <label class="form-control-label">* Username:</label>
                                            <input type="text" name="account_username" class="form-control m-input" placeholder="" value="nick.stone">
                                            <span class="m-form__help">Your username to login to your dashboard</span>
                                        </div>
                                        <div class="col-lg-6 m-form__group-sub">
                                            <label class="form-control-label">* Password:</label>
                                            <input type="password" name="account_password" class="form-control m-input" placeholder="" value="qwerty">
                                            <span class="m-form__help">Please use letters and at least one number and symbol</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="m-separator m-separator--dashed m-separator--lg"></div>
                                <div class="m-form__section">
                                    <div class="m-form__heading">
                                        <h3 class="m-form__heading-title">Client Settings</h3>
                                    </div>
                                    <div class="form-group m-form__group row">
                                        <div class="col-lg-6 m-form__group-sub">
                                            <label class="form-control-label">* User Group:</label>
                                            <div class="m-radio-inline">
                                                <label class="m-radio m-radio--solid m-radio--brand">
                                                    <input type="radio" name="account_group" checked="" value="2"> Sales Person
                                                    <span></span>
                                                </label>
                                                <label class="m-radio m-radio--solid m-radio--brand">
                                                    <input type="radio" name="account_group" value="2"> Customer
                                                    <span></span>
                                                </label>
                                            </div>
                                            <span class="m-form__help">Please select user group</span>
                                        </div>
                                        <div class="col-lg-6 m-form__group-sub">
                                            <label class="form-control-label">* Communications:</label>
                                            <div class="m-checkbox-inline">
                                                <label class="m-checkbox m-checkbox--solid m-checkbox--brand">
                                                    <input type="checkbox" name="account_communication[]" checked="" value="email"> Email
                                                    <span></span>
                                                </label>
                                                <label class="m-checkbox m-checkbox--solid  m-checkbox--brand">
                                                    <input type="checkbox" name="account_communication[]" value="sms"> SMS
                                                    <span></span>
                                                </label>
                                                <label class="m-checkbox m-checkbox--solid  m-checkbox--brand">
                                                    <input type="checkbox" name="account_communication[]" value="phone"> Phone
                                                    <span></span>
                                                </label>
                                            </div>
                                            <span class="m-form__help">Please select user communication options</span>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!--end: Form Wizard Step 2-->

                            <!--begin: Form Wizard Step 3-->
                            <div class="m-wizard__form-step" id="m_wizard_form_step_3">
                                <div class="m-form__section m-form__section--first">
                                    <div class="m-form__heading">
                                        <h3 class="m-form__heading-title">Billing Information</h3>
                                    </div>
                                    <div class="form-group m-form__group row">
                                        <div class="col-lg-12">
                                            <label class="form-control-label">* Cardholder Name:</label>
                                            <input type="text" name="billing_card_name" class="form-control m-input" placeholder="" value="Nick Stone">
                                        </div>
                                    </div>
                                    <div class="form-group m-form__group row">
                                        <div class="col-lg-12">
                                            <label class="form-control-label">* Card Number:</label>
                                            <input type="text" name="billing_card_number" class="form-control m-input" placeholder="" value="372955886840581">
                                        </div>
                                    </div>
                                    <div class="form-group m-form__group row">
                                        <div class="col-lg-4 m-form__group-sub">
                                            <label class="form-control-label">* Exp Month:</label>
                                            <select class="form-control m-input" name="billing_card_exp_month">
                                                <option value="">Select</option>
                                                <option value="01">01</option>
                                                <option value="02">02</option>
                                                <option value="03">03</option>
                                                <option value="04" selected="">04</option>
                                                <option value="05">05</option>
                                                <option value="06">06</option>
                                                <option value="07">07</option>
                                                <option value="08">08</option>
                                                <option value="09">09</option>
                                                <option value="10">10</option>
                                                <option value="11">11</option>
                                                <option value="12">12</option>
                                            </select>
                                        </div>
                                        <div class="col-lg-4 m-form__group-sub">
                                            <label class="form-control-label">* Exp Year:</label>
                                            <select class="form-control m-input" name="billing_card_exp_year">
                                                <option value="">Select</option>
                                                <option value="2018">2018</option>
                                                <option value="2019">2019</option>
                                                <option value="2020">2020</option>
                                                <option value="2021" selected="">2021</option>
                                                <option value="2022">2022</option>
                                                <option value="2023">2023</option>
                                                <option value="2024">2024</option>
                                            </select>
                                        </div>
                                        <div class="col-lg-4 m-form__group-sub">
                                            <label class="form-control-label">* CVV:</label>
                                            <input type="number" class="form-control m-input" name="billing_card_cvv" placeholder="" value="450">
                                        </div>
                                    </div>
                                </div>
                                <div class="m-separator m-separator--dashed m-separator--lg"></div>
                                <div class="m-form__section">
                                    <div class="m-form__heading">
                                        <h3 class="m-form__heading-title">Billing Address
                                            <i data-toggle="m-tooltip" data-width="auto" class="m-form__heading-help-icon flaticon-info" title="" data-original-title="If different than the corresponding address"></i>
                                        </h3>
                                    </div>
                                    <div class="form-group m-form__group row">
                                        <div class="col-lg-12">
                                            <label class="form-control-label">* Address 1:</label>
                                            <input type="text" name="billing_address_1" class="form-control m-input" placeholder="" value="Headquarters 1120 N Street Sacramento 916-654-5266">
                                        </div>
                                    </div>
                                    <div class="form-group m-form__group row">
                                        <div class="col-lg-12">
                                            <label class="form-control-label">Address 2:</label>
                                            <input type="text" name="billing_address_2" class="form-control m-input" placeholder="" value="P.O. Box 942873 Sacramento, CA 94273-0001">
                                        </div>
                                    </div>
                                    <div class="form-group m-form__group row">
                                        <div class="col-lg-5 m-form__group-sub">
                                            <label class="form-control-label">* City:</label>
                                            <input type="text" class="form-control m-input" name="billing_city" placeholder="" value="Polo Alto">
                                        </div>
                                        <div class="col-lg-5 m-form__group-sub">
                                            <label class="form-control-label">* State:</label>
                                            <input type="text" class="form-control m-input" name="billing_state" placeholder="" value="California">
                                        </div>
                                        <div class="col-lg-2 m-form__group-sub">
                                            <label class="form-control-label">* ZIP:</label>
                                            <input type="text" class="form-control m-input" name="billing_zip" placeholder="" value="34890">
                                        </div>
                                    </div>
                                </div>
                                <div class="m-separator m-separator--dashed m-separator--lg"></div>
                                <div class="m-form__section">
                                    <div class="m-form__heading">
                                        <h3 class="m-form__heading-title">Delivery Type</h3>
                                    </div>
                                    <div class="form-group m-form__group">
                                        <div class="row">
                                            <div class="col-lg-6">
                                                <label class="m-option">
                                                    <span class="m-option__control">
                                                        <span class="m-radio m-radio--state-brand">
                                                            <input type="radio" name="billing_delivery" value="">
                                                            <span></span>
                                                        </span>
                                                    </span>
                                                    <span class="m-option__label">
                                                        <span class="m-option__head">
                                                            <span class="m-option__title">
                                                                Standart Delevery
                                                            </span>
                                                            <span class="m-option__focus">
                                                                Free
                                                            </span>
                                                        </span>
                                                        <span class="m-option__body">
                                                            Estimated 14-20 Day Shipping (&nbsp;Duties end taxes may be due upon delivery&nbsp;)
                                                        </span>
                                                    </span>
                                                </label>
                                            </div>
                                            <div class="col-lg-6">
                                                <label class="m-option">
                                                    <span class="m-option__control">
                                                        <span class="m-radio m-radio--state-brand">
                                                            <input type="radio" name="billing_delivery" value="">
                                                            <span></span>
                                                        </span>
                                                    </span>
                                                    <span class="m-option__label">
                                                        <span class="m-option__head">
                                                            <span class="m-option__title">
                                                                Fast Delevery
                                                            </span>
                                                            <span class="m-option__focus">
                                                                $&nbsp;8.00
                                                            </span>
                                                        </span>
                                                        <span class="m-option__body">
                                                            Estimated 2-5 Day Shipping (&nbsp;Duties end taxes may be due upon delivery&nbsp;)
                                                        </span>
                                                    </span>
                                                </label>
                                            </div>
                                        </div>
                                        <div class="m-form__help">

                                            <!--must use this helper element to display error message for the options-->
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!--end: Form Wizard Step 3-->

                            <!--begin: Form Wizard Step 4-->
                            <div class="m-wizard__form-step" id="m_wizard_form_step_4">

                                <!--begin::Section-->
                                <div class="m-accordion m-accordion--default" id="m_accordion_1" role="tablist">

                                    <!--begin::Item-->
                                    <div class="m-accordion__item active">
                                        <div class="m-accordion__item-head" role="tab" id="m_accordion_1_item_1_head" data-toggle="collapse" href="#m_accordion_1_item_1_body" aria-expanded="  false">
                                            <span class="m-accordion__item-icon">
                                                <i class="fa flaticon-user-ok"></i>
                                            </span>
                                            <span class="m-accordion__item-title">1. Client Information</span>
                                            <span class="m-accordion__item-mode"></span>
                                        </div>
                                        <div class="m-accordion__item-body collapse show" id="m_accordion_1_item_1_body" role="tabpanel" aria-labelledby="m_accordion_1_item_1_head" data-parent="#m_accordion_1">

                                            <!--begin::Content-->
                                            <div class="tab-content active  m--padding-30">
                                                <div class="m-form__section m-form__section--first">
                                                    <div class="m-form__heading">
                                                        <h4 class="m-form__heading-title">Client Details</h4>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Name:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">Nick Stone</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Email:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">nick.stone@gmail.com</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Phone</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">+206-78-55034890</span>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="m-separator m-separator--dashed m-separator--lg"></div>
                                                <div class="m-form__section">
                                                    <div class="m-form__heading">
                                                        <h4 class="m-form__heading-title">Corresponding Address
                                                            <i data-toggle="m-tooltip" class="m-form__heading-help-icon flaticon-info" title="" data-original-title="Some help text goes here"></i>
                                                        </h4>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Address Line 1:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">Headquarters 1120 N Street Sacramento 916-654-5266</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Address Line 2:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">P.O. Box 942873 Sacramento, CA 94273-0001</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">City:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">Polo Alto</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">State:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">California</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Country:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">USA</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>

                                            <!--end::Section-->
                                        </div>
                                    </div>

                                    <!--end::Item-->

                                    <!--begin::Item-->
                                    <div class="m-accordion__item">
                                        <div class="m-accordion__item-head collapsed" role="tab" id="m_accordion_1_item_2_head" data-toggle="collapse" href="#m_accordion_1_item_2_body" aria-expanded="    false">
                                            <span class="m-accordion__item-icon">
                                                <i class="fa  flaticon-placeholder"></i>
                                            </span>
                                            <span class="m-accordion__item-title">2. Account Setup</span>
                                            <span class="m-accordion__item-mode"></span>
                                        </div>
                                        <div class="m-accordion__item-body collapse" id="m_accordion_1_item_2_body" role="tabpanel" aria-labelledby="m_accordion_1_item_2_head" data-parent="#m_accordion_1">

                                            <!--begin::Content-->
                                            <div class="tab-content  m--padding-30">
                                                <div class="m-form__section m-form__section--first">
                                                    <div class="m-form__heading">
                                                        <h4 class="m-form__heading-title">Account Details</h4>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">URL:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">sinortech.vertoffice.com</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Username:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">sinortech.admin</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Password:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">*********</span>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="m-separator m-separator--dashed m-separator--lg"></div>
                                                <div class="m-form__section">
                                                    <div class="m-form__heading">
                                                        <h4 class="m-form__heading-title">Client Settings</h4>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">User Group:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">Customer</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Communications:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">Phone, Email</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>

                                            <!--end::Content-->
                                        </div>
                                    </div>

                                    <!--end::Item-->

                                    <!--begin::Item-->
                                    <div class="m-accordion__item">
                                        <div class="m-accordion__item-head collapsed" role="tab" id="m_accordion_1_item_3_head" data-toggle="collapse" href="#m_accordion_1_item_3_body" aria-expanded="    false">
                                            <span class="m-accordion__item-icon">
                                                <i class="fa  flaticon-placeholder"></i>
                                            </span>
                                            <span class="m-accordion__item-title">3. Billing Setup</span>
                                            <span class="m-accordion__item-mode"></span>
                                        </div>
                                        <div class="m-accordion__item-body collapse" id="m_accordion_1_item_3_body" role="tabpanel" aria-labelledby="m_accordion_1_item_3_head" data-parent="#m_accordion_1">

                                            <!--begin::Content-->
                                            <div class="tab-content  m--padding-30">
                                                <div class="m-form__section m-form__section--first">
                                                    <div class="m-form__heading">
                                                        <h4 class="m-form__heading-title">Billing Information</h4>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Cardholder Name:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">Nick Stone</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Card Number:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">*************4589</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Exp Month:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">10</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Exp Year:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">2018</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">CVV:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">***</span>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="m-separator m-separator--dashed m-separator--lg"></div>
                                                <div class="m-form__section">
                                                    <div class="m-form__heading">
                                                        <h4 class="m-form__heading-title">Billing Address</h4>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Address Line 1:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">Headquarters 1120 N Street Sacramento 916-654-5266</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Address Line 2:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">P.O. Box 942873 Sacramento, CA 94273-0001</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">City:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">Polo Alto</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">State:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">California</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">ZIP:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">37505</span>
                                                        </div>
                                                    </div>
                                                    <div class="form-group m-form__group m-form__group--sm row">
                                                        <label class="col-xl-4 col-lg-4 col-form-label">Country:</label>
                                                        <div class="col-xl-8 col-lg-8">
                                                            <span class="m-form__control-static">USA</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>

                                            <!--end::Content-->
                                        </div>
                                    </div>

                                    <!--end::Item-->
                                </div>

                                <!--end::Section-->

                                <!--end::Section-->
                                <div class="m-separator m-separator--dashed m-separator--lg"></div>
                                <div class="form-group m-form__group m-form__group--sm row">
                                    <div class="col-xl-12">
                                        <div class="m-checkbox-inline">
                                            <label class="m-checkbox m-checkbox--solid m-checkbox--brand">
                                                <input type="checkbox" name="accept" value="1"> Click here to indicate that you have read and agree to the terms presented in the Terms and Conditions agreement
                                                <span></span>
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!--end: Form Wizard Step 4-->
                        </div>

                        <!--end: Form Body -->

                        <!--begin: Form Actions -->
                        <div class="m-portlet__foot m-portlet__foot--fit m--margin-top-40">
                            <div class="m-form__actions">
                                <div class="row">
                                    <div class="col-lg-6 m--align-left">
                                        <a href="#" class="btn btn-secondary m-btn m-btn--custom m-btn--icon" data-wizard-action="prev">
                                            <span>
                                                <i class="la la-arrow-left"></i>&nbsp;&nbsp;
                                                <span>Back</span>
                                            </span>
                                        </a>
                                    </div>
                                    <div class="col-lg-6 m--align-right">
                                        <a href="#" class="btn btn-primary m-btn m-btn--custom m-btn--icon" data-wizard-action="submit">
                                            <span>
                                                <i class="la la-check"></i>&nbsp;&nbsp;
                                                <span>Submit</span>
                                            </span>
                                        </a>
                                        <a href="#" class="btn btn-success m-btn m-btn--custom m-btn--icon" data-wizard-action="next">
                                            <span>
                                                <span>Save &amp; Continue</span>&nbsp;&nbsp;
                                                <i class="la la-arrow-right"></i>
                                            </span>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!--end: Form Actions -->
                    </form>
                </div>

                <!--end: Form Wizard Form-->
            </div>
        </div>
    </div>

    <!--end: Form Wizard-->
</div>

<!--end: Portlet Body-->
</div>
    </div>
</div>
</div>`;
var new_class_btn = `<button type="button" class="btn btn-warning" data-toggle="modal" data-target="#m_modal_4">Launch Modal</button>`;


// var mLayout = function () {
//     var t, e, a, n = function () {
//         0 !== $("#m_aside_left_hide_toggle").length && (n = new mToggle("m_aside_left_hide_toggle", {
//             target: "body",
//             targetState: "m-aside-left--hide",
//             togglerState: "m-brand__toggler--active"
//         })).on("toggle", function (e) {
//             t.pauseDropdownHover(800), Cookies.set("sidebar_hide_state", e.getState())
//         })
//     };
//     return {
//         init: function () {
//             this.initHeader(), this.initAside()
//         },
//         initHeader: function () {
//             var t, e, a;
//             e = mUtil.get("m_header"), a = {
//                 offset: {},
//                 minimize: {}
//             }, "hide" == mUtil.attr(e, "m-minimize-mobile") ? (a.minimize.mobile = {}, a.minimize.mobile.on = "m-header--hide", a.minimize.mobile.off = "m-header--show") : a.minimize.mobile = !1, "hide" == mUtil.attr(e, "m-minimize") ? (a.minimize.desktop = {}, a.minimize.desktop.on = "m-header--hide", a.minimize.desktop.off = "m-header--show") : a.minimize.desktop = !1, (t = mUtil.attr(e, "m-minimize-offset")) && (a.offset.desktop = t), (t = mUtil.attr(e, "m-minimize-mobile-offset")) && (a.offset.mobile = t), new mHeader("m_header", a), $("#m_aside_header_topbar_mobile_toggle").click(function () {
//                 $("body").toggleClass("m-topbar--on")
//             }), 0 !== $("#m_quicksearch").length && new mQuicksearch("m_quicksearch", {
//                 mode: mUtil.attr("m_quicksearch", "m-quicksearch-mode"),
//                 minLength: 1
//             }).on("search", function (t) {
//                 t.showProgress(), $.ajax({
//                     url: "https://keenthemes.com/metronic/preview/inc/api/quick_search.php",
//                     data: {
//                         query: t.query
//                     },
//                     dataType: "html",
//                     success: function (e) {
//                         t.hideProgress(), t.showResult(e)
//                     },
//                     error: function (e) {
//                         t.hideProgress(), t.showError("Connection error. Pleae try again later.")
//                     }
//                 })
//             }), new mScrollTop("m_scroll_top", {
//                 offset: 300,
//                 speed: 600
//             })
//         },
//         initAside: function () {
//             var o, i, l, r, s, d, c, m;
//             l = mUtil.get("body"), r = mUtil.get("m_aside_left"), s = mUtil.hasClass(r, "m-aside-left--offcanvas-default") ? "m-aside-left--offcanvas-default" : "m-aside-left", e = new mOffcanvas("m_aside_left", {
//                 baseClass: s,
//                 overlay: !0,
//                 closeBy: "m_aside_left_close_btn",
//                 toggleBy: {
//                     target: "m_aside_left_offcanvas_toggle",
//                     state: "m-brand__toggler--active"
//                 }
//             }), mUtil.hasClass(l, "m-aside-left--fixed") && (mUtil.addEvent(r, "mouseenter", function () {
//                 i && (clearTimeout(i), i = null), o = setTimeout(function () {
//                     mUtil.hasClass(l, "m-aside-left--minimize") && mUtil.isInResponsiveRange("desktop") && (mUtil.removeClass(l, "m-aside-left--minimize"), mUtil.addClass(l, "m-aside-left--minimize-hover"), t.scrollerUpdate(), t.scrollerTop())
//                 }, 300)
//             }), mUtil.addEvent(r, "mouseleave", function () {
//                 o && (clearTimeout(o), o = null), i = setTimeout(function () {
//                     mUtil.hasClass(l, "m-aside-left--minimize-hover") && mUtil.isInResponsiveRange("desktop") && (mUtil.removeClass(l, "m-aside-left--minimize-hover"), mUtil.addClass(l, "m-aside-left--minimize"), t.scrollerUpdate(), t.scrollerTop())
//                 }, 500)
//             })), c = mUtil.get("m_ver_menu"), m = "1" === mUtil.attr(c, "m-menu-dropdown") ? "dropdown" : "accordion", "1" === mUtil.attr(c, "m-menu-scrollable") && (d = {
//                 height: function () {
//                     return mUtil.getViewPort().height - parseInt(mUtil.css("m_header", "height")) - 60
//                 }
//             }), t = new mMenu("m_ver_menu", {
//                 scroll: d,
//                 submenu: {
//                     desktop: {
//                         default: m,
//                         state: {
//                             body: "m-aside-left--minimize",
//                             mode: "dropdown"
//                         }
//                     },
//                     tablet: "accordion",
//                     mobile: "accordion"
//                 },
//                 accordion: {
//                     autoScroll: !1,
//                     expandAll: !1
//                 }
//             }), 0 !== $("#m_aside_left_minimize_toggle").length && (a = new mToggle("m_aside_left_minimize_toggle", {
//                 target: "body",
//                 targetState: "m-brand--minimize m-aside-left--minimize",
//                 togglerState: "m-brand__toggler--active"
//             })).on("toggle", function (e) {
//                 horMenu.pauseDropdownHover(800), t.pauseDropdownHover(800), Cookies.set("sidebar_toggle_state", e.getState())
//             }), n(), this.onLeftSidebarToggle(function (t) {
//                 var e = $(".m-datatable");
//                 $(e).each(function () {
//                     $(this).mDatatable("redraw")
//                 })
//             })
//         },
//         getAsideMenu: function () {
//             return t
//         },
//         onLeftSidebarToggle: function (t) {
//             a && a.on("toggle", t)
//         },
//         closeMobileAsideMenuOffcanvas: function () {
//             mUtil.isMobileDevice() && e.hide()
//         }
//     }
// }();
// $(document).ready(function () {
//     !1 === mUtil.isAngularVersion() && mLayout.init()
// });