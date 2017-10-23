var app  = new Vue({
    el: "#siteContent",
    data:{
        params:{
            page: 1,
            pageCount: 1,
            base_site: '',
            area: '',
            siteClass: '',
            hasPhone: 0,
            hasIM: 0,
            hasLink: 0,
        },
        siteList: [],
        shopCart:[],
        toggle:false,

    },
    created:function(){
        axios.get('/api/v1/getsite/').then(res=>{
            this.siteList = res.data.resData;
            this.params.page = res.data.page;
            this.params.pageCount = res.data.pageCount;
            this.addCheckState();
        })
    },
    methods:{
        checkSite:function(event, site){
            if(event.target.checked){
                this.getCheckedSite();
            }else{
                this.removeCheckSite(site);
            };
        },
        addCheckState:function(){
            this.siteList.map((item)=>{item.check = false;})
        },
        getCheckedSite:function(){
            let checkedList = this.siteList.filter(item => { return item.check});
            this.shopCart = _.union(this.shopCart, checkedList);
        },
        removeCheckSite:function(site){
            let temp_list = this.shopCart;
            let index = _.findIndex(temp_list, 'id', site.id);
            this.shopCart.splice(index, 1);
            let index_l = _.findIndex(this.siteList, 'id', site.id);
            if(index_l >= 0 && this.siteList[index_l].check){
                this.siteList[index_l].check = false;
            }
        },
        getSiteList:function(){
            let req_url = '/api/v1/getsite/'+ this.getParam();
            axios.get( req_url).then(res=>{
                this.siteList = res.data.resData;
                this.params.page = res.data.page;
                this.params.pageCount = res.data.pageCount;
                this.addCheckState();
            });
        },
        getParam:function(){
            let param_str =  '?page=' + this.params.page;
            if (this.params.base_site != ''){
                param_str = param_str + '&base_site=' + this.params.base_site;
            }
            if (this.params.siteClass != ''){
                param_str = param_str + '&siteClass=' + this.params.siteClas;
            }
            if (this.params.area != ''){
                param_str = param_str + '&siteClass=' + this.params.area;
            }
            if (this.params.hasPhone){
                param_str = param_str + '&hasPhone=' + 'true';
            }
            if (this.params.hasIM){
                param_str = param_str + '&hasIM=' + 'true';
            }
            if (this.params.hasLink){
                param_str = param_str + '&hasLink=' + 'true';
            }
            return param_str;
        },
        chgPage: function(page){
            if(this.params.page !== page){
                this.params.page = page;
            }
            this.params.page = 10;
        },
        postCheckSite:function(){
            let id_list = [];
            this.shopCart.forEach(item=>{
                id_list.push(item.id);
            })
            if(id_list.length == 0){
                alert("请选择要投放的网站");
                return false;
            }
            data = {site_list: id_list};
            console.log(data);
            let post_url = "/api/v1/getsite/";
            axios.post(post_url, data).then(res =>{
                if(retCode == 1){
                    window.location.href="/shop/order/" + res.data;
                }else{
                    alert("服务器错误，请稍后再试");
                }
            }).catch(error=>{
                console.log(error);
            })
        }
    },
    computed:{
        shopCount: function(){
            return this.shopCart.length;
        },
        priceCount: function(){
           let count = 0;
           this.shopCart.forEach(item =>{
                count = count + item.price;
           })
           return count;
        }
    },
    watch: {
        'params': {
            handler(newParams, oldParams){
                console.log(JSON.stringify(newParams));
                this.getSiteList();
            },
            deep:true
        }
    }
});

//var app2 = new Vue({
//    el:"#shopCart",
//    data:""
//})
document.getElementById("postSite").addEventListener("click", function(){
    app.postCheckSite();
})
Vue.component('star', {
    template: "<i  v-once class='text-yellow fa fa-star'></i>",
});

Vue.component("shopCart", {
    template:``,
})