(function(){
  const key="theme", root=document.documentElement, btn=document.getElementById("themeToggle");
  function set(mode){root.setAttribute("data-theme",mode); localStorage.setItem(key,mode);}
  const saved=localStorage.getItem(key); if(saved) set(saved);
  btn && btn.addEventListener("click", ()=> set(root.getAttribute("data-theme")==="light"?"dark":"light"));
})();
