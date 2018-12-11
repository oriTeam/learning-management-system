<template>
    <ul class="timeline">
        <li class="timeline-item">
            <div class="timeline-badge ">1</div>
            <div class="timeline-panel">
                <div class="timeline-heading">
                    <h4 class="timeline-title">Admin added a comment.</h4>
                    <div class="timeline-panel-controls">
                        <div class="controls">
                            <button class="btn btn-sm btn-link"><i class="fas fa-edit"></i> Chỉnh sửa</button>
                            <button class="btn btn-sm btn-link"><i class="fas fa-trash-alt"></i> Xóa</button>
                        </div>
                        <div class="timestamp">
                            <small class="text-muted">24. Sep 17:03</small>
                        </div>
                    </div>
                </div>
                <div class="timeline-body"><p><i>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Totam, maxime
                    alias nam dignissimos natus voluptate iure deleniti. Doloremque, perspiciatis voluptas dignissimos
                    ex, ullam et, reprehenderit similique possimus iste commodi minima fugiat non culpa, veniam
                    temporibus laborum. Distinctio ipsam cupiditate debitis aliquid deleniti consectetur voluptates
                    corporis officiis tempora minus veniam, accusamus cum optio nesciunt illo nulla odio? Quidem
                    nesciunt, omnis at quo aliquam porro amet fugit mollitia minus explicabo, possimus deserunt rem ut
                    commodi laboriosam quia. Numquam, est facilis rem iste voluptatum. Cupiditate porro fuga saepe quis
                    nulla mollitia, magni dicta soluta distinctio tempore voluptate quo perferendis. Maiores eveniet
                    deleniti, nemo.</i></p></div>
            </div>

        </li>
    </ul>
</template>

<script>

</script>
<style lang="scss">
    .timeline {
        list-style: none;
        padding: 20px 0 20px;
        position: relative;

        &:before {
            background-color: #eee;
            bottom: 0;
            content: " ";
            left: 50px;
            margin-left: -1.5px;
            position: absolute;
            top: 0;
            width: 3px;
        }

        > li {
            margin-bottom: 20px;
            position: relative;

            &:before,
            &:after {
                content: " ";
                display: table;
            }

            &:after {
                clear: both;
            }

            > .timeline-panel {
                border-radius: 2px;
                border: 1px solid #d4d4d4;
                box-shadow: 0 1px 2px rgba(100, 100, 100, 0.2);
                margin-left: 100px;
                padding: 20px;
                position: relative;

                .timeline-heading {
                    .timeline-panel-controls {
                        position: absolute;
                        right: 8px;
                        top: 5px;

                        .timestamp {
                            display: inline-block;
                        }

                        .controls {
                            display: inline-block;
                            padding-right: 5px;
                            border-right: 1px solid #aaa;

                            a {
                                color: #999;
                                font-size: 11px;
                                padding: 0 5px;

                                &:hover {
                                    color: #333;
                                    text-decoration: none;
                                    cursor: pointer;
                                }
                            }
                        }

                        .controls + .timestamp {
                            padding-left: 5px;
                        }
                    }
                }
            }

            .timeline-badge {
                background-color: #999;
                border-radius: 50%;
                color: #fff;
                font-size: 1.4em;
                height: 50px;
                left: 50px;
                line-height: 52px;
                margin-left: -25px;
                position: absolute;
                text-align: center;
                top: 16px;
                width: 50px;
                z-index: 100;
            }

            .timeline-badge + .timeline-panel {
                &:before {
                    border-bottom: 15px solid transparent;
                    border-left: 0 solid #ccc;
                    border-right: 15px solid #ccc;
                    border-top: 15px solid transparent;
                    content: " ";
                    display: inline-block;
                    position: absolute;
                    left: -15px;
                    right: auto;
                    top: 26px;
                }

                &:after {
                    border-bottom: 14px solid transparent;
                    border-left: 0 solid #fff;
                    border-right: 14px solid #fff;
                    border-top: 14px solid transparent;
                    content: " ";
                    display: inline-block;
                    position: absolute;
                    left: -14px;
                    right: auto;
                    top: 27px;
                }
            }
        }
    }

    .timeline-badge {
        &.primary {
            background-color: #2e6da4 !important;
        }

        &.success {
            background-color: #3f903f !important;
        }

        &.warning {
            background-color: #f0ad4e !important;
        }

        &.danger {
            background-color: #d9534f !important;
        }

        &.info {
            background-color: #5bc0de !important;
        }
    }

    .timeline-title {
        margin-top: 0;
        color: inherit;
    }

    .timeline-body {
        > p,
        > ul {
            margin-bottom: 0;
        }

        > p + p {
            margin-top: 5px;
        }
    }
</style>