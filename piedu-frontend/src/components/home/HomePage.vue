<template>
    <div id="homepage">
        <hero></hero>
        <introduce></introduce>
        <system-statistic></system-statistic>
        <course-category></course-category>
        <random-class></random-class>
        <tutorial></tutorial>
        <faq-link></faq-link>
        <contact-link></contact-link>
    </div>
</template>
<script>
    import Hero from './Hero.vue'
    import Introduce from './Introduce.vue'
    import SystemStatistic from './SystemStatistic.vue'
    import CourseCategory from './CourseCategory.vue'
    import RandomClass from  './RandomClass.vue'
    import Tutorial from  './Tutorial.vue'
    import FAQLink from './FAQLink.vue'
    import ContactLink from './ContactLink.vue'

    export default {
        name: 'homepage',
        components: {
            'hero': Hero,
            'introduce':Introduce,
            'system-statistic': SystemStatistic,
            'course-category': CourseCategory,
            'random-class': RandomClass,
            'tutorial': Tutorial,
            'faq-link': FAQLink,
            'contact-link': ContactLink
        }
    }
</script>
