const Counter = {
    data() {
      return {
        counter: 0
      }
    },
    mounted() {
      setInterval(() => {
        this.counter++
      }, 1000)
    },
    delimiters: ['[[', ']]'] 
}

const AttributeBinding = {
    data() {
        return {
            message:"You loaded this page on " + new Date().toLocaleString()
        }
    }
}

const EventHandling = {
    data(){
        return {
            message : 'Hello Vue.js',
            text : 'これはテストテキストです',
        }
    },
    methods:{
        reverseMessage() {
            this.message = this.message
                .split('')
                .reverse()
                .join('')
            this.text = this.text
                .split('')
                .reverse()
                .join('')
        }
    },
    delimiters:['[[', ']]']
}

const TwoWayBinding ={
    data() {
        return{
            message : "Hello Vue!"
        }
    },
    delimiters:['[[', ']]'],
}

const ConditionalRendring = {
    data(){
        return {
            seen : true
        }
    },
    methods:{
        replace(){
            if (this.seen == true){
                this.seen = false
            } else {
                this.seen = true
            }
        }
    },
    delimiters: ["[[", "]]"],
}