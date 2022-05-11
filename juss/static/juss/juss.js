/**
 * filter
 */
document.querySelectorAll("select.juss-filter-select").forEach(item => {
  item.onchange = (e) => {
    let href = item.selectedOptions[0].dataset.href;
    window.location.href = href;
  }
})

/**
 * form tabs
 */
var fieldsets = document.querySelectorAll("form > div > fieldset, .inline-group fieldset:not(.aligned)");
if(fieldsets.length > 1) {
  //var html = "<ul class=\"juss-tabs\">";
  var root = document.createElement('div');
  root.classList.add('tabs');
  root.classList.add('is-boxed');
  var ul = document.createElement("ul");
  ul.classList.add("juss-tabs");
  fieldsets.forEach((item, index) => {
    item.classList.remove("collapse");
    var title = item.querySelector("h2");
    //title.classList.add('is-hidden');
    title = title ? title.innerHTML : "基础信息";
    var li = document.createElement("li");
    var a = document.createElement('a');
    a.setAttribute('href', '#tab'+index);
    a.innerHTML = title;
    li.setAttribute("onclick", "changeTab(this, "+index+")");
    li.append(a);
    ul.appendChild(li);
  });
  root.appendChild(ul);
  document.getElementById("content-main").insertBefore(root, document.querySelector(".object-tools"));
  document.getElementById("content-main").insertAdjacentElement("afterbegin", root);
  document.querySelector(".juss-tabs li:first-child").classList.add("is-active");

  fieldsets[0].style.display = "block";
    Array.from(fieldsets).slice(1).map(item => item.style.display = "none");

}

const changeTab = (e, index) => {
  fieldsets.forEach((item,i) => {
    if(i == index) {
      item.style.display = "block";
    } else {
      item.style.display = "none";
    }
  });
  if(!e.classList.contains("is-active")) {
    document.querySelector(".tabs .is-active").classList.remove("is-active");
    e.classList.add("is-active");
  }


    document.querySelectorAll(".selector-chosen").forEach(i => {
	i.querySelector("select").style.height = "268px";
    })    
};


/**
 * left toggle
 */
// var toggle = Cookies.get('left-toggle');
// if(toggle) {
//   django.jQuery("#left-box").hide();
//   django.jQuery("#header2").addClass("header_fullwidth");
//   django.jQuery("#left_toggle_x").hide();
//   django.jQuery("#left_toggle_menu").show();
// } else {
//   django.jQuery("#left_toggle_x").show();
//   django.jQuery("#left_toggle_menu").hide();
// }
// django.jQuery("#left_toggle").on("click", function(e) {
//   e.preventDefault();
//   if(django.jQuery("#header2").hasClass("header_fullwidth")) {
//     Cookies.remove('left-toggle');
//     django.jQuery("#left-box").show();
//     django.jQuery("#left_toggle_x").show();
//     django.jQuery("#left_toggle_menu").hide();
//     django.jQuery("#header2").removeClass("header_fullwidth");
//   } else {
//     Cookies.set('left-toggle', 'true');
//     django.jQuery("#left-box").hide();
//     django.jQuery("#left_toggle_x").hide();
//     django.jQuery("#left_toggle_menu").show();
//     django.jQuery("#header2").addClass("header_fullwidth");
//   }
// });

/**
 * actions toggle all
 */
// if(document.getElementById("action-toggle")) {
//   document.getElementById("action-toggle").remove();
//   var input = document.createElement("input");
//   input.setAttribute("type", "checkbox");
//   input.setAttribute("id", "action-toggle");
//   //input.style.display = "none";
//   var label = document.createElement("label");
//   label.setAttribute("for", "action-toggle");
//   label.innerHTML = "全选";
//   label.style.marginRight = ".5rem";
//   label.style.marginLeft = ".25rem";
//   var actions = document.querySelector("#changelist-form .actions");
//   actions.insertBefore(input, actions.childNodes[0]);
//   actions.insertBefore(label, actions.childNodes[1]);
// }

/**
 * add label for input checkbox
 */
// document.querySelectorAll("input[type='checkbox']").forEach((row, index) => {
//   var label = document.createElement("label");
//   var id = null;
//   if(!row.nextSibling) {
//     id = row.getAttribute("id");
//     if(!id) {
//       id = `auto_checkbox_${index}`
//     }
//     row.setAttribute("id", id);
//     label.setAttribute("for", id);
//     row.parentNode.appendChild(label);
//   }
// })

// /** dashboard module **/
// function setWaterfall() {
//   let maxwidth = document.getElementById("content-main").clientWidth
//   let y = 0;
//   let x = 0;
//   let column = 1
//   if(maxwidth <= 768) {
//     column = 1
//   } else if (maxwidth <= 1024) {
//     column = 3
//   } else {
//     column = 4
//   }
//   let width = maxwidth / column
//   let cols = new Array(column).fill(y)
//   document.querySelectorAll(".dashboard #content-main .module").forEach(row => {
//     row.style.position = "absolute"
//     row.style.width = width + 'px'
//     y = Math.min.apply(null, cols)
//     x = cols.indexOf(y)
//     row.style.top = y + 'px'
//     row.style.left = width * x + 'px'
//     cols[x] += row.clientHeight
//   })
//   document.getElementById("content-main").style.height = Math.max.apply(null, cols) + 'px';
// }

// if(document.querySelector(".dashboard")) {
//   setWaterfall();
//   window.onresize = function(){
//     setWaterfall();
//   }
// }



/** 提醒删除 **/
document.querySelectorAll(".notification .delete").forEach(item => {
  item.addEventListener("click", () => {
    item.parentElement.remove();
  });
});
