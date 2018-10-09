var tag_model = {
	worldcup:{
		name: "World Cup 2018",
		title: "Tin tức mới nhất về World Cup 2018",
		tag: "#wc",
	},
	argentina:{
		name: "Đội tuyển Argentina",
		title: "Đội tuyển Argentina",
		tag: "#arg",
	},
	germany:{
		name: "Đội tuyển Đức",
		title: "Đội tuyển Đức",
		tag: "#ger",
	},
	france:{
		name: "Đội tuyển Pháp",
		title: "đội tuyển Pháp",
		tag: "#fra",
	},
	brazil:{
		name: "Đội tuyển Brazil",
		title: "Đội tuyển Brazil",
		tag: "#brz",
	},
	england:{
		name: "Đội tuyển Anh",
		title: "Đội tuyển Anh",
		tag: "#eng",
	},
	korea: {
		name: "Đội tuyển Hàn Quốc",
		title: "đội tuyển Hàn Quốc",
		tag: "#kor",
	},
	japan: {
		name: "Đội tuyển Nhật Bản",
		title: "Đội tuyển Nhật Bản",
		tag: "#jp",
	},
	nigeria: {
		name: "Đội tuyển Nigeria",
		title: "Đội tuyển Nigeria",
		tag: "#nir",
	},
	egypt: {
		name: "Đội tuyển Ai Cập",
		title: "Đội tuyển Ai Cập",
		tag: "#egy",
	},
	mexico: {
		name: "Đội tuyển Mexico",
		title: "Đội tuyển Mexico",
		tag: "#mex",
	},
	australia: {
		name: "Đội tuyển Úc",
		title: "Đội tuyển Úc",
		tag: "#aus",
	}
};
var new_model = {
	new1:{
		img_src: "https://image-service.onefootball.com/resize?fit=max&image=http%3A%2F%2Fimages.performgroup.com%2Fdi%2Flibrary%2Fomnisport%2Fe6%2F94%2Fdries-mertens_fxsf3n2f8xst1ecsugqthn6t7.jpg%3Ft%3D327134404&q=25&w=1080",
		alt: "",
		text: "Trận đấu Anh - Tunisia phải đối mặt với những 'vị khách lạ' trên sân",
		tag : ["#wc", "#arg", "#fra", "#brz"],
		show: true,
		key: "n1",
	},
	new2:{
		img_src: "https://image-service.onefootball.com/resize?fit=max&image=http%3A%2F%2Fimages.performgroup.com%2Fdi%2Flibrary%2Fomnisport%2Fa2%2F22%2Fdriesmertens-cropped_2fs88ngh894w19zocvt31salg.jpg%3Ft%3D162850340&q=25&w=1080",
		alt: "",
		text: "ĐT Anh: Hệ thống tốt nhưng con người dở thì đừng mơ World Cup",
		tag : ["#wc", "#aus", "#eng", "#brz"],
		show: true,
		key: "n2",
	},
	new3:{
		img_src: "https://image-service.onefootball.com/resize?fit=max&image=https%3A%2F%2Fen.onefootball.com%2Fwp-content%2Fuploads%2Fsites%2F10%2F2018%2F06%2FFBL-WC-2018-ENG-PRESSER-1529304424-e1529304469430.jpg&q=75&w=1080",
		alt: "",
		text: "Radamel Falcao - Con hổ ma mãnh trong cơn đói World Cup",
		tag : ["#wc", "#aus", "#arg"],
		show : true,
		key: "n3",
	},
	new4:{
		img_src: "https://en.onefootball.com/wp-content/uploads/sites/10/2018/06/FBL-WC-2018-TUN-TRAINING-1529303256-1-e1529303288856.jpg",
		alt: "Ramos nhái lại pha ngã kiếm penalty của Ronaldo",
		text: "Ramos nhái lại pha ngã kiếm penalty của Ronaldo",
		tag : ["#fra","#eng","#wc"],
		show: true,
		key: "n4",
	},
	new5:{
		img_src: "https://en.onefootball.com/wp-content/uploads/sites/10/2018/06/FBL-WC-2018-BEL-TRAINING-1529303997-1-e1529304034964.jpg",
		alt: "'Tôi cần vé' và những cổ động viên xem World Cup từ ngoài hàng rào",
		text: "'Tôi cần vé' và những cổ động viên xem World Cup từ ngoài hàng rào",
		tag : ["#brz","#wc", "#arg", "#eng"],
		show: true,
		key: "n5",
	},
	new6:{
		img_src: "https://en.onefootball.com/wp-content/uploads/sites/10/2018/06/FBL-WC-2018-SWE-PRESSER-1529304097-1-e1529304132290.jpg",
		alt: "Khám phá ga tàu điện ngầm Moscow mùa World Cup",
		text: "Khám phá ga tàu điện ngầm Moscow mùa World Cup",
		tag : ["#wc","#eng", "#fra","#brz"],
		show: true,
		key: "n6",
	},
	new7:{
		img_src: "https://image-service.onefootball.com/resize?fit=max&image=http%3A%2F%2Fimages.performgroup.com%2Fdi%2Flibrary%2Fomnisport%2Fef%2F38%2Fharrykane-cropped_1gq8e87yaulos1u7437rqjvwk2.jpg%3Ft%3D233166404&q=25&w=1080",
		alt: "Evra: Chớ có dại mà nhận lời qua nhà Ronaldo chơi",
		text: "Evra: Chớ có dại mà nhận lời qua nhà Ronaldo chơi",
		tag : ["#aus","#wc", "#ger", "#fra"],
		show: true,
		key: "n7",
	},
	new8:{
		img_src: "https://image-service.onefootball.com/resize?fit=max&image=http%3A%2F%2Fimages.performgroup.com%2Fdi%2Flibrary%2Fomnisport%2Ffa%2F9f%2Fkane-cropped_yozioqceooib1a7pr5k2emzyn.jpg%3Ft%3D212230276&q=25&w=1080",
		alt: "Vì sao trọng tài không dùng VAR cho Hàn Quốc hưởng phạt đền?",
		text: "Vì sao trọng tài không dùng VAR cho Hàn Quốc hưởng phạt đền?",
		tag : ["#fra","#arg","#egy","#nir"],
		show: true,
		key: "n8",
	},
	new9:{
		img_src: "https://image-service.onefootball.com/resize?fit=max&image=http%3A%2F%2Fimages.performgroup.com%2Fdi%2Flibrary%2Fomnisport%2Fd1%2Ff4%2Fhazard-cropped_ohd77yeg3wwj1k4qpa975mp1b.jpg%3Ft%3D307794852&q=25&w=1080",
		alt: "VAR có thực sự đem đến công bằng?",
		text: "VAR có thực sự đem đến công bằng?",
		tag : ["#nir","#egy","#ger", "#arg"],
		show: true,
		key: "n9",
	},
	new10:{
		img_src: "https://image-service.onefootball.com/resize?fit=max&image=https%3A%2F%2Fen.onefootball.com%2Fwp-content%2Fuploads%2Fsites%2F10%2F2018%2F06%2FFBL-ITA-SERIE-A-TORINO-LAZIO-1529227012-e1529227052872.jpg&q=75&w=1080",
		alt: "Antoine Griezmann - Hoàng tử bé thắp ánh sáng cho Les Bleus",
		text: "Antoine Griezmann - Hoàng tử bé thắp ánh sáng cho Les Bleus",
		tag : ["#eng", "#jp", "#egy", "#nir"],
		show: true,
		key: "n10",
	},
	new11:{
		img_src: "https://image-service.onefootball.com/resize?fit=max&image=https%3A%2F%2Fen.onefootball.com%2Fwp-content%2Fuploads%2Fsites%2F10%2F2018%2F06%2FFBL-WC-2018-BRA-PRESSER-1529136617-e1529136659985.jpg&q=75&w=1080",
		alt: "Sadio Mane, kẻ lang thang vì giấc mơ World Cup",
		text: "Sadio Mane, kẻ lang thang vì giấc mơ World Cup",
		tag : ["#nir","#jp", "#egy", "#kor", "#nir"],
		show: true,
		key: "n11",
	},
	new12:{
		img_src: "https://image-service.onefootball.com/resize?fit=max&image=https%3A%2F%2Fen.onefootball.com%2Fwp-content%2Fuploads%2Fsites%2F10%2F2018%2F06%2FReal-Madrid-v-Liverpool-UEFA-Champions-League-Final-1529147609-e1529147643545.jpg&q=75&w=1080",
		alt: "Sergio Ramos - Gã côn đồ sân cỏ và huyền thoại bất tử",
		text: "Sergio Ramos - Gã côn đồ sân cỏ và huyền thoại bất tử",
		tag : ["#arg", "#jp", "#kor", "#mex"],
		show: true,
		key: "n12",
	},
	new13:{
		img_src: "https://image-service.onefootball.com/resize?fit=max&image=http%3A%2F%2Fimages.performgroup.com%2Fdi%2Flibrary%2Fomnisport%2Fe0%2Ffa%2Fisco-cropped_jq7rnwu3f9zdzzoby0850pu8.jpg%3Ft%3D316550276&q=25&w=1080",
		alt: "Giá trị thương hiệu của Neymar đã vượt Messi và Ronaldo",
		text: "Giá trị thương hiệu của Neymar đã vượt Messi và Ronaldo",
		tag : ["#nir","#kor", "#jp", "#mex"],
		show: true,
		key: "n13",
	},
	new14:{
		img_src: "https://image-service.onefootball.com/resize?fit=max&image=http%3A%2F%2Fimages.performgroup.com%2Fdi%2Flibrary%2Fomnisport%2Fbe%2F9f%2Fronaldopique-cropped_elw0nqu2duln1etuvurg2t84t.jpg%3Ft%3D91274468&q=25&w=1080",
		alt: "Từ chối ra sân, tiền đạo Croatia trước nguy cơ bị đuổi về nước",
		text: "Từ chối ra sân, tiền đạo Croatia trước nguy cơ bị đuổi về nước",
		tag : ["#mex","#jp", "#kor", "#ger"],
		show: true,
		key: "n14",
	},
	new15:{
		img_src: "https://image-service.onefootball.com/resize?fit=max&image=http%3A%2F%2Fimages.performgroup.com%2Fdi%2Flibrary%2Fomnisport%2F90%2Fcb%2Fpiquegriezmann-cropped_g7tmstrh0o6j169q0ox1ihwhv.jpg%3Ft%3D100972852&q=25&w=1080",
		alt: "Griezmann trở thành cầu thủ đầu tiên ghi bàn nhờ công nghệ VAR",
		text: "Griezmann trở thành cầu thủ đầu tiên ghi bàn nhờ công nghệ VAR",
		tag : ["#mex", "#jp", "#kor"],
		show : true,
		key: "n15",
	},
	new16:{
		img_src: "https://image-service.onefootball.com/resize?fit=max&image=http%3A%2F%2Fimages.performgroup.com%2Fdi%2Flibrary%2Fomnisport%2F8c%2Fee%2Fantoinegriezmann-cropped_urfviv6betix12u84444rdpac.jpg%3Ft%3D238823852&q=25&w=1080",
		alt: "ĐT Nhật Bản đón 'viện binh' từ Arsenal trước trận ra quân",
		text: "ĐT Nhật Bản đón 'viện binh' từ Arsenal trước trận ra quân",
		tag : ["#mex", "#arg", "#ger"],
		show : true,
		key: "n16",
	},
	new17:{
		img_src: "https://en.onefootball.com/wp-content/uploads/sites/10/2018/06/FBL-FRIENDLY-KSA-PER-1529134308-1-e1529134343376.jpg",
		alt: "World Cup ngày 19/6: Ramos chế nhạo Ronaldo",
		text: "World Cup ngày 19/6: Ramos chế nhạo Ronaldo",
		tag : ["#aus","#wc","#ger"],
		show : true,
		key: "n17",
	},
	
};
var results = {
	yesterday: {
		day : "19-06-2018",
		match: [
			"Hàn Quốc 0 - 1 Đan Mạch",
			"Bỉ 3 - 0 Panama",
		],
	},
	today: {
		day : "20-06-2018",
		match: [
			"Anh 0 - 0 Pháp",
			"Đức 22:00 Brazil",
		]
	}
}
var filter = true;
Vue.options.delimiters = ['[[', ']]'];
var trendingTag = new Vue({
	el: "#trending-tag",
	data: {
		tags : tag_model,
	},
	methods: {
		selectTag: function(event){
			var allButton =  document.getElementsByClassName('tag-btn');
			for (btn in allButton){
				if(allButton.hasOwnProperty(btn)){
					allButton[btn].style.background ="#fff";
				}
			}
			event.target.style.background = "#6ae66a"; 
			// news.tag = event.currentTarget.getAttribute('tag');
			var currentTag = event.currentTarget.getAttribute('tag');
			// alert(currentTag);
			var fnews = news.lastestNews;
			for (key in fnews){
				if(!fnews[key].tag.includes(currentTag)){
					fnews[key].show = false;
				}
				else fnews[key].show = true;
			}

		},
	}
});

var news = new Vue({
	el: "#news",
	data: {
		lastestNews: new_model,
		tag: "#wc",

	},
	
})
var rs = new Vue({
	el: "#result",
	data: {
		results: results,
	},
})





















var model = {
	person: {
		orion: {
			name: "Orion",
			gender: "Male",
			age: 20,
			message: "I am a Vietnam boy",
		},
		hunter: {
			name: "Hunter",
			gender: "Male",
			age: 20,
			message: "Do you know me?",
		},
		andromeda: {
			name: "Andromeda",
			gender: "Female",
			age: 20,
			message: "I am beautiful",
		},
		gemini: {
			name: "Gemini",
			gender: "Male",
			age: 20,
			message: "Both is handsome",
		},
		aquarius: {
			name: "Aquarius",
			gender: "Male",
			age: 20,
			message: "I am so kute",
		},
		aries: {
			name: "Aries",
			gender: "Female",
			age: 20,
			message: "Hello, I am Aries"
		},
		vantrong291: {
			name: "Van Trong",
			gender: "Male",
			age: 20,
			message: "VN(*",
		}

	},
	work: {

	}
} 
// console.log(model);
// var vm = new Vue({
// 	el: '#app',
// 	// data : {
// 	// 	message: "Mean?",
// 	// }
// 	data: model,
// 	created: function(){
// 		alert("Created");
// 	},
// 	mounted: function(){
// 		alert("Mounted");
// 	},
// 	updated: function(){
// 		alert("Updated");
// 	},
// 	destroyed: function(){
// 		alert("Destroyed");
// 	},
// 	computed: {
// 		fullName: function() {
// 			var persons = this.person;
// 			console.log(persons['vantrong291']);
// 			var allName = "";
// 			for (person in persons){
// 				allName += person.name + " ";
// 			}
// 			return allName;
// 		},
// 		now: function () {
//    			return Date.now()
//   		}
// 	}
// })

// new Vue({
//   el: '#demo',
//   data: {
//     show: true
//   }
// })

// // setTimeout(function() {
// // 	vm.$destroy();
// // }, 5000);