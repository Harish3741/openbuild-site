(()=>{
  // A new page starts at the top, at once. The artifact viewer otherwise carries the last page's scroll position over, so a card clicked halfway down
  // home would open the next page halfway down. Smooth scrolling is held back (html.ready) until the page has settled, or that reset would glide up from the bottom.
  const root=document.documentElement,still=matchMedia('(prefers-reduced-motion:reduce)').matches;
  if(!location.hash){
    try{history.scrollRestoration='manual';}catch{}
    const top=()=>scrollTo({top:0,left:0,behavior:'instant'});
    let guard=true;
    const settle=()=>{guard=false;root.classList.add('ready');};
    top();addEventListener('load',top,{once:true});addEventListener('pageshow',top,{once:true});
    // Until the visitor touches the page, any scroll is the viewer restoring the old position: undo it
    addEventListener('scroll',()=>{if(guard&&scrollY)top();},{passive:true});
    for(const t of ['wheel','touchstart','keydown','pointerdown'])addEventListener(t,settle,{once:true,passive:true});
    setTimeout(settle,1500);
  }else root.classList.add('ready');
  // The same page whatever its address: /, /index.html and /index are one page, as are /societies and /societies.html
  const page=p=>p.replace(/\.html$/,'').replace(/\/index$/,'/');
  // On the live site the address bar stays clean: open-build.org/, /societies or /partners, with no index.html, .html or #section
  // (old links like /index.html#past still land on their section first)
  if(/(^|\.)open-build\.org$|github\.io$/.test(location.hostname)){
    const clean=()=>{const p=page(location.pathname);if(p!==location.pathname||location.hash)history.replaceState(history.state,'',p+location.search);};
    location.hash?addEventListener('load',clean,{once:true}):clean();
  }
  // Leaving for another page: fade out and go to the top first, so the position carried over is the top
  document.addEventListener('click',e=>{
    const a=e.target.closest('a[href]');
    if(!a||e.defaultPrevented||e.button||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||a.target)return;
    const u=new URL(a.href,location.href);
    if(u.origin!==location.origin)return;
    // A link within this page scrolls there without writing #section into the address bar
    if(page(u.pathname)===page(location.pathname)){
      e.preventDefault();
      const t=u.hash.length>1&&document.getElementById(u.hash.slice(1));
      t&&t.id!=='top'?t.scrollIntoView():scrollTo({top:0});
      return;
    }
    e.preventDefault();root.classList.add('leaving');
    setTimeout(()=>{root.classList.remove('ready');scrollTo({top:0,left:0,behavior:'instant'});location.href=u.href;},still?0:170);
  });
  addEventListener('pageshow',()=>root.classList.remove('leaving'));

  const h=document.getElementById('top');
  const onScroll=()=>h.classList.toggle('scrolled',scrollY>8);
  addEventListener('scroll',onScroll,{passive:true});onScroll();


  // Stages reveal once on scroll-in, and everything inside a stage starts together.
  // A stage already scrolled past (a fast scroll or a nav jump) shows at once rather than waiting to be scrolled back to.
  const io=new IntersectionObserver(es=>{for(const e of es)if(e.isIntersecting||e.boundingClientRect.bottom<0){
    const st=e.target;[st,...st.querySelectorAll('[data-reveal],.timeline')].forEach(el=>el.classList.add('in'));st.querySelector('.timeline')?.handovers?.();io.unobserve(st);
  }},{rootMargin:'0px 0px -15% 0px'});
  document.querySelectorAll('[data-stage]').forEach(el=>io.observe(el));
  // Photo cards are the one exception: each comes in on its own, and cards that scroll in together follow one another
  const cardIO=new IntersectionObserver(es=>{let k=0;for(const e of es)if(e.isIntersecting||e.boundingClientRect.bottom<0){
    e.target.style.animationDelay=k++*.3+'s';e.target.classList.add('in');cardIO.unobserve(e.target);
  }},{rootMargin:'0px 0px -15% 0px'});
  document.querySelectorAll('.shots>li').forEach(li=>cardIO.observe(li));

  // The committee timeline (partners page only)
  const tl=document.querySelector('.timeline');
  if(tl){
  // Size the timeline cover to the boxes (labels and years stay visible)
  const cover=tl.querySelector('.tl-cover');
  const fit=()=>{
    const t=tl.getBoundingClientRect(),a=tl.querySelector('.seg').getBoundingClientRect(),z=tl.querySelector('.bar').getBoundingClientRect();
    Object.assign(cover.style,{left:a.left-t.left-2+'px',top:a.top-t.top-8+'px',width:z.right-a.left+4+'px',height:z.bottom-a.top+16+'px'});
  };
  // Box outlines: rounded outer ends, zigzag on any side next to another box of the same row
  const draw=()=>{
    const A=6,N=4,R=6,p=.5;
    tl.querySelectorAll('.tl-row:not(.tl-ob)').forEach(row=>{
      const segs=[...row.querySelectorAll('.seg')];
      segs.forEach((seg,i)=>{
        const w=seg.offsetWidth,h=seg.offsetHeight,L=i>0,Rt=i<segs.length-1,y=k=>(p+k*(h-2*p)/N).toFixed(2);
        // right side: even points out, odd in; left side is the same zigzag shifted in by A, so neighbours read as one torn line
        const rx=k=>k%2?w-p-A:w-p, lx=k=>k%2?p:p+A;
        let d=L?`M${lx(0)} ${y(0)}`:`M${p} ${p+R}Q${p} ${p} ${p+R} ${p}`;
        d+=Rt?`L${rx(0)} ${y(0)}`:`L${w-p-R} ${p}Q${w-p} ${p} ${w-p} ${p+R}`;
        if(Rt)for(let k=1;k<=N;k++)d+=`L${rx(k)} ${y(k)}`;else d+=`L${w-p} ${h-p-R}Q${w-p} ${h-p} ${w-p-R} ${h-p}`;
        d+=L?`L${lx(N)} ${y(N)}`:`L${p+R} ${h-p}Q${p} ${h-p} ${p} ${h-p-R}`;
        if(L)for(let k=N-1;k>=0;k--)d+=`L${lx(k)} ${y(k)}`;
        seg.innerHTML=`<svg aria-hidden="true" viewBox="0 0 ${w} ${h}"><path d="${d}Z"/></svg>`;
      });
    });
  };
  const layout=()=>{fit();draw();};
  layout();new ResizeObserver(layout).observe(tl);

  // As the sweep reaches each break, the committee boxes either side of it jolt; the Open Build bar just glides on.
  // The sweep runs --sweep on --ease-sweep (0.65,0,0.35,1), so invert that curve to find when the edge reaches each break.
  const sweepTime=f=>{
    const B=(t,p1,p2)=>3*p1*t*(1-t)**2+3*p2*t*t*(1-t)+t**3;
    let lo=0,hi=1;for(let i=0;i<32;i++){const m=(lo+hi)/2;B(m,0,1)<f?lo=m:hi=m;}
    return B(lo,.65,.35)*parseFloat(getComputedStyle(tl).getPropertyValue('--sweep'))*1000;
  };
  const jolt=[{transform:'none'},{transform:'translateX(-5px) rotate(-1.4deg)'},{transform:'translateX(5px) rotate(1.1deg)'},{transform:'translateX(-4px) rotate(-.7deg)'},{transform:'translateX(3px) rotate(.4deg)'},{transform:'translateX(-1px)'},{transform:'none'}];
  tl.handovers=()=>{
    if(matchMedia('(prefers-reduced-motion:reduce)').matches)return;
    const c=cover.getBoundingClientRect();
    tl.querySelectorAll('.tl-row:not(.tl-ob)').forEach(row=>{
      const segs=[...row.querySelectorAll('.seg')];
      for(let i=1;i<segs.length;i++){
        const at=sweepTime((segs[i].getBoundingClientRect().left-c.left)/c.width);
        for(const el of [segs[i-1],segs[i]])el.animate(jolt,{duration:800,delay:at,easing:'ease-out'});
      }
    });
  };

  }

  // Walking through the door (home only). Scrolling the hero swings the door fully open and pours its light down onto the Next up card.
  const hero=document.querySelector('.hero');
  if(hero){
  const doorway=hero.querySelector('.doorway'),frame=doorway.querySelector('.frame'),leaf=frame.querySelector('.leaf');
  const floor=hero.querySelector('.floor'),card=hero.querySelector('.next'),beam=hero.querySelector('.beam'),ray=beam.firstElementChild;
  const motionOK=matchMedia('(prefers-reduced-motion:no-preference)').matches;
  let range=300,prog=motionOK?0:1,cur=64,tgt=64,v=0,raf=0,live=false;
  const step=()=>{v=v*.78+(tgt-cur)*.06;cur+=v;leaf.style.transform='perspective(900px) rotateY('+cur.toFixed(2)+'deg)';raf=Math.abs(tgt-cur)>.02||Math.abs(v)>.02?requestAnimationFrame(step):0;};
  const aim=()=>{if(!live)return;tgt=64+23*prog;if(!raf)raf=requestAnimationFrame(step);};
  const through=()=>{
    if(motionOK)prog=Math.min(1,Math.max(0,scrollY/range));
    ray.style.setProperty('--p',prog.toFixed(3));card.style.setProperty('--lit',prog.toFixed(3));aim();
  };
  // The beam runs from the doorway's opening down to the card, widening as it goes (offsets, so the card's own entrance doesn't move it)
  const fitBeam=()=>{
    const fl=doorway.offsetLeft+frame.offsetLeft+frame.clientLeft,fr=fl+frame.clientWidth,top=floor.offsetTop+floor.offsetHeight,bot=card.offsetTop+2;
    const cx=(fl+fr)/2,half=(fr-fl)*1.2,bl=Math.max(card.offsetLeft+20,cx-half),br=Math.min(card.offsetLeft+card.offsetWidth-20,cx+half);
    const x0=Math.min(fl,bl),w=Math.max(fr,br)-x0;
    Object.assign(beam.style,{left:x0+'px',top:top+'px',width:w+'px',height:bot-top+'px',clipPath:`polygon(${fl-x0}px 0,${fr-x0}px 0,${br-x0}px 100%,${bl-x0}px 100%)`});
    range=Math.max(180,hero.getBoundingClientRect().top+scrollY+card.offsetTop-innerHeight*.55);
    through();
  };
  fitBeam();new ResizeObserver(fitBeam).observe(hero);addEventListener('scroll',through,{passive:true});
  if(motionOK)leaf.addEventListener('animationend',()=>{live=true;aim();},{once:true});

  }

  // Logo carousels (societies, partner rows): repeat each row until half of it covers the widest screen, so the loop has no seam.
  // About 4s of travel per card.
  for(const socs of document.querySelectorAll('.socs')){
    const set=[...socs.children],n=set.length;
    const w=set[n-1].getBoundingClientRect().right-set[0].getBoundingClientRect().left;
    const m=Math.max(1,Math.ceil(Math.max(innerWidth,screen.width)/w));
    for(let k=1;k<2*m;k++)for(const li of set){const c=li.cloneNode(true);c.setAttribute('aria-hidden','true');for(const a of c.querySelectorAll('a'))a.tabIndex=-1;socs.append(c);}
    socs.style.setProperty('--loop',n*m*4+'s');
    socs.parentElement.classList.add('loop');
  }

  // Who we are (home only): one person at the front of the stack. The names, the arrows, a swipe and the arrow keys all move it.
  // It also steps on by itself while in view, until the visitor moves it once.
  const stack=document.querySelector('.stack');
  if(stack){
    const faces=[...stack.children],names=[...document.querySelectorAll('.people button')],n=faces.length;
    const who=document.querySelector('.team-who'),nav=document.querySelector('.team-nav'),count=nav.querySelector('.mono');
    let at=0,timer=0;
    const go=(i,byHand)=>{
      at=(i+n)%n;
      faces.forEach((f,k)=>{const pos=(k-at+n)%n;f.dataset.pos=pos<3?pos:9;});
      names.forEach((b,k)=>b.setAttribute('aria-pressed',k===at));
      who.innerHTML=names[at].innerHTML;count.textContent=at+1+' / '+n;
      if(byHand){clearInterval(timer);timer=-1;}
    };
    nav.hidden=false;
    names.forEach((b,k)=>b.addEventListener('click',()=>go(k,true)));
    nav.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>go(at+ +b.dataset.step,true)));
    document.getElementById('team').addEventListener('keydown',e=>{const d={ArrowLeft:-1,ArrowRight:1}[e.key];if(d){go(at+d,true);names[at].closest('.people').contains(document.activeElement)&&names[at].focus();}});
    let x0=null;
    stack.addEventListener('pointerdown',e=>{x0=e.clientX;});
    stack.addEventListener('pointerup',e=>{if(x0!==null&&Math.abs(e.clientX-x0)>40)go(at+(e.clientX<x0?1:-1),true);x0=null;});
    stack.addEventListener('pointercancel',()=>{x0=null;});
    if(!still)new IntersectionObserver(([e])=>{
      if(timer<0)return;
      clearInterval(timer);timer=e.isIntersecting?setInterval(()=>{if(!stack.matches(':hover'))go(at+1);},4500):0;
    },{threshold:.6}).observe(stack);
  }

  for(const f of document.querySelectorAll('form')){
    f.addEventListener('submit',e=>{
      e.preventDefault();
      f.querySelector('.sent')?.remove();
      const p=document.createElement('p');p.className='sent';p.setAttribute('role','status');
      p.textContent='Thanks, we have your details. This is a preview of the site, so the form is not connected yet.';
      f.append(p);
    });
  }
})();
