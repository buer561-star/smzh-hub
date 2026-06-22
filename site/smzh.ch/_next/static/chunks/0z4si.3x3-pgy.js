(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,939919,t=>{"use strict";let e,r=globalThis,i=r.ShadowRoot&&(void 0===r.ShadyCSS||r.ShadyCSS.nativeShadow)&&"adoptedStyleSheets"in Document.prototype&&"replace"in CSSStyleSheet.prototype,a=Symbol(),s=new WeakMap;class n{constructor(t,e,r){if(this._$cssResult$=!0,r!==a)throw Error("CSSResult is not constructable. Use `unsafeCSS` or `css` instead.");this.cssText=t,this.t=e}get styleSheet(){let t=this.o,e=this.t;if(i&&void 0===t){let r=void 0!==e&&1===e.length;r&&(t=s.get(e)),void 0===t&&((this.o=t=new CSSStyleSheet).replaceSync(this.cssText),r&&s.set(e,t))}return t}toString(){return this.cssText}}let o=t=>new n("string"==typeof t?t:t+"",void 0,a),l=(t,...e)=>new n(1===t.length?t[0]:e.reduce((e,r,i)=>e+(t=>{if(!0===t._$cssResult$)return t.cssText;if("number"==typeof t)return t;throw Error("Value passed to 'css' function must be a 'css' function result: "+t+". Use 'unsafeCSS' to pass non-literal values, but take care to ensure page security.")})(r)+t[i+1],t[0]),t,a),h=i?t=>t:t=>t instanceof CSSStyleSheet?(t=>{let e="";for(let r of t.cssRules)e+=r.cssText;return o(e)})(t):t,{is:c,defineProperty:d,getOwnPropertyDescriptor:p,getOwnPropertyNames:u,getOwnPropertySymbols:m,getPrototypeOf:g}=Object,f=globalThis,v=f.trustedTypes,y=v?v.emptyScript:"",b=f.reactiveElementPolyfillSupport,z={toAttribute(t,e){switch(e){case Boolean:t=t?y:null;break;case Object:case Array:t=null==t?t:JSON.stringify(t)}return t},fromAttribute(t,e){let r=t;switch(e){case Boolean:r=null!==t;break;case Number:r=null===t?null:Number(t);break;case Object:case Array:try{r=JSON.parse(t)}catch(t){r=null}}return r}},x=(t,e)=>!c(t,e),w={attribute:!0,type:String,converter:z,reflect:!1,useDefault:!1,hasChanged:x};Symbol.metadata??=Symbol("metadata"),f.litPropertyMetadata??=new WeakMap;class $ extends HTMLElement{static addInitializer(t){this._$Ei(),(this.l??=[]).push(t)}static get observedAttributes(){return this.finalize(),this._$Eh&&[...this._$Eh.keys()]}static createProperty(t,e=w){if(e.state&&(e.attribute=!1),this._$Ei(),this.prototype.hasOwnProperty(t)&&((e=Object.create(e)).wrapped=!0),this.elementProperties.set(t,e),!e.noAccessor){let r=Symbol(),i=this.getPropertyDescriptor(t,r,e);void 0!==i&&d(this.prototype,t,i)}}static getPropertyDescriptor(t,e,r){let{get:i,set:a}=p(this.prototype,t)??{get(){return this[e]},set(t){this[e]=t}};return{get:i,set(e){let s=i?.call(this);a?.call(this,e),this.requestUpdate(t,s,r)},configurable:!0,enumerable:!0}}static getPropertyOptions(t){return this.elementProperties.get(t)??w}static _$Ei(){if(this.hasOwnProperty("elementProperties"))return;let t=g(this);t.finalize(),void 0!==t.l&&(this.l=[...t.l]),this.elementProperties=new Map(t.elementProperties)}static finalize(){if(this.hasOwnProperty("finalized"))return;if(this.finalized=!0,this._$Ei(),this.hasOwnProperty("properties")){let t=this.properties;for(let e of[...u(t),...m(t)])this.createProperty(e,t[e])}let t=this[Symbol.metadata];if(null!==t){let e=litPropertyMetadata.get(t);if(void 0!==e)for(let[t,r]of e)this.elementProperties.set(t,r)}for(let[t,e]of(this._$Eh=new Map,this.elementProperties)){let r=this._$Eu(t,e);void 0!==r&&this._$Eh.set(r,t)}this.elementStyles=this.finalizeStyles(this.styles)}static finalizeStyles(t){let e=[];if(Array.isArray(t))for(let r of new Set(t.flat(1/0).reverse()))e.unshift(h(r));else void 0!==t&&e.push(h(t));return e}static _$Eu(t,e){let r=e.attribute;return!1===r?void 0:"string"==typeof r?r:"string"==typeof t?t.toLowerCase():void 0}constructor(){super(),this._$Ep=void 0,this.isUpdatePending=!1,this.hasUpdated=!1,this._$Em=null,this._$Ev()}_$Ev(){this._$ES=new Promise(t=>this.enableUpdating=t),this._$AL=new Map,this._$E_(),this.requestUpdate(),this.constructor.l?.forEach(t=>t(this))}addController(t){(this._$EO??=new Set).add(t),void 0!==this.renderRoot&&this.isConnected&&t.hostConnected?.()}removeController(t){this._$EO?.delete(t)}_$E_(){let t=new Map;for(let e of this.constructor.elementProperties.keys())this.hasOwnProperty(e)&&(t.set(e,this[e]),delete this[e]);t.size>0&&(this._$Ep=t)}createRenderRoot(){let t=this.shadowRoot??this.attachShadow(this.constructor.shadowRootOptions);return((t,e)=>{if(i)t.adoptedStyleSheets=e.map(t=>t instanceof CSSStyleSheet?t:t.styleSheet);else for(let i of e){let e=document.createElement("style"),a=r.litNonce;void 0!==a&&e.setAttribute("nonce",a),e.textContent=i.cssText,t.appendChild(e)}})(t,this.constructor.elementStyles),t}connectedCallback(){this.renderRoot??=this.createRenderRoot(),this.enableUpdating(!0),this._$EO?.forEach(t=>t.hostConnected?.())}enableUpdating(t){}disconnectedCallback(){this._$EO?.forEach(t=>t.hostDisconnected?.())}attributeChangedCallback(t,e,r){this._$AK(t,r)}_$ET(t,e){let r=this.constructor.elementProperties.get(t),i=this.constructor._$Eu(t,r);if(void 0!==i&&!0===r.reflect){let a=(void 0!==r.converter?.toAttribute?r.converter:z).toAttribute(e,r.type);this._$Em=t,null==a?this.removeAttribute(i):this.setAttribute(i,a),this._$Em=null}}_$AK(t,e){let r=this.constructor,i=r._$Eh.get(t);if(void 0!==i&&this._$Em!==i){let t=r.getPropertyOptions(i),a="function"==typeof t.converter?{fromAttribute:t.converter}:void 0!==t.converter?.fromAttribute?t.converter:z;this._$Em=i;let s=a.fromAttribute(e,t.type);this[i]=s??this._$Ej?.get(i)??s,this._$Em=null}}requestUpdate(t,e,r,i=!1,a){if(void 0!==t){let s=this.constructor;if(!1===i&&(a=this[t]),!(((r??=s.getPropertyOptions(t)).hasChanged??x)(a,e)||r.useDefault&&r.reflect&&a===this._$Ej?.get(t)&&!this.hasAttribute(s._$Eu(t,r))))return;this.C(t,e,r)}!1===this.isUpdatePending&&(this._$ES=this._$EP())}C(t,e,{useDefault:r,reflect:i,wrapped:a},s){r&&!(this._$Ej??=new Map).has(t)&&(this._$Ej.set(t,s??e??this[t]),!0!==a||void 0!==s)||(this._$AL.has(t)||(this.hasUpdated||r||(e=void 0),this._$AL.set(t,e)),!0===i&&this._$Em!==t&&(this._$Eq??=new Set).add(t))}async _$EP(){this.isUpdatePending=!0;try{await this._$ES}catch(t){Promise.reject(t)}let t=this.scheduleUpdate();return null!=t&&await t,!this.isUpdatePending}scheduleUpdate(){return this.performUpdate()}performUpdate(){if(!this.isUpdatePending)return;if(!this.hasUpdated){if(this.renderRoot??=this.createRenderRoot(),this._$Ep){for(let[t,e]of this._$Ep)this[t]=e;this._$Ep=void 0}let t=this.constructor.elementProperties;if(t.size>0)for(let[e,r]of t){let{wrapped:t}=r,i=this[e];!0!==t||this._$AL.has(e)||void 0===i||this.C(e,void 0,r,i)}}let t=!1,e=this._$AL;try{(t=this.shouldUpdate(e))?(this.willUpdate(e),this._$EO?.forEach(t=>t.hostUpdate?.()),this.update(e)):this._$EM()}catch(e){throw t=!1,this._$EM(),e}t&&this._$AE(e)}willUpdate(t){}_$AE(t){this._$EO?.forEach(t=>t.hostUpdated?.()),this.hasUpdated||(this.hasUpdated=!0,this.firstUpdated(t)),this.updated(t)}_$EM(){this._$AL=new Map,this.isUpdatePending=!1}get updateComplete(){return this.getUpdateComplete()}getUpdateComplete(){return this._$ES}shouldUpdate(t){return!0}update(t){this._$Eq&&=this._$Eq.forEach(t=>this._$ET(t,this[t])),this._$EM()}updated(t){}firstUpdated(t){}}$.elementStyles=[],$.shadowRootOptions={mode:"open"},$.elementProperties=new Map,$.finalized=new Map,b?.({ReactiveElement:$}),(f.reactiveElementVersions??=[]).push("2.1.2");let k=globalThis,S=t=>t,_=k.trustedTypes,A=_?_.createPolicy("lit-html",{createHTML:t=>t}):void 0,M="$lit$",C=`lit$${Math.random().toFixed(9).slice(2)}$`,E="?"+C,T=`<${E}>`,N=document,I=()=>N.createComment(""),P=t=>null===t||"object"!=typeof t&&"function"!=typeof t,L=Array.isArray,R=t=>L(t)||"function"==typeof t?.[Symbol.iterator],D="[ 	\n\f\r]",F=/<(?:(!--|\/[^a-zA-Z])|(\/?[a-zA-Z][^>\s]*)|(\/?$))/g,j=/-->/g,H=/>/g,O=RegExp(`>|${D}(?:([^\\s"'>=/]+)(${D}*=${D}*(?:[^ 	
\f\r"'\`<>=]|("|')|))|$)`,"g"),B=/'/g,q=/"/g,U=/^(?:script|style|textarea|title)$/i,V=t=>(e,...r)=>({_$litType$:t,strings:e,values:r}),W=V(1),G=V(2),X=V(3),Y=Symbol.for("lit-noChange"),Z=Symbol.for("lit-nothing"),K=new WeakMap,J=N.createTreeWalker(N,129);function Q(t,e){if(!L(t)||!t.hasOwnProperty("raw"))throw Error("invalid template strings array");return void 0!==A?A.createHTML(e):e}let tt=(t,e)=>{let r=t.length-1,i=[],a,s=2===e?"<svg>":3===e?"<math>":"",n=F;for(let e=0;e<r;e++){let r=t[e],o,l,h=-1,c=0;for(;c<r.length&&(n.lastIndex=c,null!==(l=n.exec(r)));)c=n.lastIndex,n===F?"!--"===l[1]?n=j:void 0!==l[1]?n=H:void 0!==l[2]?(U.test(l[2])&&(a=RegExp("</"+l[2],"g")),n=O):void 0!==l[3]&&(n=O):n===O?">"===l[0]?(n=a??F,h=-1):void 0===l[1]?h=-2:(h=n.lastIndex-l[2].length,o=l[1],n=void 0===l[3]?O:'"'===l[3]?q:B):n===q||n===B?n=O:n===j||n===H?n=F:(n=O,a=void 0);let d=n===O&&t[e+1].startsWith("/>")?" ":"";s+=n===F?r+T:h>=0?(i.push(o),r.slice(0,h)+M+r.slice(h)+C+d):r+C+(-2===h?e:d)}return[Q(t,s+(t[r]||"<?>")+(2===e?"</svg>":3===e?"</math>":"")),i]};class te{constructor({strings:t,_$litType$:e},r){let i;this.parts=[];let a=0,s=0;const n=t.length-1,o=this.parts,[l,h]=tt(t,e);if(this.el=te.createElement(l,r),J.currentNode=this.el.content,2===e||3===e){const t=this.el.content.firstChild;t.replaceWith(...t.childNodes)}for(;null!==(i=J.nextNode())&&o.length<n;){if(1===i.nodeType){if(i.hasAttributes())for(const t of i.getAttributeNames())if(t.endsWith(M)){const e=h[s++],r=i.getAttribute(t).split(C),n=/([.?@])?(.*)/.exec(e);o.push({type:1,index:a,name:n[2],strings:r,ctor:"."===n[1]?tn:"?"===n[1]?to:"@"===n[1]?tl:ts}),i.removeAttribute(t)}else t.startsWith(C)&&(o.push({type:6,index:a}),i.removeAttribute(t));if(U.test(i.tagName)){const t=i.textContent.split(C),e=t.length-1;if(e>0){i.textContent=_?_.emptyScript:"";for(let r=0;r<e;r++)i.append(t[r],I()),J.nextNode(),o.push({type:2,index:++a});i.append(t[e],I())}}}else if(8===i.nodeType)if(i.data===E)o.push({type:2,index:a});else{let t=-1;for(;-1!==(t=i.data.indexOf(C,t+1));)o.push({type:7,index:a}),t+=C.length-1}a++}}static createElement(t,e){let r=N.createElement("template");return r.innerHTML=t,r}}function tr(t,e,r=t,i){if(e===Y)return e;let a=void 0!==i?r._$Co?.[i]:r._$Cl,s=P(e)?void 0:e._$litDirective$;return a?.constructor!==s&&(a?._$AO?.(!1),void 0===s?a=void 0:(a=new s(t))._$AT(t,r,i),void 0!==i?(r._$Co??=[])[i]=a:r._$Cl=a),void 0!==a&&(e=tr(t,a._$AS(t,e.values),a,i)),e}class ti{constructor(t,e){this._$AV=[],this._$AN=void 0,this._$AD=t,this._$AM=e}get parentNode(){return this._$AM.parentNode}get _$AU(){return this._$AM._$AU}u(t){let{el:{content:e},parts:r}=this._$AD,i=(t?.creationScope??N).importNode(e,!0);J.currentNode=i;let a=J.nextNode(),s=0,n=0,o=r[0];for(;void 0!==o;){if(s===o.index){let e;2===o.type?e=new ta(a,a.nextSibling,this,t):1===o.type?e=new o.ctor(a,o.name,o.strings,this,t):6===o.type&&(e=new th(a,this,t)),this._$AV.push(e),o=r[++n]}s!==o?.index&&(a=J.nextNode(),s++)}return J.currentNode=N,i}p(t){let e=0;for(let r of this._$AV)void 0!==r&&(void 0!==r.strings?(r._$AI(t,r,e),e+=r.strings.length-2):r._$AI(t[e])),e++}}class ta{get _$AU(){return this._$AM?._$AU??this._$Cv}constructor(t,e,r,i){this.type=2,this._$AH=Z,this._$AN=void 0,this._$AA=t,this._$AB=e,this._$AM=r,this.options=i,this._$Cv=i?.isConnected??!0}get parentNode(){let t=this._$AA.parentNode,e=this._$AM;return void 0!==e&&11===t?.nodeType&&(t=e.parentNode),t}get startNode(){return this._$AA}get endNode(){return this._$AB}_$AI(t,e=this){P(t=tr(this,t,e))?t===Z||null==t||""===t?(this._$AH!==Z&&this._$AR(),this._$AH=Z):t!==this._$AH&&t!==Y&&this._(t):void 0!==t._$litType$?this.$(t):void 0!==t.nodeType?this.T(t):R(t)?this.k(t):this._(t)}O(t){return this._$AA.parentNode.insertBefore(t,this._$AB)}T(t){this._$AH!==t&&(this._$AR(),this._$AH=this.O(t))}_(t){this._$AH!==Z&&P(this._$AH)?this._$AA.nextSibling.data=t:this.T(N.createTextNode(t)),this._$AH=t}$(t){let{values:e,_$litType$:r}=t,i="number"==typeof r?this._$AC(t):(void 0===r.el&&(r.el=te.createElement(Q(r.h,r.h[0]),this.options)),r);if(this._$AH?._$AD===i)this._$AH.p(e);else{let t=new ti(i,this),r=t.u(this.options);t.p(e),this.T(r),this._$AH=t}}_$AC(t){let e=K.get(t.strings);return void 0===e&&K.set(t.strings,e=new te(t)),e}k(t){L(this._$AH)||(this._$AH=[],this._$AR());let e=this._$AH,r,i=0;for(let a of t)i===e.length?e.push(r=new ta(this.O(I()),this.O(I()),this,this.options)):r=e[i],r._$AI(a),i++;i<e.length&&(this._$AR(r&&r._$AB.nextSibling,i),e.length=i)}_$AR(t=this._$AA.nextSibling,e){for(this._$AP?.(!1,!0,e);t!==this._$AB;){let e=S(t).nextSibling;S(t).remove(),t=e}}setConnected(t){void 0===this._$AM&&(this._$Cv=t,this._$AP?.(t))}}class ts{get tagName(){return this.element.tagName}get _$AU(){return this._$AM._$AU}constructor(t,e,r,i,a){this.type=1,this._$AH=Z,this._$AN=void 0,this.element=t,this.name=e,this._$AM=i,this.options=a,r.length>2||""!==r[0]||""!==r[1]?(this._$AH=Array(r.length-1).fill(new String),this.strings=r):this._$AH=Z}_$AI(t,e=this,r,i){let a=this.strings,s=!1;if(void 0===a)(s=!P(t=tr(this,t,e,0))||t!==this._$AH&&t!==Y)&&(this._$AH=t);else{let i,n,o=t;for(t=a[0],i=0;i<a.length-1;i++)(n=tr(this,o[r+i],e,i))===Y&&(n=this._$AH[i]),s||=!P(n)||n!==this._$AH[i],n===Z?t=Z:t!==Z&&(t+=(n??"")+a[i+1]),this._$AH[i]=n}s&&!i&&this.j(t)}j(t){t===Z?this.element.removeAttribute(this.name):this.element.setAttribute(this.name,t??"")}}class tn extends ts{constructor(){super(...arguments),this.type=3}j(t){this.element[this.name]=t===Z?void 0:t}}class to extends ts{constructor(){super(...arguments),this.type=4}j(t){this.element.toggleAttribute(this.name,!!t&&t!==Z)}}class tl extends ts{constructor(t,e,r,i,a){super(t,e,r,i,a),this.type=5}_$AI(t,e=this){if((t=tr(this,t,e,0)??Z)===Y)return;let r=this._$AH,i=t===Z&&r!==Z||t.capture!==r.capture||t.once!==r.once||t.passive!==r.passive,a=t!==Z&&(r===Z||i);i&&this.element.removeEventListener(this.name,this,r),a&&this.element.addEventListener(this.name,this,t),this._$AH=t}handleEvent(t){"function"==typeof this._$AH?this._$AH.call(this.options?.host??this.element,t):this._$AH.handleEvent(t)}}class th{constructor(t,e,r){this.element=t,this.type=6,this._$AN=void 0,this._$AM=e,this.options=r}get _$AU(){return this._$AM._$AU}_$AI(t){tr(this,t)}}let tc=k.litHtmlPolyfillSupport;tc?.(te,ta),(k.litHtmlVersions??=[]).push("3.3.2");let td=globalThis;class tp extends ${constructor(){super(...arguments),this.renderOptions={host:this},this._$Do=void 0}createRenderRoot(){let t=super.createRenderRoot();return this.renderOptions.renderBefore??=t.firstChild,t}update(t){let e=this.render();this.hasUpdated||(this.renderOptions.isConnected=this.isConnected),super.update(t),this._$Do=((t,e,r)=>{let i=r?.renderBefore??e,a=i._$litPart$;if(void 0===a){let t=r?.renderBefore??null;i._$litPart$=a=new ta(e.insertBefore(I(),t),t,void 0,r??{})}return a._$AI(t),a})(e,this.renderRoot,this.renderOptions)}connectedCallback(){super.connectedCallback(),this._$Do?.setConnected(!0)}disconnectedCallback(){super.disconnectedCallback(),this._$Do?.setConnected(!1)}render(){return Y}}tp._$litElement$=!0,tp.finalized=!0,td.litElementHydrateSupport?.({LitElement:tp});let tu=td.litElementPolyfillSupport;tu?.({LitElement:tp}),(td.litElementVersions??=[]).push("4.2.2");let tm=l`
  :host {
    display: inline-block;
    width: var(--smzh-button-host-width, auto);
  }

  .button[data-full-width="true"] {
    box-sizing: border-box;
    width: 100%;
  }

  .button {
    --smzh-button-radius: 24px;
    --smzh-button-px: var(--smzh-spacing-x-sm);
    --smzh-button-py: var(--smzh-spacing-xxx-sm);
    --smzh-button-gap: var(--smzh-spacing-xxx-sm);

    align-items: center;
    background: var(--smzh-color-primary-active);
    border: 1px solid var(--smzh-color-primary-active);
    border-radius: var(--smzh-button-radius);
    color: var(--smzh-color-text-on-primary);
    cursor: pointer;
    display: inline-flex;
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-md-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    gap: var(--smzh-button-gap);
    justify-content: center;
    letter-spacing: var(--smzh-typography-text-md-letter-spacing);
    line-height: var(--smzh-typography-text-md-line-height);
    padding: var(--smzh-button-py) var(--smzh-button-px);
    transition:
      background-color 140ms ease,
      border-color 140ms ease,
      color 140ms ease,
      box-shadow 140ms ease,
      opacity 140ms ease;
    white-space: nowrap;
  }

  .text {
    line-height: inherit;
  }

  .text[data-hidden="true"] {
    display: none;
  }

  .icon {
    align-items: center;
    display: inline-flex;
    flex: 0 0 auto;
    height: 20px;
    justify-content: center;
    width: 20px;
  }

  .spinner {
    animation: smzh-button-spin 1s linear infinite;
    border-color: currentColor;
    border-radius: 50%;
    border-style: solid;
    border-top-color: transparent;
    border-width: 2px;
    box-sizing: border-box;
    display: inline-block;
    flex-shrink: 0;
    height: var(--smzh-button-spinner-size, 16px);
    width: var(--smzh-button-spinner-size, 16px);
  }

  .button[data-size="sm"] {
    --smzh-button-px: var(--smzh-spacing-x-sm);
    --smzh-button-py: var(--smzh-spacing-xxx-sm);
  }

  .button[data-size="md"] {
    --smzh-button-px: var(--smzh-spacing-md);
    --smzh-button-py: var(--smzh-spacing-xx-sm);
  }

  .button[data-size="lg"] {
    --smzh-button-px: var(--smzh-spacing-x-md);
    --smzh-button-py: var(--smzh-spacing-x-sm);
  }

  .button[data-icon-only="true"] {
    --smzh-button-px: 0;
    --smzh-button-py: 0;
    height: var(--smzh-button-icon-size, 40px);
    min-height: var(--smzh-button-icon-size, 40px);
    min-width: var(--smzh-button-icon-size, 40px);
    padding: 0;
    width: var(--smzh-button-icon-size, 40px);
  }

  .button[data-icon-only="true"][data-size="sm"] {
    --smzh-button-icon-size: 40px;
  }

  .button[data-icon-only="true"][data-size="md"] {
    --smzh-button-icon-size: 44px;
  }

  .button[data-icon-only="true"][data-size="lg"] {
    --smzh-button-icon-size: 48px;
  }

  .button[data-icon-only="true"][data-full-width="true"] {
    min-width: 0;
    width: 100%;
  }

  .button[data-shape="pill"] {
    --smzh-button-radius: 24px;
  }

  .button[data-shape="rounded"] {
    --smzh-button-radius: var(--smzh-spacing-xxx-sm);
  }

  .button[data-variant="primary"] {
    background: var(--smzh-color-primary-active);
    border-color: var(--smzh-color-primary-active);
    color: var(--smzh-color-text-on-primary);
  }

  .button[data-variant="primary"]:hover:not(:disabled) {
    background: var(--smzh-color-primary);
    border-color: var(--smzh-color-primary);
  }

  .button[data-variant="primary"]:active:not(:disabled) {
    background: var(--smzh-color-primary-hover);
    border-color: var(--smzh-color-primary-hover);
  }

  .button[data-variant="secondary"] {
    background: var(--smzh-color-surface);
    border-color: var(--smzh-color-border-default);
    color: var(--smzh-color-primary-active);
  }

  .button[data-variant="secondary"]:hover:not(:disabled) {
    background: var(--smzh-color-surface);
    border-color: var(--smzh-color-border-strong);
    box-shadow: var(--smzh-color-shadow-xs);
    color: var(--smzh-color-primary-active);
  }

  .button[data-variant="secondary"]:active:not(:disabled) {
    background: var(--smzh-color-surface);
    border-color: var(--smzh-color-border-strong);
    box-shadow: none;
    color: var(--smzh-color-primary-active);
  }

  .button[data-variant="tertiary"] {
    background: transparent;
    border-color: transparent;
    color: var(--smzh-color-primary-active);
  }

  .button[data-variant="tertiary"]:hover:not(:disabled) {
    background: var(--smzh-color-primary-subtle-hover);
  }

  .button[data-variant="tertiary"]:active:not(:disabled) {
    background: var(--smzh-color-primary-subtle-active);
  }

  .button[data-variant="tertiary"]:hover:not(:disabled) .text,
  .button[data-variant="tertiary"]:active:not(:disabled) .text {
    text-decoration: underline;
  }

  .button[data-variant="destructive"] {
    background: var(--smzh-color-error);
    border-color: var(--smzh-color-error-border);
    color: var(--smzh-color-text-on-primary);
  }

  .button[data-variant="destructive"]:hover:not(:disabled) {
    background: var(--smzh-color-error-hover);
    border-color: var(--smzh-color-error-hover);
    color: var(--smzh-color-text-on-primary);
  }

  .button[data-variant="destructive"]:active:not(:disabled) {
    background: var(--smzh-color-error-active);
    border-color: var(--smzh-color-error-active);
    color: var(--smzh-color-text-on-primary);
  }

  .button[data-inverse="true"][data-variant="primary"] {
    background: var(--smzh-color-surface);
    border-color: var(--smzh-color-surface);
    color: var(--smzh-color-primary-active);
  }

  .button[data-inverse="true"][data-variant="primary"]:hover:not(:disabled) {
    background: var(--smzh-color-primary);
    border-color: var(--smzh-color-primary);
    color: var(--smzh-color-text-on-primary);
  }

  .button[data-inverse="true"][data-variant="primary"]:active:not(:disabled) {
    background: var(--smzh-color-primary-hover);
    border-color: var(--smzh-color-primary-hover);
    color: var(--smzh-color-text-on-primary);
  }

  .button[data-inverse="true"][data-variant="secondary"] {
    background: transparent;
    border-color: var(--smzh-color-surface);
    box-shadow: none;
    color: var(--smzh-color-surface);
  }

  .button[data-inverse="true"][data-variant="tertiary"] {
    color: var(--smzh-color-surface);
  }

  .button[data-inverse="true"][data-variant="tertiary"]:hover:not(:disabled) {
    background: var(--smzh-color-primary-subtle-hover);
  }

  .button[data-inverse="true"][data-variant="tertiary"]:active:not(:disabled) {
    background: var(--smzh-color-primary-subtle-active);
  }

  .button[data-inverse="true"][data-variant="tertiary"]:hover:not(:disabled)
    .text,
  .button[data-inverse="true"][data-variant="tertiary"]:active:not(:disabled)
    .text {
    text-decoration: underline;
  }

  .button[data-inverse="true"][data-variant="destructive"] {
    background: var(--smzh-color-error-subtle);
    border-color: var(--smzh-color-error-subtle);
    color: var(--smzh-color-text-error-strong);
  }

  .button[data-inverse="true"][data-variant="destructive"]:hover:not(
      :disabled
    ) {
    background: var(--smzh-color-error-hover);
    border-color: var(--smzh-color-error-hover);
    color: var(--smzh-color-text-on-primary);
  }

  .button[data-inverse="true"][data-variant="destructive"]:active:not(
      :disabled
    ) {
    background: var(--smzh-color-error-active);
    border-color: var(--smzh-color-error-active);
    color: var(--smzh-color-text-on-primary);
  }

  .button:focus-visible {
    outline: none;
    box-shadow:
      0 0 0 2px var(--smzh-color-surface),
      0 0 0 4px var(--smzh-color-primary-active);
  }

  .button[data-variant="destructive"]:focus-visible {
    box-shadow:
      0 0 0 2px var(--smzh-color-surface),
      0 0 0 4px var(--smzh-color-error);
  }

  .button[data-inverse="true"]:focus-visible {
    box-shadow:
      0 0 0 2px var(--smzh-color-primary-active),
      0 0 0 4px var(--smzh-color-surface);
  }

  .button[data-inverse="true"][data-variant="destructive"]:focus-visible {
    box-shadow:
      0 0 0 2px var(--smzh-color-primary-active),
      0 0 0 4px var(--smzh-color-error);
  }

  .button:disabled {
    background: var(--smzh-color-background);
    border-color: var(--smzh-color-background);
    color: var(--smzh-color-text-disabled);
    cursor: not-allowed;
  }

  .button[data-variant="secondary"]:disabled {
    background: var(--smzh-color-background-subtle);
    border-width: 0;
    border-color: transparent;
    box-shadow: none;
  }

  .button[data-variant="destructive"]:disabled {
    background: var(--smzh-color-error-disabled);
    border-color: var(--smzh-color-error-disabled);
    color: var(--smzh-color-text-error-strong);
  }

  .button[data-inverse="true"][data-variant="destructive"]:disabled {
    background: var(--smzh-color-error-disabled);
    border-color: var(--smzh-color-border-default);
    color: var(--smzh-color-text-error-strong);
  }

  .button[data-variant="tertiary"]:disabled {
    background: transparent;
    border-color: transparent;
  }

  @keyframes smzh-button-spin {
    to {
      transform: rotate(360deg);
    }
  }
`,tg=["primary","secondary","tertiary","destructive"],tf="primary",tv=["sm","md","lg"],ty=["pill","rounded"],tb="pill",tz=["leading","trailing"],tx="leading",tw=["button","submit","reset"],t$="button";function tk(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="m6 9 6 6 6-6" />
  </svg>`}let tS={"chevron-right":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="m9 18 6-6-6-6" />
  </svg>`},"chevron-left":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="m15 18-6-6 6-6" />
  </svg>`},"chevron-up":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="m18 15-6-6-6 6" />
  </svg>`},"chevron-down":tk,"chevrons-up-down":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="m7 15 5 5 5-5" />
    <path d="m7 9 5-5 5 5" />
  </svg>`},plus:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M5 12h14" />
    <path d="M12 5v14" />
  </svg>`},close:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M18 6 6 18" />
    <path d="m6 6 12 12" />
  </svg>`},check:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M20 6 9 17l-5-5" />
  </svg>`},"thumbs-up":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88Z" />
    <path d="M7 10v12" />
  </svg>`},minus:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M5 12h14" />
  </svg>`},search:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="m21 21-4.34-4.34" />
    <circle cx="11" cy="11" r="8" />
  </svg>`},settings:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M9.671 4.136a2.34 2.34 0 0 1 4.659 0 2.34 2.34 0 0 0 3.319 1.915 2.34 2.34 0 0 1 2.33 4.033 2.34 2.34 0 0 0 0 3.831 2.34 2.34 0 0 1-2.33 4.033 2.34 2.34 0 0 0-3.319 1.915 2.34 2.34 0 0 1-4.659 0 2.34 2.34 0 0 0-3.32-1.915 2.34 2.34 0 0 1-2.33-4.033 2.34 2.34 0 0 0 0-3.831A2.34 2.34 0 0 1 6.35 6.051a2.34 2.34 0 0 0 3.319-1.915" />
    <circle cx="12" cy="12" r="3" />
  </svg>`},"chart-no-axes-combined":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M12 16v5" />
    <path d="M16 14v7" />
    <path d="M20 10v11" />
    <path d="m22 3-8.646 8.646a.5.5 0 0 1-.708 0L9.354 8.354a.5.5 0 0 0-.707 0L2 15" />
    <path d="M4 18v3" />
    <path d="M8 14v7" />
  </svg>`},"chart-pie":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M21 12c.552 0 1.005-.449.95-.998a10 10 0 0 0-8.953-8.951c-.55-.055-.998.398-.998.95v8a1 1 0 0 0 1 1z" />
    <path d="M21.21 15.89A10 10 0 1 1 8 2.83" />
  </svg>`},"calendar-days":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M8 2v4" />
    <path d="M16 2v4" />
    <rect width="18" height="18" x="3" y="4" rx="2" />
    <path d="M3 10h18" />
    <path d="M8 14h.01" />
    <path d="M12 14h.01" />
    <path d="M16 14h.01" />
    <path d="M8 18h.01" />
    <path d="M12 18h.01" />
    <path d="M16 18h.01" />
  </svg>`},banknote:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <rect width="20" height="12" x="2" y="6" rx="2" />
    <circle cx="12" cy="12" r="2" />
    <path d="M6 12h.01M18 12h.01" />
  </svg>`},landmark:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M10 18v-7" />
    <path d="M11.12 2.198a2 2 0 0 1 1.76.006l7.866 3.847c.476.233.31.949-.22.949H3.474c-.53 0-.695-.716-.22-.949z" />
    <path d="M14 18v-7" />
    <path d="M18 18v-7" />
    <path d="M3 22h18" />
    <path d="M6 18v-7" />
  </svg>`},house:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8" />
    <path d="M3 10a2 2 0 0 1 .709-1.528l7-6a2 2 0 0 1 2.582 0l7 6A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
  </svg>`},heart:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5" />
  </svg>`},car:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="m21 8-2 2-1.5-3.7A2 2 0 0 0 15.646 5H8.4a2 2 0 0 0-1.903 1.257L5 10 3 8" />
    <path d="M7 14h.01" />
    <path d="M17 14h.01" />
    <rect width="18" height="8" x="3" y="10" rx="2" />
    <path d="M5 18v2" />
    <path d="M19 18v2" />
  </svg>`},fuel:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M14 13h2a2 2 0 0 1 2 2v2a2 2 0 0 0 4 0v-6.998a2 2 0 0 0-.59-1.42L18 5" />
    <path d="M14 21V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v16" />
    <path d="M2 21h13" />
    <path d="M3 9h11" />
  </svg>`},"hand-coins":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M11 15h2a2 2 0 1 0 0-4h-3c-.6 0-1.1.2-1.4.6L3 17" />
    <path d="m7 21 1.6-1.4c.3-.4.8-.6 1.4-.6h4c1.1 0 2.1-.4 2.8-1.2l4.6-4.4a2 2 0 0 0-2.75-2.91l-4.2 3.9" />
    <path d="m2 16 6 6" />
    <circle cx="16" cy="9" r="2.9" />
    <circle cx="6" cy="5" r="3" />
  </svg>`},info:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <circle cx="12" cy="12" r="10" />
    <path d="M12 16v-4" />
    <path d="M12 8h.01" />
  </svg>`},"help-circle":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <circle cx="12" cy="12" r="10" />
    <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" />
    <path d="M12 17h.01" />
  </svg>`},"alert-circle":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <circle cx="12" cy="12" r="10" />
    <line x1="12" x2="12" y1="8" y2="12" />
    <line x1="12" x2="12.01" y1="16" y2="16" />
  </svg>`},"alert-triangle":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3" />
    <path d="M12 9v4" />
    <path d="M12 17h.01" />
  </svg>`},loader:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M12 2v4" />
    <path d="m16.2 7.8 2.9-2.9" />
    <path d="M18 12h4" />
    <path d="m16.2 16.2 2.9 2.9" />
    <path d="M12 18v4" />
    <path d="m4.9 19.1 2.9-2.9" />
    <path d="M2 12h4" />
    <path d="m4.9 4.9 2.9 2.9" />
  </svg>`},calendar:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M8 2v4" />
    <path d="M16 2v4" />
    <rect width="18" height="18" x="3" y="4" rx="2" />
    <path d="M3 10h18" />
  </svg>`},clock:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <circle cx="12" cy="12" r="10" />
    <path d="M12 6v6l4 2" />
  </svg>`},"external-link":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M15 3h6v6" />
    <path d="M10 14 21 3" />
    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
  </svg>`},"file-text":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z" />
    <path d="M14 2v5a1 1 0 0 0 1 1h5" />
    <path d="M10 9H8" />
    <path d="M16 13H8" />
    <path d="M16 17H8" />
  </svg>`},send:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z" />
    <path d="m21.854 2.147-10.94 10.939" />
  </svg>`},"arrow-up-right":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M7 7h10v10" />
    <path d="M7 17 17 7" />
  </svg>`},"file-pen-line":function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M14.364 13.634a2 2 0 0 0-.506.854l-.837 2.87a.5.5 0 0 0 .62.62l2.87-.837a2 2 0 0 0 .854-.506l4.013-4.009a1 1 0 0 0-3.004-3.004z" />
    <path d="M14.487 7.858A1 1 0 0 1 14 7V2" />
    <path d="M20 19.645V20a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l2.516 2.516" />
    <path d="M8 18h1" />
  </svg>`},download:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M12 15V3" />
    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
    <path d="m7 10 5 5 5-5" />
  </svg>`},upload:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M12 3v12" />
    <path d="m17 8-5-5-5 5" />
    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
  </svg>`},trash:function(t){let e=t?.stroke??"currentColor",r="number"==typeof t?.size&&Number.isFinite(t.size)&&t.size>0?t.size:20;return W`<svg
    width=${r}
    height=${r}
    viewBox="0 0 24 24"
    fill="none"
    stroke=${e}
    stroke-width="2"
    stroke-linecap="round"
    stroke-linejoin="round"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M10 11v6" />
    <path d="M14 11v6" />
    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6" />
    <path d="M3 6h18" />
    <path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" />
  </svg>`}};function t_(t){return"string"==typeof t&&t in tS}Object.keys(tS),"u">typeof window&&!customElements.get("smzh-button")&&customElements.define("smzh-button",class extends tp{hasWarnedMissingIconOnlyAriaLabel=!1;hasWarnedInvalidIconName=!1;lightDomObserver=null;lightDomReactionScheduled=!1;static styles=tm;static properties={variant:{type:String,reflect:!0},size:{type:String,reflect:!0},shape:{type:String,reflect:!0},inverse:{type:Boolean,reflect:!0},disabled:{type:Boolean,reflect:!0},loading:{type:Boolean,reflect:!0},iconPosition:{type:String,attribute:"icon-position",reflect:!0},icon:{type:String,reflect:!0},ariaLabel:{type:String,attribute:"aria-label"},type:{type:String,reflect:!0},fullWidth:{type:Boolean,attribute:"full-width",reflect:!0}};constructor(){super(),this.variant=tf,this.size="sm",this.shape=tb,this.inverse=!1,this.disabled=!1,this.loading=!1,this.iconPosition=tx,this.icon=void 0,this.ariaLabel=null,this.type=t$,this.fullWidth=!1}connectedCallback(){super.connectedCallback(),this.observeLightDom()}disconnectedCallback(){this.unobserveLightDom(),this.style.removeProperty("--smzh-button-host-width"),super.disconnectedCallback()}willUpdate(t){super.willUpdate(t),t.has("fullWidth")&&this.syncHostFullWidth()}firstUpdated(){this.reportIconOnlyA11yIssue(),this.reportInvalidIconName()}updated(t){(t.has("icon")||t.has("loading")||t.has("ariaLabel"))&&this.reportIconOnlyA11yIssue(),t.has("icon")&&this.reportInvalidIconName()}resolveVariant(){var t;return"string"==typeof(t=this.variant)&&tg.includes(t)?this.variant:tf}resolveSize(){var t;return"string"==typeof(t=this.size)&&tv.includes(t)?this.size:"sm"}resolveShape(){var t;return"string"==typeof(t=this.shape)&&ty.includes(t)?this.shape:tb}resolveIconPosition(){var t;return"string"==typeof(t=this.iconPosition)&&tz.includes(t)?this.iconPosition:tx}resolveType(){var t;return"string"==typeof(t=this.type)&&tw.includes(t)?this.type:t$}isFullWidthActive(){return!0===this.fullWidth}syncHostFullWidth(){this.isFullWidthActive()?this.style.setProperty("--smzh-button-host-width","100%"):this.style.removeProperty("--smzh-button-host-width")}resolveAriaLabel(){if("string"==typeof this.ariaLabel&&this.ariaLabel.trim().length>0)return this.ariaLabel;let t=this.getAttribute("aria-label");if("string"==typeof t&&t.trim().length>0)return t}getDefaultSlotText(){let t=[];for(let e of Array.from(this.childNodes)){if(e.nodeType===Node.TEXT_NODE){t.push(e.textContent??"");continue}if(e.nodeType===Node.ELEMENT_NODE){let r=e.getAttribute("slot");if("icon-leading"===r||"icon-trailing"===r)continue;t.push(e.textContent??"")}}return t.join(" ").trim()}hasSlottedIcon(t){return null!==this.querySelector(`[slot="${t}"]`)}getButtonVisualState(){let t=this.getDefaultSlotText().length>0,e=this.hasSlottedIcon("icon-leading"),r=this.hasSlottedIcon("icon-trailing"),i=t_(this.icon),a=this.loading||i||e||r;return{hasDefaultSlotText:t,hasLeadingSlot:e,hasTrailingSlot:r,hasNamedIcon:i,hasVisualIcon:a,isIconOnly:!t&&a}}renderIconSlot(t,e){if(this.loading)return W`<span class="icon" aria-hidden="true"
        ><span class="spinner" role="presentation"></span
      ></span>`;let r=t_(this.icon)?this.icon:void 0;return e?W`<span class="icon" aria-hidden="true"
        ><slot name=${t} @slotchange=${this.handleSlotChange}></slot
      ></span>`:r?W`<span class="icon" aria-hidden="true"
        >${tS[r](void 0)}</span
      >`:Z}observeLightDom(){"u">typeof MutationObserver&&(this.unobserveLightDom(),this.lightDomObserver=new MutationObserver(()=>{this.scheduleLightDomReaction()}),this.lightDomObserver.observe(this,{childList:!0,subtree:!0,characterData:!0}))}unobserveLightDom(){this.lightDomObserver?.disconnect(),this.lightDomObserver=null,this.lightDomReactionScheduled=!1}scheduleLightDomReaction(){this.lightDomReactionScheduled||(this.lightDomReactionScheduled=!0,queueMicrotask(()=>{this.lightDomReactionScheduled=!1,this.isConnected&&(this.reportIconOnlyA11yIssue(),this.reportInvalidIconName(),this.requestUpdate())}))}reportInvalidIconName(){let t=this.getAttribute("icon");if(null===t||""===t||t_(t)){this.hasWarnedInvalidIconName=!1;return}this.hasWarnedInvalidIconName||(console.warn(`[smzh-button] Unknown icon "${t}". The icon attribute is ignored until it matches a registered name (see LucideIconName / src/shared/icons/lucide-icons.ts).`),this.hasWarnedInvalidIconName=!0)}reportIconOnlyA11yIssue(){let{isIconOnly:t}=this.getButtonVisualState(),e=this.resolveAriaLabel(),r="string"==typeof e&&e.trim().length>0;if(t&&!r){this.hasWarnedMissingIconOnlyAriaLabel||(console.warn("[smzh-button] Icon-only usage requires an accessible label. Provide a non-empty 'aria-label' attribute (or ariaLabel property)."),this.hasWarnedMissingIconOnlyAriaLabel=!0);return}this.hasWarnedMissingIconOnlyAriaLabel=!1}handleSlotChange(){this.reportIconOnlyA11yIssue(),this.requestUpdate()}render(){let t=this.resolveVariant(),e=this.resolveSize(),r=this.resolveShape(),i=this.resolveType(),a=this.resolveIconPosition(),{hasLeadingSlot:s,hasTrailingSlot:n,isIconOnly:o}=this.getButtonVisualState(),l=o?this.resolveAriaLabel():void 0,h=this.disabled||this.loading,c=this.isFullWidthActive();return W`
      <button
        class="button"
        type=${i}
        aria-label=${l??Z}
        aria-busy=${this.loading?"true":"false"}
        ?disabled=${h}
        data-variant=${t}
        data-size=${e}
        data-shape=${r}
        data-inverse=${this.inverse?"true":"false"}
        data-icon-only=${o?"true":"false"}
        data-full-width=${c?"true":"false"}
      >
        ${o||"leading"===a?this.renderIconSlot("icon-leading",s):Z}
        <span class="text" data-hidden=${o?"true":"false"}
          ><slot @slotchange=${this.handleSlotChange}></slot
        ></span>
        ${!o&&"trailing"===a?this.renderIconSlot("icon-trailing",n):Z}
      </button>
    `}});let tA=l`
  :host {
    display: block;
    width: 100%;
    box-sizing: border-box;
    /* Override on the host, e.g. style="--smzh-calculator-shell-min-height: auto" */
    --smzh-calculator-shell-min-height: min(100vh, 720px);
  }

  *,
  *::before,
  *::after {
    box-sizing: inherit;
  }

  .shell {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--smzh-spacing-x-big);
    min-height: var(--smzh-calculator-shell-min-height);
    padding: var(--smzh-spacing-lg) var(--smzh-spacing-x-lg);
    align-items: stretch;
  }

  .panel {
    min-width: 0;
  }

  .panel--left {
    padding: var(--smzh-spacing-md) var(--smzh-spacing-x-big) 0 0;
  }

  .panel--right {
    background: var(--smzh-color-background-subtle);
    border: 1px solid var(--smzh-color-border-default);
    border-radius: 16px;
    padding: var(--smzh-spacing-lg);
    display: flex;
    flex-direction: column;
    align-items: stretch;
    justify-content: center;
  }

  /*
   * Tablet / mobile: one column, right slot first (flex + order is reliable; grid+order is flaky).
   * max-width uses host token so it stays overridable; literal 900px avoids var()-in-@media issues.
   */
  @media (max-width: 900px) {
    .shell {
      display: flex;
      flex-direction: column;
      gap: var(--smzh-spacing-x-big);
      min-height: auto;
      padding: var(--smzh-spacing-x-big) var(--smzh-spacing-md);
    }

    .panel--right {
      order: 1;
    }

    .panel--left {
      order: 2;
      padding: 0;
    }
  }
`;"u">typeof window&&!customElements.get("smzh-calculator-layout")&&customElements.define("smzh-calculator-layout",class extends tp{static styles=tA;render(){return W`
      <div class="shell" part="shell">
        <div class="panel panel--left" part="left-panel">
          <slot name="left"></slot>
        </div>
        <div class="panel panel--right" part="right-panel">
          <slot name="right"></slot>
        </div>
      </div>
    `}});let{I:tM}={M:M,P:C,A:E,C:1,L:tt,R:ti,D:R,V:tr,I:ta,H:ts,N:to,U:tl,B:tn,F:th};class tC{constructor(t){}get _$AU(){return this._$AM._$AU}_$AT(t,e,r){this._$Ct=t,this._$AM=e,this._$Ci=r}_$AS(t,e){return this.update(t,e)}update(t,e){return this.render(...e)}}let tE=(t,e)=>{let r=t._$AN;if(void 0===r)return!1;for(let t of r)t._$AO?.(e,!1),tE(t,e);return!0},tT=t=>{let e,r;do{if(void 0===(e=t._$AM))break;(r=e._$AN).delete(t),t=e}while(0===r?.size)},tN=t=>{for(let e;e=t._$AM;t=e){let r=e._$AN;if(void 0===r)e._$AN=r=new Set;else if(r.has(t))break;r.add(t),tL(e)}};function tI(t){void 0!==this._$AN?(tT(this),this._$AM=t,tN(this)):this._$AM=t}function tP(t,e=!1,r=0){let i=this._$AH,a=this._$AN;if(void 0!==a&&0!==a.size)if(e)if(Array.isArray(i))for(let t=r;t<i.length;t++)tE(i[t],!1),tT(i[t]);else null!=i&&(tE(i,!1),tT(i));else tE(this,t)}let tL=t=>{2==t.type&&(t._$AP??=tP,t._$AQ??=tI)};class tR extends tC{constructor(){super(...arguments),this._$AN=void 0}_$AT(t,e,r){super._$AT(t,e,r),tN(this),this.isConnected=t._$AU}_$AO(t,e=!0){t!==this.isConnected&&(this.isConnected=t,t?this.reconnected?.():this.disconnected?.()),e&&(tE(this,t),tT(this))}setValue(t){if(void 0===this._$Ct.strings)this._$Ct._$AI(t,this);else{let e=[...this._$Ct._$AH];e[this._$Ci]=t,this._$Ct._$AI(e,this,0)}}disconnected(){}reconnected(){}}class tD{}let tF=new WeakMap,tj=(e=class extends tR{render(t){return Z}update(t,[e]){let r=e!==this.G;return r&&void 0!==this.G&&this.rt(void 0),(r||this.lt!==this.ct)&&(this.G=e,this.ht=t.options?.host,this.rt(this.ct=t.element)),Z}rt(t){if(this.isConnected||(t=void 0),"function"==typeof this.G){let e=this.ht??globalThis,r=tF.get(e);void 0===r&&(r=new WeakMap,tF.set(e,r)),void 0!==r.get(this.G)&&this.G.call(this.ht,void 0),r.set(this.G,t),void 0!==t&&this.G.call(this.ht,t)}else this.G.value=t}get lt(){return"function"==typeof this.G?tF.get(this.ht??globalThis)?.get(this.G):this.G?.value}disconnected(){this.lt===this.ct&&this.rt(void 0)}reconnected(){this.rt(this.ct)}},(...t)=>({_$litDirective$:e,values:t})),tH=l`
  :host {
    --smzh-input-control-gap: var(--smzh-spacing-xxx-sm);
    --smzh-input-control-padding-block: var(--smzh-spacing-x-sm);
    --smzh-input-control-padding-inline: var(--smzh-spacing-md);
    --smzh-input-control-radius: 8px;
    --smzh-input-icon-size: var(--smzh-spacing-big);
    --smzh-input-label-offset: calc(var(--smzh-spacing-xxx-sm) / 2);

    display: block;
    width: 100%;
  }

  :host([hidden]) {
    display: none !important;
  }

  .root {
    display: flex;
    flex-direction: column;
    gap: var(--smzh-input-control-gap);
    width: 100%;
  }

  .label-row {
    align-items: center;
    display: flex;
    flex-wrap: wrap;
    gap: var(--smzh-input-control-gap);
    justify-content: flex-start;
    padding-left: var(--smzh-input-label-offset);
    width: 100%;
  }

  .label {
    color: var(--smzh-input-label-color, var(--smzh-color-text-form-label));
    cursor: default;
    flex: 0 1 auto;
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-sm-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-medium);
    letter-spacing: var(--smzh-typography-text-sm-letter-spacing);
    line-height: var(--smzh-typography-text-sm-line-height);
    min-width: 0;
  }

  .label-end {
    align-items: center;
    display: flex;
    flex: 0 0 auto;
    min-height: var(--smzh-typography-text-sm-line-height);
  }

  .label-end ::slotted(*) {
    align-items: center;
    display: inline-flex;
    justify-content: center;
  }

  .label-end ::slotted(button) {
    line-height: 1;
  }

  .hint {
    color: var(--smzh-input-hint-color, var(--smzh-color-text-input-soft));
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-sm-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    letter-spacing: var(--smzh-typography-text-sm-letter-spacing);
    line-height: var(--smzh-typography-text-sm-line-height);
    margin: 0;
    width: 100%;
  }

  :host([destructive]) .hint {
    color: var(
      --smzh-input-hint-color-destructive,
      var(--smzh-color-text-form-hint-error)
    );
  }

  .control {
    align-items: center;
    background: var(--smzh-color-surface);
    border: 1px solid var(--smzh-color-border-default);
    border-radius: var(--smzh-input-control-radius);
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    gap: var(--smzh-input-control-gap);
    min-height: calc(
      var(--smzh-typography-text-sm-line-height) + 2 *
        var(--smzh-input-control-padding-block)
    );
    min-width: 0;
    padding: var(--smzh-input-control-padding-block)
      var(--smzh-input-control-padding-inline);
    transition:
      border-color 140ms ease,
      background-color 140ms ease,
      box-shadow 140ms ease;
    width: 100%;
  }

  .control[data-variant="filled"] {
    background: var(--smzh-color-background-subtle);
  }

  :host([disabled]) .control {
    cursor: not-allowed;
    background: var(--smzh-color-input-disabled-surface);
  }

  :host([destructive]) .control {
    border-color: var(--smzh-color-border-error-subtle);
  }

  :host(:not([readonly])) .control:focus-within {
    border-color: var(--smzh-color-border-focus-subtle);
    box-shadow: 0 0 0 4px var(--smzh-color-input-focus-ring);
    outline: none;
  }

  :host([destructive]:not([readonly])) .control:focus-within {
    border-color: var(--smzh-color-border-error-subtle);
    box-shadow: 0 0 0 4px var(--smzh-color-input-error-focus-ring);
  }

  .prefix {
    align-items: center;
    color: var(
      --smzh-input-adornment-color-empty,
      var(--smzh-color-text-input-soft)
    );
    display: none;
    flex: 0 0 auto;
    gap: var(--smzh-input-control-gap);
  }

  :host([has-prefix]) .prefix {
    display: inline-flex;
  }

  .input {
    background: transparent;
    border: none;
    box-sizing: border-box;
    color: var(--smzh-input-value-color, var(--smzh-color-text-form-value));
    flex: 1 1 auto;
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-sm-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    letter-spacing: var(--smzh-typography-text-sm-letter-spacing);
    line-height: var(--smzh-typography-text-sm-line-height);
    margin: 0;
    min-width: 0;
    outline: none;
    padding: 0;
    width: 100%;
  }

  .input::placeholder {
    color: var(
      --smzh-input-placeholder-color,
      var(--smzh-color-text-input-soft)
    );
  }

  /* Hide native number spinners (WebKit/Blink/Firefox); optional stepper adds custom controls */
  .input::-webkit-outer-spin-button,
  .input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }

  .input[type="number"] {
    appearance: textfield;
    -moz-appearance: textfield;
  }

  .input:disabled {
    cursor: not-allowed;
  }

  .control[data-variant="filled"] .input {
    color: var(--smzh-input-value-color, var(--smzh-color-text-form-value));
  }

  :host([disabled]) .input {
    color: var(
      --smzh-input-disabled-value-color,
      var(--smzh-color-text-input-soft)
    );
  }

  :host([readonly]) .input {
    color: var(
      --smzh-input-readonly-value-color,
      var(--smzh-color-text-subtle)
    );
    cursor: default;
  }

  .suffix {
    color: var(
      --smzh-input-suffix-color-empty,
      var(--smzh-input-adornment-color-empty, var(--smzh-color-text-input-soft))
    );
    flex: 0 0 auto;
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-sm-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    letter-spacing: var(--smzh-typography-text-sm-letter-spacing);
    line-height: var(--smzh-typography-text-sm-line-height);
    white-space: nowrap;
  }

  .control[data-has-value="true"] .prefix,
  .control[data-has-value="true"] .trailing {
    color: var(--smzh-input-adornment-color, var(--smzh-color-text-form-value));
  }

  .control[data-has-value="true"] .suffix {
    color: var(
      --smzh-input-suffix-color,
      var(--smzh-input-adornment-color, var(--smzh-color-text-form-value))
    );
  }

  :host([disabled]) .suffix {
    color: var(
      --smzh-input-disabled-value-color,
      var(--smzh-color-text-input-soft)
    );
  }

  :host([disabled]) .prefix,
  :host([disabled]) .trailing {
    color: var(
      --smzh-input-disabled-value-color,
      var(--smzh-color-text-input-soft)
    );
  }

  :host([readonly]) .suffix {
    color: var(
      --smzh-input-readonly-value-color,
      var(--smzh-color-text-input-soft)
    );
  }

  :host([readonly]) .prefix,
  :host([readonly]) .trailing {
    color: var(
      --smzh-input-readonly-value-color,
      var(--smzh-color-text-input-soft)
    );
  }

  .stepper-wrap {
    flex: 0 0 auto;
    position: relative;
    height: var(--smzh-spacing-big);
    width: var(--smzh-spacing-big);
  }

  .stepper-icon {
    align-items: center;
    color: var(
      --smzh-input-stepper-icon-color,
      var(--smzh-input-value-color, var(--smzh-color-text-form-value))
    );
    display: flex;
    inset: 0;
    justify-content: center;
    pointer-events: none;
    position: absolute;
  }

  .stepper-icon svg {
    display: block;
  }

  .stepper-actions {
    display: flex;
    flex-direction: column;
    height: 100%;
    position: relative;
    width: 100%;
    z-index: 1;
  }

  .step-btn {
    background: transparent;
    border: none;
    cursor: pointer;
    flex: 1 1 50%;
    margin: 0;
    min-height: 0;
    padding: 0;
  }

  .step-btn:focus-visible {
    outline: 2px solid var(--smzh-color-border-focus);
    outline-offset: 1px;
  }

  :host([readonly]) .stepper-icon {
    color: var(
      --smzh-input-stepper-icon-color,
      var(--smzh-input-readonly-value-color, var(--smzh-color-text-subtle))
    );
  }

  :host([disabled]) .step-btn {
    cursor: not-allowed;
    pointer-events: none;
  }

  .trailing {
    align-items: center;
    color: var(
      --smzh-input-adornment-color-empty,
      var(--smzh-color-text-input-soft)
    );
    display: none;
    flex: 0 0 auto;
  }

  :host([has-trailing]) .trailing {
    display: inline-flex;
  }

  .trailing ::slotted(*) {
    display: flex;
  }

  .prefix ::slotted(svg),
  .trailing ::slotted(svg) {
    height: var(--smzh-input-icon-size);
    width: var(--smzh-input-icon-size);
  }
`,tO=["default","filled"],tB=tO[0];function tq(t){return"string"==typeof t&&tO.includes(t)}let tU=["text","tel","number"],tV=["text","tel","numeric"],tW=["de-CH","en-US","de-DE","plain"];function tG(t){return"string"==typeof t&&tV.includes(t)}function tX(t){return"string"==typeof t&&tW.includes(t)}let tY="text";class tZ extends tp{static styles=tH;inputRef=new tD;inputId=`smzh-input-${Math.random().toString(36).slice(2,10)}`;hintId=`smzh-input-hint-${Math.random().toString(36).slice(2,10)}`;static properties={label:{type:String},hint:{type:String},value:{type:String},placeholder:{type:String},ariaLabel:{type:String,attribute:"aria-label"},type:{type:String},name:{type:String,reflect:!0},autocomplete:{type:String},inputmode:{type:String},amountFormat:{type:String,attribute:"amount-format"},disabled:{type:Boolean,reflect:!0},readonly:{type:Boolean,reflect:!0},variant:{type:String,reflect:!0},suffix:{type:String},stepper:{type:Boolean,reflect:!0},step:{type:String},min:{type:String},max:{type:String},pattern:{type:String},maxlength:{type:String},digitsOnly:{type:Boolean,reflect:!0,attribute:"digits-only"},destructive:{type:Boolean,reflect:!0},hasPrefix:{type:Boolean,reflect:!0,attribute:"has-prefix"},hasTrailing:{type:Boolean,reflect:!0,attribute:"has-trailing"}};constructor(){super(),this.label="",this.hint="",this.value="",this.placeholder="",this.ariaLabel=null,this.type=tY,this.name="",this.autocomplete="",this.inputmode=void 0,this.amountFormat=void 0,this.disabled=!1,this.readonly=!1,this.variant=tB,this.suffix="",this.stepper=!1,this.step="",this.min="",this.max="",this.pattern="",this.maxlength="",this.digitsOnly=!1,this.destructive=!1,this.hasPrefix=!1,this.hasTrailing=!1}firstUpdated(){this.syncSlotFlags()}slotHasContent(t){return!!t&&t.assignedNodes({flatten:!0}).some(t=>t.nodeType===Node.TEXT_NODE?!!t.textContent?.trim():t.nodeType===Node.ELEMENT_NODE)}syncSlotFlags(){let t=this.renderRoot.querySelector('slot[name="prefix"]'),e=this.renderRoot.querySelector('slot[name="trailing"]');this.hasPrefix=this.slotHasContent(t),this.hasTrailing=this.slotHasContent(e)}handleSlotChange=()=>{this.syncSlotFlags()};updated(t){if(super.updated(t),this.shouldFormatAsAmount()&&(t.has("value")||t.has("amountFormat")||t.has("type")||t.has("stepper"))){let t=this.getFormattedValue(this.value??"");if(t!==(this.value??"")){this.value=t;return}}if(t.has("value")||t.has("amountFormat")||t.has("type")||t.has("stepper")){let t=this.inputRef.value,e=this.getFormattedValue(this.value??"");t&&t.value!==e&&(t.value=e)}}resolveAmountFormat(){return tX(this.amountFormat)?this.amountFormat:void 0}shouldFormatAsAmount(){return"text"===this.resolveInputType()&&void 0!==this.resolveAmountFormat()}stripAmountSeparators(t){return t.replace(/[\s,.'’]/g,"")}limitDigitsByMaxlength(t){let e=this.maxlength?.trim();if(!e)return t;let r=Number.parseInt(e,10);return Number.isFinite(r)?t.slice(0,r):t}formatAmountDigits(t,e){if(!t)return"";let r=this.limitDigitsByMaxlength(t.replace(/\D/g,""));return r?"plain"===e?r:Number(r).toLocaleString(e):""}getFormattedValue(t){let e=this.resolveAmountFormat();return e&&"number"!==this.resolveInputType()?this.formatAmountDigits(t,e):t}setCursorFromDigitIndex(t,e){let r=t.value;if(!r||e<=0)return void t.setSelectionRange(0,0);let i=0;for(let a=0;a<r.length;a+=1)if(/\d/.test(r[a])&&(i+=1)>=e){let e=a+1;t.setSelectionRange(e,e);return}let a=r.length;t.setSelectionRange(a,a)}resolveVariant(){return tq(this.variant)?this.variant:tB}resolveAriaLabel(t){if(t)return;let e=this.ariaLabel?.trim();return e||this.getAttribute("aria-label")?.trim()||void 0}resolveInputType(){var t;return this.stepper?"number":"string"==typeof(t=this.type)&&tU.includes(t)?this.type:tY}handleInput=t=>{t.stopPropagation();let e=t.target,r=e.value,i=this.resolveAmountFormat();if(this.shouldFormatAsAmount()&&!this.disabled&&!this.readonly&&i){let t=e.selectionStart??r.length,a=r.slice(0,t).replace(/\D/g,"").length,s=this.formatAmountDigits(this.stripAmountSeparators(r),i);s!==r&&(e.value=s,queueMicrotask(()=>{this.setCursorFromDigitIndex(e,Math.min(a,this.limitDigitsByMaxlength(this.stripAmountSeparators(r)).length))})),this.value=s,this.dispatchEvent(new Event("input",{bubbles:!0,composed:!0}));return}if(this.digitsOnly&&!this.disabled&&!this.readonly&&"number"!==this.resolveInputType()){let t=e.selectionStart??r.length,i=r.slice(0,t).replace(/\D/g,"").length,a=r.replace(/\D/g,""),s=this.maxlength?.trim();if(s){let t=Number.parseInt(s,10);Number.isFinite(t)&&(a=a.slice(0,t))}if(a!==r){e.value=a,this.value=a;let t=Math.min(i,a.length);queueMicrotask(()=>{e.setSelectionRange(t,t)}),this.dispatchEvent(new Event("input",{bubbles:!0,composed:!0}));return}}this.value=r,this.dispatchEvent(new Event("input",{bubbles:!0,composed:!0}))};handleStep=t=>{if(this.disabled||this.readonly)return;let e=this.inputRef.value;if(!e||"number"!==this.resolveInputType())return;let r=e.value;t>0?e.stepUp():e.stepDown(),e.value!==r&&(this.value=e.value,this.dispatchEvent(new Event("input",{bubbles:!0,composed:!0})),this.dispatchEvent(new Event("change",{bubbles:!0,composed:!0})))};render(){let t=this.resolveVariant(),e=this.resolveInputType(),r=this.shouldFormatAsAmount(),i=this.suffix?.trim()??"",a=i.length>0,s=this.label?.trim()??"",n=s.length>0,o=this.hint?.trim()??"",l=o.length>0,h=this.resolveAriaLabel(n);return W`
      <div class="root" part="root">
        ${n?W`
              <div class="label-row" part="label-row">
                <label for=${this.inputId} class="label" part="label"
                  >${s}</label
                >
                <span class="label-end" part="label-end">
                  <slot name="label-end"></slot>
                </span>
              </div>
            `:Z}
        <div
          class="control"
          part="control"
          data-variant=${t}
          data-has-value=${this.value?"true":"false"}
        >
          <span class="prefix" part="prefix">
            <slot name="prefix" @slotchange=${this.handleSlotChange}></slot>
          </span>
          <input
            ${tj(this.inputRef)}
            id=${this.inputId}
            class="input"
            part="input"
            type=${e}
            .value=${this.getFormattedValue(this.value??"")}
            placeholder=${this.placeholder??""}
            name=${(this.name?.trim()?this.name:void 0)??Z}
            autocomplete=${(this.autocomplete?.trim()?this.autocomplete:void 0)??Z}
            inputmode=${(tG(this.inputmode)?this.inputmode:void 0)??Z}
            ?disabled=${this.disabled}
            ?readonly=${this.readonly}
            step=${(this.step?.trim()?this.step:void 0)??Z}
            min=${(this.min?.trim()?this.min:void 0)??Z}
            max=${(this.max?.trim()?this.max:void 0)??Z}
            pattern=${(this.pattern?.trim()?this.pattern:void 0)??Z}
            maxlength=${(!r&&this.maxlength?.trim()?this.maxlength:void 0)??Z}
            aria-label=${h??Z}
            aria-describedby=${(l?this.hintId:void 0)??Z}
            @input=${this.handleInput}
          />
          ${a?W`<span class="suffix" part="suffix">${i}</span>`:Z}
          ${this.stepper?W`
                <div class="stepper-wrap" part="stepper">
                  <span class="stepper-icon" aria-hidden="true">
                    ${tS["chevrons-up-down"](void 0)}
                  </span>
                  <div class="stepper-actions">
                    <button
                      type="button"
                      class="step-btn"
                      part="step-up"
                      aria-label="Increase value"
                      ?disabled=${this.disabled||this.readonly}
                      @click=${()=>this.handleStep(1)}
                    ></button>
                    <button
                      type="button"
                      class="step-btn"
                      part="step-down"
                      aria-label="Decrease value"
                      ?disabled=${this.disabled||this.readonly}
                      @click=${()=>this.handleStep(-1)}
                    ></button>
                  </div>
                </div>
              `:Z}
          <span class="trailing" part="trailing">
            <slot name="trailing" @slotchange=${this.handleSlotChange}></slot>
          </span>
        </div>
        ${l?W`<p id=${this.hintId} class="hint" part="hint">${o}</p>`:Z}
      </div>
    `}}"u">typeof window&&!customElements.get("smzh-input")&&customElements.define("smzh-input",tZ);let tK=l`
  :host {
    display: inline-flex;
    font-family: var(--smzh-font-family-sans);
    vertical-align: top;
    /* Foundation defaults; override on :host to theme without piercing shadow. */
    --smzh-tooltip-max-width: 220px;
    --smzh-tooltip-border-radius: var(--smzh-spacing-xxx-sm);
    --smzh-tooltip-padding-y: var(--smzh-spacing-xxx-sm);
    --smzh-tooltip-padding-x: var(--smzh-spacing-x-sm);
    --smzh-tooltip-arrow-span: var(--smzh-spacing-x-sm);
    --smzh-tooltip-arrow-depth: 6px;
    --smzh-tooltip-arrow-half-span: calc(var(--smzh-tooltip-arrow-span) / 2);
    --smzh-tooltip-arrow-overlap: 1px;
    /* Offset between trigger and bubble; matches Foundation arrow depth (6px). */
    --smzh-tooltip-gap: 6px;
    --smzh-tooltip-z-index: 20;
    /* Fallback if .surface mode classes are missing; light mode overrides on .surface.mode-light */
    --smzh-tooltip-arrow-fill: var(--smzh-color-tooltip-surface-dark);
  }

  :host([hidden]) {
    display: none !important;
  }

  .wrap {
    position: relative;
    display: inline-flex;
    align-items: center;
    box-sizing: border-box;
  }

  .trigger-wrap {
    display: inline-flex;
    align-items: center;
    box-sizing: border-box;
  }

  /* Static layout (no trigger): bubble stays in normal flow so the host sizes correctly. */
  :host(:not([data-has-trigger])) .wrap {
    position: static;
  }

  :host(:not([data-has-trigger])) .surface {
    position: static;
    z-index: auto;
    max-width: var(--smzh-tooltip-max-width);
    pointer-events: auto;
  }

  /* Interactive: absolutely position the bubble relative to the trigger. */
  :host([data-has-trigger]) .surface {
    position: absolute;
    z-index: var(--smzh-tooltip-z-index);
    pointer-events: none;
    width: max-content;
    inline-size: max-content;
    max-width: ${o("min(var(--smzh-tooltip-max-width), 70vw)")};
    max-inline-size: ${o("min(var(--smzh-tooltip-max-width), 70vw)")};
    white-space: normal;
    box-sizing: border-box;
  }

  :host([data-has-trigger][placement="top"]) .surface {
    bottom: calc(100% + var(--smzh-tooltip-gap));
    left: 50%;
    top: auto;
    right: auto;
    translate: -50% 0;
  }

  :host([data-has-trigger][placement="bottom"]) .surface {
    top: calc(100% + var(--smzh-tooltip-gap));
    left: 50%;
    bottom: auto;
    right: auto;
    translate: -50% 0;
  }

  :host([data-has-trigger][placement="left"]) .surface {
    right: calc(100% + var(--smzh-tooltip-gap));
    top: 50%;
    left: auto;
    bottom: auto;
    translate: 0 -50%;
  }

  :host([data-has-trigger][placement="right"]) .surface {
    left: calc(100% + var(--smzh-tooltip-gap));
    top: 50%;
    right: auto;
    bottom: auto;
    translate: 0 -50%;
  }

  .surface {
    display: inline-flex;
    align-items: center;
    box-sizing: border-box;
    gap: 0;
  }

  /* Closed state must win over display:inline-flex on .surface (use unsafeCSS: Lit css treats [ as binding). */
  ${o(".surface[hidden]")} {
    display: none !important;
  }

  .surface.is-column {
    flex-direction: column;
  }

  .surface.is-row {
    flex-direction: row;
  }

  .surface.mode-dark {
    filter: drop-shadow(var(--smzh-shadow-tooltip-filter));
  }

  .body {
    box-sizing: border-box;
    max-width: var(--smzh-tooltip-max-width);
    border-radius: var(--smzh-tooltip-border-radius);
    padding: var(--smzh-tooltip-padding-y) var(--smzh-tooltip-padding-x);
    text-align: center;
  }

  .surface.mode-dark .body {
    color: var(--smzh-color-tooltip-text-on-dark);
    background: var(--smzh-color-tooltip-surface-dark);
    box-shadow: none;
  }

  .surface.mode-light {
    --smzh-tooltip-arrow-fill: var(--smzh-color-tooltip-surface-light);
  }

  .surface.mode-light .body {
    color: var(--smzh-color-tooltip-text-on-light);
    background: var(--smzh-color-tooltip-surface-light);
    box-shadow: none;
  }

  .surface.mode-hint {
    --smzh-tooltip-arrow-fill: var(--smzh-color-border-default);
    --smzh-tooltip-arrow-span: 10.392px;
    --smzh-tooltip-arrow-depth: 9px;
    --smzh-tooltip-arrow-overlap: 0px;
    filter: none;
  }

  .surface.mode-hint .body {
    color: var(--smzh-color-tile-title);
    background: var(--smzh-color-background);
    border: 1px solid var(--smzh-color-border-default);
    border-radius: var(--smzh-spacing-xxx-sm);
    padding: var(--smzh-spacing-xx-sm) 15px;
    text-align: left;
    box-shadow: var(--smzh-color-tooltip-hint-shadow);
  }

  .body-inner {
    font-size: var(--smzh-typography-text-xs-font-size);
    line-height: var(--smzh-typography-text-xs-line-height);
    letter-spacing: var(--smzh-typography-text-xs-letter-spacing);
    font-weight: var(--smzh-font-weight-medium);
    word-wrap: break-word;
    overflow-wrap: anywhere;
  }

  .surface.mode-hint .body-inner {
    font-weight: var(--smzh-font-weight-normal);
  }

  .arrow {
    flex-shrink: 0;
    display: flex;
    box-sizing: border-box;
    pointer-events: none;
    line-height: 0;
  }

  .surface.placement-top .arrow,
  .surface.placement-bottom .arrow {
    width: var(--smzh-tooltip-arrow-span);
    height: var(--smzh-tooltip-arrow-depth);
    justify-content: center;
  }

  .surface.placement-top .arrow {
    align-items: flex-end;
    margin-bottom: calc(-1 * var(--smzh-tooltip-arrow-overlap));
  }

  .surface.placement-bottom .arrow {
    align-items: flex-start;
    margin-top: calc(-1 * var(--smzh-tooltip-arrow-overlap));
  }

  .surface.placement-left .arrow,
  .surface.placement-right .arrow {
    width: var(--smzh-tooltip-arrow-depth);
    height: var(--smzh-tooltip-arrow-span);
    align-items: center;
  }

  .surface.placement-left .arrow {
    justify-content: flex-end;
    margin-right: calc(-1 * var(--smzh-tooltip-arrow-overlap));
  }

  .surface.placement-right .arrow {
    justify-content: flex-start;
    margin-left: calc(-1 * var(--smzh-tooltip-arrow-overlap));
  }

  .arrow-inner {
    width: 0;
    height: 0;
    border-style: solid;
    border-color: transparent;
  }

  .surface.placement-bottom .arrow-inner {
    border-width: var(--smzh-tooltip-arrow-depth)
      var(--smzh-tooltip-arrow-half-span) 0 var(--smzh-tooltip-arrow-half-span);
    border-top-color: var(--smzh-tooltip-arrow-fill);
    margin-top: 0;
  }

  .surface.placement-top .arrow-inner {
    border-width: 0 var(--smzh-tooltip-arrow-half-span)
      var(--smzh-tooltip-arrow-depth) var(--smzh-tooltip-arrow-half-span);
    border-bottom-color: var(--smzh-tooltip-arrow-fill);
  }

  .surface.placement-left .arrow-inner {
    border-width: var(--smzh-tooltip-arrow-half-span)
      var(--smzh-tooltip-arrow-depth) var(--smzh-tooltip-arrow-half-span) 0;
    border-right-color: var(--smzh-tooltip-arrow-fill);
  }

  .surface.placement-right .arrow-inner {
    border-width: var(--smzh-tooltip-arrow-half-span) 0
      var(--smzh-tooltip-arrow-half-span) var(--smzh-tooltip-arrow-depth);
    border-left-color: var(--smzh-tooltip-arrow-fill);
  }
`,tJ=["top","bottom","left","right"],tQ=tJ[1],t0=["dark","light","hint"],t1=t0[0];function t2(t){return"string"==typeof t&&tJ.includes(t)}function t4(t){return"string"==typeof t&&t0.includes(t)}let t3="smzh-tooltip-default-slot",t5=tJ.map(t=>`'${t}'`).join(" | "),t8=t0.map(t=>`'${t}'`).join(" | ");class t6 extends tp{static nextTooltipSurfaceId=0;lastWarnedPlacement=null;lastWarnedMode=null;hasWarnedEmptyDefaultSlot=!1;generatedTooltipId="";isOpen=!1;static styles=tK;static properties={placement:{type:String,reflect:!0},mode:{type:String,reflect:!0},tooltipId:{type:String,attribute:"tooltip-id",reflect:!0}};constructor(){super(),this.placement=tQ,this.mode=t1,this.tooltipId=void 0,this.generatedTooltipId=`smzh-tt-${t6.nextTooltipSurfaceId++}`}get effectiveTooltipId(){let t=this.tooltipId?.trim();return t&&t.length>0?t:this.generatedTooltipId}isTriggerSlottable(t){return t.nodeType===Node.ELEMENT_NODE&&("trigger"===t.slot||"trigger"===t.getAttribute("slot"))}hasTriggerSlotContent(){if([...this.children].some(t=>this.isTriggerSlottable(t)))return!0;let t=this.renderRoot?.querySelector('slot[name="trigger"]');return(t?.assignedElements().length??0)>0}getTriggerElement(){let t=this.renderRoot?.querySelector('slot[name="trigger"]')?.assignedElements()[0];return t||[...this.children].find(t=>this.isTriggerSlottable(t))}get bubbleVisible(){return!this.hasTriggerSlotContent()||this.isOpen}setOpen(t){this.isOpen!==t&&(this.isOpen=t,this.requestUpdate())}handleMouseEnter=()=>{this.hasTriggerSlotContent()&&this.setOpen(!0)};handleMouseLeave=()=>{!this.hasTriggerSlotContent()||this.matches(":focus-within")||this.setOpen(!1)};handleFocusIn=()=>{this.hasTriggerSlotContent()&&this.setOpen(!0)};handleFocusOut=t=>{if(!this.hasTriggerSlotContent())return;let e=t.relatedTarget;e instanceof Node&&this.contains(e)||this.setOpen(!1)};handleTriggerSlotChange=()=>{this.hasTriggerSlotContent()&&this.setOpen(!1),this.requestUpdate()};syncAccessibility(){let t=this.getTriggerElement();t instanceof Element&&this.hasTriggerSlotContent()&&(this.bubbleVisible?t.setAttribute("aria-describedby",this.effectiveTooltipId):t.removeAttribute("aria-describedby"))}reportContractIssues(){let t=this.placement;"string"==typeof t&&t.length>0&&!t2(t)?(this.lastWarnedPlacement!==t&&console.warn(`[smzh-tooltip] Invalid placement '${t}'. Allowed: ${t5}.`),this.lastWarnedPlacement=t):this.lastWarnedPlacement=null;let e=this.mode;"string"==typeof e&&e.length>0&&!t4(e)?(this.lastWarnedMode!==e&&console.warn(`[smzh-tooltip] Invalid mode '${e}'. Allowed: ${t8}.`),this.lastWarnedMode=e):this.lastWarnedMode=null}handleDefaultSlotChange(t){let e=t.target;e instanceof HTMLSlotElement&&this.updateDefaultSlotWarning(e)}updateDefaultSlotWarning(t){t.assignedNodes({flatten:!0}).some(t=>t.nodeType===Node.TEXT_NODE?(t.textContent??"").trim().length>0:t.nodeType===Node.ELEMENT_NODE)?this.hasWarnedEmptyDefaultSlot=!1:this.hasWarnedEmptyDefaultSlot||(console.warn("[smzh-tooltip] Default slot has no visible content. Add text or elements as children of <smzh-tooltip>."),this.hasWarnedEmptyDefaultSlot=!0)}resolvePlacement(){return t2(this.placement)?this.placement:tQ}resolveMode(){return t4(this.mode)?this.mode:t1}willUpdate(t){super.willUpdate(t),this.toggleAttribute("data-has-trigger",this.hasTriggerSlotContent())}firstUpdated(t){super.firstUpdated(t),this.reportContractIssues();let e=this.renderRoot?.querySelector(`#${t3}`);e instanceof HTMLSlotElement&&this.updateDefaultSlotWarning(e),this.syncAccessibility()}updated(t){(t.has("placement")||t.has("mode"))&&this.reportContractIssues(),this.syncAccessibility()}render(){let t=function(t){switch(t){case"top":return"bottom";case"bottom":return"top";case"left":return"right";case"right":return"left"}}(this.resolvePlacement()),e=this.resolveMode(),r=W`
      <div class="arrow" part="arrow" aria-hidden="true">
        <div class="arrow-inner"></div>
      </div>
    `,i=W`
      <div class="body" part="content">
        <div class="body-inner">
          <slot
            id=${t3}
            @slotchange=${this.handleDefaultSlotChange}
          ></slot>
        </div>
      </div>
    `,a=W`
      <div
        class="surface mode-${e} placement-${t} ${"top"===t||"bottom"===t?"is-column":"is-row"}"
        id=${this.effectiveTooltipId}
        role="tooltip"
        ?hidden=${!this.bubbleVisible}
      >
        ${"top"===t||"left"===t?W`${r}${i}`:W`${i}${r}`}
      </div>
    `;return W`
      <div
        class="wrap"
        @mouseenter=${this.handleMouseEnter}
        @mouseleave=${this.handleMouseLeave}
        @focusin=${this.handleFocusIn}
        @focusout=${this.handleFocusOut}
      >
        <span class="trigger-wrap">
          <slot
            name="trigger"
            @slotchange=${this.handleTriggerSlotChange}
          ></slot>
        </span>
        ${a}
      </div>
    `}}"u">typeof window&&!customElements.get("smzh-tooltip")&&customElements.define("smzh-tooltip",t6);let t9=l`
  :host {
    display: inline-flex;
  }

  .root {
    align-items: center;
    background: var(--smzh-color-background-subtle);
    border-radius: var(--smzh-spacing-xxx-sm);
    box-sizing: border-box;
    display: inline-flex;
    gap: var(--smzh-spacing-xxx-sm);
    padding: var(--smzh-spacing-xxx-sm);
  }

  .segment {
    background: var(--smzh-color-border-default);
    border-radius: var(--smzh-spacing-x-sm);
    height: 6px;
    width: 20px;
  }

  .segment[data-active="true"] {
    background: var(--smzh-color-primary-active);
    width: 30px;
  }
`;"u">typeof window&&!customElements.get("smzh-progress-indicator")&&customElements.define("smzh-progress-indicator",class extends tp{hasWarnedInvalidTotalSteps=!1;hasWarnedInvalidActiveStep=!1;static styles=t9;static properties={totalSteps:{type:Number,attribute:"total-steps",reflect:!0},activeStep:{type:Number,attribute:"active-step",reflect:!0},ariaLabel:{type:String,attribute:"aria-label"}};constructor(){super(),this.totalSteps=3,this.activeStep=1,this.ariaLabel=null}resolveTotalSteps(){let t=this.totalSteps;return"number"==typeof t&&Number.isInteger(t)&&t>=1?t:3}resolveActiveStep(t){let e=this.activeStep;return"number"==typeof e&&Number.isInteger(e)?e<1?1:e>t?t:e:Math.min(1,t)}resolveAriaLabel(){if("string"==typeof this.ariaLabel&&this.ariaLabel.trim().length>0)return this.ariaLabel.trim();let t=this.getAttribute("aria-label");return"string"==typeof t&&t.trim().length>0?t.trim():"Progress"}reportContractIssues(t){let e=this.totalSteps;"number"==typeof e&&Number.isInteger(e)&&e>=1?this.hasWarnedInvalidTotalSteps=!1:this.hasWarnedInvalidTotalSteps||(console.warn(`[smzh-progress-indicator] Invalid total-steps value "${e}". Expected an integer >= 1. Falling back to 3.`),this.hasWarnedInvalidTotalSteps=!0);let r=this.activeStep;"number"==typeof r&&Number.isInteger(r)?this.hasWarnedInvalidActiveStep=!1:this.hasWarnedInvalidActiveStep||(console.warn(`[smzh-progress-indicator] Invalid active-step value "${r}". Expected an integer. Falling back to a clamped default within 1..${t}.`),this.hasWarnedInvalidActiveStep=!0)}firstUpdated(t){super.firstUpdated(t),this.reportContractIssues(this.resolveTotalSteps())}updated(t){(t.has("totalSteps")||t.has("activeStep"))&&this.reportContractIssues(this.resolveTotalSteps())}render(){let t=this.resolveTotalSteps(),e=this.resolveActiveStep(t),r=this.resolveAriaLabel(),i=Array.from({length:t},(t,e)=>e+1);return W`
      <div
        class="root"
        role="progressbar"
        aria-label=${r??Z}
        aria-valuemin="1"
        aria-valuemax=${String(t)}
        aria-valuenow=${String(e)}
      >
        ${i.map(t=>W`<span
              class="segment"
              data-active=${t===e?"true":"false"}
            ></span>`)}
      </div>
    `}});let t7=l`
  :host {
    --smzh-select-control-padding-block: var(--smzh-spacing-x-sm);
    --smzh-select-control-padding-inline: var(--smzh-spacing-md);
    --smzh-select-control-radius: 8px;

    display: block;
    position: relative;
    width: 100%;
  }

  :host([hidden]) {
    display: none !important;
  }

  .shell {
    align-items: center;
    background: var(--smzh-select-surface, var(--smzh-color-surface));
    border: 1px solid
      var(--smzh-select-border-color, var(--smzh-color-border-default));
    border-radius: var(--smzh-select-control-radius);
    box-sizing: border-box;
    color: var(--smzh-select-value-color, var(--smzh-color-text-form-value));
    display: flex;
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-sm-font-size);
    font-style: normal;
    font-weight: var(
      --smzh-select-value-font-weight,
      var(--smzh-font-weight-normal)
    );
    letter-spacing: var(--smzh-typography-text-sm-letter-spacing);
    line-height: var(--smzh-typography-text-sm-line-height);
    min-height: calc(
      var(--smzh-typography-text-sm-line-height) + 2 *
        var(--smzh-select-control-padding-block)
    );
    min-width: 0;
    padding: var(--smzh-select-control-padding-block)
      var(--smzh-select-control-padding-inline);
    position: relative;
    transition:
      border-color 140ms ease,
      box-shadow 140ms ease;
    width: 100%;
  }

  .shell:focus-within {
    border-color: var(--smzh-color-border-focus-subtle);
    box-shadow: 0 0 0 4px var(--smzh-color-input-focus-ring);
    outline: none;
  }

  slot {
    display: block;
    flex: 1 1 auto;
    min-width: 0;
  }

  ::slotted(select) {
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    background: transparent;
    border: none;
    box-sizing: border-box;
    color: inherit;
    cursor: pointer;
    display: block;
    font-family: inherit;
    font-size: inherit;
    font-style: inherit;
    font-weight: inherit;
    letter-spacing: inherit;
    line-height: inherit;
    margin: 0;
    outline: none;
    padding: 0 calc(var(--smzh-spacing-big) + var(--smzh-spacing-xxx-sm)) 0 0;
    -webkit-text-fill-color: currentColor;
    width: 100%;
  }

  ::slotted(select:disabled) {
    color: var(
      --smzh-select-disabled-value-color,
      var(--smzh-color-text-disabled)
    );
    cursor: not-allowed;
    opacity: 0.65;
    -webkit-text-fill-color: currentColor;
  }

  .chevron {
    align-items: center;
    color: var(
      --smzh-select-chevron-color,
      var(--smzh-select-value-color, var(--smzh-color-text-form-value))
    );
    display: flex;
    inset: 0 0 0 auto;
    justify-content: center;
    margin: auto var(--smzh-spacing-x-sm) auto auto;
    pointer-events: none;
    position: absolute;
    width: var(--smzh-spacing-big);
  }

  .chevron svg {
    display: block;
  }
`;function et(){}function ee(t){return null==t?et:function(){return this.querySelector(t)}}function er(){return[]}function ei(t){return null==t?er:function(){return this.querySelectorAll(t)}}function ea(t){return function(){return this.matches(t)}}function es(t){return function(e){return e.matches(t)}}"u">typeof window&&!customElements.get("smzh-select")&&customElements.define("smzh-select",class extends tp{static styles=t7;render(){return W`
      <div class="shell" part="shell">
        <slot></slot>
        <span class="chevron" part="chevron" aria-hidden="true">
          ${tk()}
        </span>
      </div>
    `}});var en,eo,el,eh,ec,ed=Array.prototype.find;function ep(){return this.firstElementChild}var eu=Array.prototype.filter;function em(){return Array.from(this.children)}function eg(t){return Array(t.length)}function ef(t,e){this.ownerDocument=t.ownerDocument,this.namespaceURI=t.namespaceURI,this._next=null,this._parent=t,this.__data__=e}function ev(t,e,r,i,a,s){for(var n,o=0,l=e.length,h=s.length;o<h;++o)(n=e[o])?(n.__data__=s[o],i[o]=n):r[o]=new ef(t,s[o]);for(;o<l;++o)(n=e[o])&&(a[o]=n)}function ey(t,e,r,i,a,s,n){var o,l,h,c=new Map,d=e.length,p=s.length,u=Array(d);for(o=0;o<d;++o)(l=e[o])&&(u[o]=h=n.call(l,l.__data__,o,e)+"",c.has(h)?a[o]=l:c.set(h,l));for(o=0;o<p;++o)h=n.call(t,s[o],o,s)+"",(l=c.get(h))?(i[o]=l,l.__data__=s[o],c.delete(h)):r[o]=new ef(t,s[o]);for(o=0;o<d;++o)(l=e[o])&&c.get(u[o])===l&&(a[o]=l)}function eb(t){return t.__data__}function ez(t,e){return t<e?-1:t>e?1:t>=e?0:NaN}ef.prototype={constructor:ef,appendChild:function(t){return this._parent.insertBefore(t,this._next)},insertBefore:function(t,e){return this._parent.insertBefore(t,e)},querySelector:function(t){return this._parent.querySelector(t)},querySelectorAll:function(t){return this._parent.querySelectorAll(t)}};var ex="http://www.w3.org/1999/xhtml";let ew={svg:"http://www.w3.org/2000/svg",xhtml:ex,xlink:"http://www.w3.org/1999/xlink",xml:"http://www.w3.org/XML/1998/namespace",xmlns:"http://www.w3.org/2000/xmlns/"};function e$(t){var e=t+="",r=e.indexOf(":");return r>=0&&"xmlns"!==(e=t.slice(0,r))&&(t=t.slice(r+1)),ew.hasOwnProperty(e)?{space:ew[e],local:t}:t}function ek(t){return t.ownerDocument&&t.ownerDocument.defaultView||t.document&&t||t.defaultView}function eS(t,e){return t.style.getPropertyValue(e)||ek(t).getComputedStyle(t,null).getPropertyValue(e)}function e_(t){return t.trim().split(/^|\s+/)}function eA(t){return t.classList||new eM(t)}function eM(t){this._node=t,this._names=e_(t.getAttribute("class")||"")}function eC(t,e){for(var r=eA(t),i=-1,a=e.length;++i<a;)r.add(e[i])}function eE(t,e){for(var r=eA(t),i=-1,a=e.length;++i<a;)r.remove(e[i])}function eT(){this.textContent=""}function eN(){this.innerHTML=""}function eI(){this.nextSibling&&this.parentNode.appendChild(this)}function eP(){this.previousSibling&&this.parentNode.insertBefore(this,this.parentNode.firstChild)}function eL(t){var e=e$(t);return(e.local?function(t){return function(){return this.ownerDocument.createElementNS(t.space,t.local)}}:function(t){return function(){var e=this.ownerDocument,r=this.namespaceURI;return r===ex&&e.documentElement.namespaceURI===ex?e.createElement(t):e.createElementNS(r,t)}})(e)}function eR(){return null}function eD(){var t=this.parentNode;t&&t.removeChild(this)}function eF(){var t=this.cloneNode(!1),e=this.parentNode;return e?e.insertBefore(t,this.nextSibling):t}function ej(){var t=this.cloneNode(!0),e=this.parentNode;return e?e.insertBefore(t,this.nextSibling):t}function eH(t){return function(){var e=this.__on;if(e){for(var r,i=0,a=-1,s=e.length;i<s;++i)(r=e[i],t.type&&r.type!==t.type||r.name!==t.name)?e[++a]=r:this.removeEventListener(r.type,r.listener,r.options);++a?e.length=a:delete this.__on}}}function eO(t,e,r){return function(){var i,a=this.__on,s=function(t){e.call(this,t,this.__data__)};if(a){for(var n=0,o=a.length;n<o;++n)if((i=a[n]).type===t.type&&i.name===t.name){this.removeEventListener(i.type,i.listener,i.options),this.addEventListener(i.type,i.listener=s,i.options=r),i.value=e;return}}this.addEventListener(t.type,s,r),i={type:t.type,name:t.name,value:e,listener:s,options:r},a?a.push(i):this.__on=[i]}}function eB(t,e,r){var i=ek(t),a=i.CustomEvent;"function"==typeof a?a=new a(e,r):(a=i.document.createEvent("Event"),r?(a.initEvent(e,r.bubbles,r.cancelable),a.detail=r.detail):a.initEvent(e,!1,!1)),t.dispatchEvent(a)}eM.prototype={add:function(t){0>this._names.indexOf(t)&&(this._names.push(t),this._node.setAttribute("class",this._names.join(" ")))},remove:function(t){var e=this._names.indexOf(t);e>=0&&(this._names.splice(e,1),this._node.setAttribute("class",this._names.join(" ")))},contains:function(t){return this._names.indexOf(t)>=0}};var eq=[null];function eU(t,e){this._groups=t,this._parents=e}function eV(){return new eU([[document.documentElement]],eq)}function eW(t){return"string"==typeof t?new eU([[document.querySelector(t)]],[document.documentElement]):new eU([[t]],eq)}eU.prototype=eV.prototype={constructor:eU,select:function(t){"function"!=typeof t&&(t=ee(t));for(var e=this._groups,r=e.length,i=Array(r),a=0;a<r;++a)for(var s,n,o=e[a],l=o.length,h=i[a]=Array(l),c=0;c<l;++c)(s=o[c])&&(n=t.call(s,s.__data__,c,o))&&("__data__"in s&&(n.__data__=s.__data__),h[c]=n);return new eU(i,this._parents)},selectAll:function(t){if("function"==typeof t){var e;e=t,t=function(){var t;return t=e.apply(this,arguments),null==t?[]:Array.isArray(t)?t:Array.from(t)}}else t=ei(t);for(var r=this._groups,i=r.length,a=[],s=[],n=0;n<i;++n)for(var o,l=r[n],h=l.length,c=0;c<h;++c)(o=l[c])&&(a.push(t.call(o,o.__data__,c,l)),s.push(o));return new eU(a,s)},selectChild:function(t){var e;return this.select(null==t?ep:(e="function"==typeof t?t:es(t),function(){return ed.call(this.children,e)}))},selectChildren:function(t){var e;return this.selectAll(null==t?em:(e="function"==typeof t?t:es(t),function(){return eu.call(this.children,e)}))},filter:function(t){"function"!=typeof t&&(t=ea(t));for(var e=this._groups,r=e.length,i=Array(r),a=0;a<r;++a)for(var s,n=e[a],o=n.length,l=i[a]=[],h=0;h<o;++h)(s=n[h])&&t.call(s,s.__data__,h,n)&&l.push(s);return new eU(i,this._parents)},data:function(t,e){if(!arguments.length)return Array.from(this,eb);var r=e?ey:ev,i=this._parents,a=this._groups;"function"!=typeof t&&(y=t,t=function(){return y});for(var s=a.length,n=Array(s),o=Array(s),l=Array(s),h=0;h<s;++h){var c=i[h],d=a[h],p=d.length,u="object"==typeof(v=t.call(c,c&&c.__data__,h,i))&&"length"in v?v:Array.from(v),m=u.length,g=o[h]=Array(m),f=n[h]=Array(m);r(c,d,g,f,l[h]=Array(p),u,e);for(var v,y,b,z,x=0,w=0;x<m;++x)if(b=g[x]){for(x>=w&&(w=x+1);!(z=f[w])&&++w<m;);b._next=z||null}}return(n=new eU(n,i))._enter=o,n._exit=l,n},enter:function(){return new eU(this._enter||this._groups.map(eg),this._parents)},exit:function(){return new eU(this._exit||this._groups.map(eg),this._parents)},join:function(t,e,r){var i=this.enter(),a=this,s=this.exit();return"function"==typeof t?(i=t(i))&&(i=i.selection()):i=i.append(t+""),null!=e&&(a=e(a))&&(a=a.selection()),null==r?s.remove():r(s),i&&a?i.merge(a).order():a},merge:function(t){for(var e=t.selection?t.selection():t,r=this._groups,i=e._groups,a=r.length,s=i.length,n=Math.min(a,s),o=Array(a),l=0;l<n;++l)for(var h,c=r[l],d=i[l],p=c.length,u=o[l]=Array(p),m=0;m<p;++m)(h=c[m]||d[m])&&(u[m]=h);for(;l<a;++l)o[l]=r[l];return new eU(o,this._parents)},selection:function(){return this},order:function(){for(var t=this._groups,e=-1,r=t.length;++e<r;)for(var i,a=t[e],s=a.length-1,n=a[s];--s>=0;)(i=a[s])&&(n&&4^i.compareDocumentPosition(n)&&n.parentNode.insertBefore(i,n),n=i);return this},sort:function(t){function e(e,r){return e&&r?t(e.__data__,r.__data__):!e-!r}t||(t=ez);for(var r=this._groups,i=r.length,a=Array(i),s=0;s<i;++s){for(var n,o=r[s],l=o.length,h=a[s]=Array(l),c=0;c<l;++c)(n=o[c])&&(h[c]=n);h.sort(e)}return new eU(a,this._parents).order()},call:function(){var t=arguments[0];return arguments[0]=this,t.apply(null,arguments),this},nodes:function(){return Array.from(this)},node:function(){for(var t=this._groups,e=0,r=t.length;e<r;++e)for(var i=t[e],a=0,s=i.length;a<s;++a){var n=i[a];if(n)return n}return null},size:function(){let t=0;for(let e of this)++t;return t},empty:function(){return!this.node()},each:function(t){for(var e=this._groups,r=0,i=e.length;r<i;++r)for(var a,s=e[r],n=0,o=s.length;n<o;++n)(a=s[n])&&t.call(a,a.__data__,n,s);return this},attr:function(t,e){var r=e$(t);if(arguments.length<2){var i=this.node();return r.local?i.getAttributeNS(r.space,r.local):i.getAttribute(r)}return this.each((null==e?r.local?function(t){return function(){this.removeAttributeNS(t.space,t.local)}}:function(t){return function(){this.removeAttribute(t)}}:"function"==typeof e?r.local?function(t,e){return function(){var r=e.apply(this,arguments);null==r?this.removeAttributeNS(t.space,t.local):this.setAttributeNS(t.space,t.local,r)}}:function(t,e){return function(){var r=e.apply(this,arguments);null==r?this.removeAttribute(t):this.setAttribute(t,r)}}:r.local?function(t,e){return function(){this.setAttributeNS(t.space,t.local,e)}}:function(t,e){return function(){this.setAttribute(t,e)}})(r,e))},style:function(t,e,r){return arguments.length>1?this.each((null==e?function(t){return function(){this.style.removeProperty(t)}}:"function"==typeof e?function(t,e,r){return function(){var i=e.apply(this,arguments);null==i?this.style.removeProperty(t):this.style.setProperty(t,i,r)}}:function(t,e,r){return function(){this.style.setProperty(t,e,r)}})(t,e,null==r?"":r)):eS(this.node(),t)},property:function(t,e){return arguments.length>1?this.each((null==e?function(t){return function(){delete this[t]}}:"function"==typeof e?function(t,e){return function(){var r=e.apply(this,arguments);null==r?delete this[t]:this[t]=r}}:function(t,e){return function(){this[t]=e}})(t,e)):this.node()[t]},classed:function(t,e){var r=e_(t+"");if(arguments.length<2){for(var i=eA(this.node()),a=-1,s=r.length;++a<s;)if(!i.contains(r[a]))return!1;return!0}return this.each(("function"==typeof e?function(t,e){return function(){(e.apply(this,arguments)?eC:eE)(this,t)}}:e?function(t){return function(){eC(this,t)}}:function(t){return function(){eE(this,t)}})(r,e))},text:function(t){return arguments.length?this.each(null==t?eT:("function"==typeof t?function(t){return function(){var e=t.apply(this,arguments);this.textContent=null==e?"":e}}:function(t){return function(){this.textContent=t}})(t)):this.node().textContent},html:function(t){return arguments.length?this.each(null==t?eN:("function"==typeof t?function(t){return function(){var e=t.apply(this,arguments);this.innerHTML=null==e?"":e}}:function(t){return function(){this.innerHTML=t}})(t)):this.node().innerHTML},raise:function(){return this.each(eI)},lower:function(){return this.each(eP)},append:function(t){var e="function"==typeof t?t:eL(t);return this.select(function(){return this.appendChild(e.apply(this,arguments))})},insert:function(t,e){var r="function"==typeof t?t:eL(t),i=null==e?eR:"function"==typeof e?e:ee(e);return this.select(function(){return this.insertBefore(r.apply(this,arguments),i.apply(this,arguments)||null)})},remove:function(){return this.each(eD)},clone:function(t){return this.select(t?ej:eF)},datum:function(t){return arguments.length?this.property("__data__",t):this.node().__data__},on:function(t,e,r){var i,a,s=(t+"").trim().split(/^|\s+/).map(function(t){var e="",r=t.indexOf(".");return r>=0&&(e=t.slice(r+1),t=t.slice(0,r)),{type:t,name:e}}),n=s.length;if(arguments.length<2){var o=this.node().__on;if(o){for(var l,h=0,c=o.length;h<c;++h)for(i=0,l=o[h];i<n;++i)if((a=s[i]).type===l.type&&a.name===l.name)return l.value}return}for(i=0,o=e?eO:eH;i<n;++i)this.each(o(s[i],e,r));return this},dispatch:function(t,e){return this.each(("function"==typeof e?function(t,e){return function(){return eB(this,t,e.apply(this,arguments))}}:function(t,e){return function(){return eB(this,t,e)}})(t,e))},[Symbol.iterator]:function*(){for(var t=this._groups,e=0,r=t.length;e<r;++e)for(var i,a=t[e],s=0,n=a.length;s<n;++s)(i=a[s])&&(yield i)}};var eG={value:()=>{}};function eX(){for(var t,e=0,r=arguments.length,i={};e<r;++e){if(!(t=arguments[e]+"")||t in i||/[\s.]/.test(t))throw Error("illegal type: "+t);i[t]=[]}return new eY(i)}function eY(t){this._=t}function eZ(t,e,r){for(var i=0,a=t.length;i<a;++i)if(t[i].name===e){t[i]=eG,t=t.slice(0,i).concat(t.slice(i+1));break}return null!=r&&t.push({name:e,value:r}),t}eY.prototype=eX.prototype={constructor:eY,on:function(t,e){var r,i=this._,a=(t+"").trim().split(/^|\s+/).map(function(t){var e="",r=t.indexOf(".");if(r>=0&&(e=t.slice(r+1),t=t.slice(0,r)),t&&!i.hasOwnProperty(t))throw Error("unknown type: "+t);return{type:t,name:e}}),s=-1,n=a.length;if(arguments.length<2){for(;++s<n;)if((r=(t=a[s]).type)&&(r=function(t,e){for(var r,i=0,a=t.length;i<a;++i)if((r=t[i]).name===e)return r.value}(i[r],t.name)))return r;return}if(null!=e&&"function"!=typeof e)throw Error("invalid callback: "+e);for(;++s<n;)if(r=(t=a[s]).type)i[r]=eZ(i[r],t.name,e);else if(null==e)for(r in i)i[r]=eZ(i[r],t.name,null);return this},copy:function(){var t={},e=this._;for(var r in e)t[r]=e[r].slice();return new eY(t)},call:function(t,e){if((r=arguments.length-2)>0)for(var r,i,a=Array(r),s=0;s<r;++s)a[s]=arguments[s+2];if(!this._.hasOwnProperty(t))throw Error("unknown type: "+t);for(i=this._[t],s=0,r=i.length;s<r;++s)i[s].value.apply(e,a)},apply:function(t,e,r){if(!this._.hasOwnProperty(t))throw Error("unknown type: "+t);for(var i=this._[t],a=0,s=i.length;a<s;++a)i[a].value.apply(e,r)}};var eK,eJ,eQ=0,e0=0,e1=0,e2=0,e4=0,e3=0,e5="object"==typeof performance&&performance.now?performance:Date,e8="object"==typeof window&&window.requestAnimationFrame?window.requestAnimationFrame.bind(window):function(t){setTimeout(t,17)};function e6(){return e4||(e8(e9),e4=e5.now()+e3)}function e9(){e4=0}function e7(){this._call=this._time=this._next=null}function rt(t,e,r){var i=new e7;return i.restart(t,e,r),i}function re(){e4=(e2=e5.now())+e3,eQ=e0=0;try{e6(),++eQ;for(var t,e=eK;e;)(t=e4-e._time)>=0&&e._call.call(void 0,t),e=e._next;--eQ}finally{eQ=0,function(){for(var t,e,r=eK,i=1/0;r;)r._call?(i>r._time&&(i=r._time),t=r,r=r._next):(e=r._next,r._next=null,r=t?t._next=e:eK=e);eJ=t,ri(i)}(),e4=0}}function rr(){var t=e5.now(),e=t-e2;e>1e3&&(e3-=e,e2=t)}function ri(t){!eQ&&(e0&&(e0=clearTimeout(e0)),t-e4>24?(t<1/0&&(e0=setTimeout(re,t-e5.now()-e3)),e1&&(e1=clearInterval(e1))):(e1||(e2=e5.now(),e1=setInterval(rr,1e3)),eQ=1,e8(re)))}function ra(t,e,r){var i=new e7;return e=null==e?0:+e,i.restart(r=>{i.stop(),t(r+e)},e,r),i}e7.prototype=rt.prototype={constructor:e7,restart:function(t,e,r){if("function"!=typeof t)throw TypeError("callback is not a function");r=(null==r?e6():+r)+(null==e?0:+e),this._next||eJ===this||(eJ?eJ._next=this:eK=this,eJ=this),this._call=t,this._time=r,ri()},stop:function(){this._call&&(this._call=null,this._time=1/0,ri())}};var rs=eX("start","end","cancel","interrupt"),rn=[];function ro(t,e,r,i,a,s){var n=t.__transition;if(n){if(r in n)return}else t.__transition={};!function(t,e,r){var i,a=t.__transition;function s(l){var h,c,d,p;if(1!==r.state)return o();for(h in a)if((p=a[h]).name===r.name){if(3===p.state)return ra(s);4===p.state?(p.state=6,p.timer.stop(),p.on.call("interrupt",t,t.__data__,p.index,p.group),delete a[h]):+h<e&&(p.state=6,p.timer.stop(),p.on.call("cancel",t,t.__data__,p.index,p.group),delete a[h])}if(ra(function(){3===r.state&&(r.state=4,r.timer.restart(n,r.delay,r.time),n(l))}),r.state=2,r.on.call("start",t,t.__data__,r.index,r.group),2===r.state){for(h=0,r.state=3,i=Array(d=r.tween.length),c=-1;h<d;++h)(p=r.tween[h].value.call(t,t.__data__,r.index,r.group))&&(i[++c]=p);i.length=c+1}}function n(e){for(var a=e<r.duration?r.ease.call(null,e/r.duration):(r.timer.restart(o),r.state=5,1),s=-1,n=i.length;++s<n;)i[s].call(t,a);5===r.state&&(r.on.call("end",t,t.__data__,r.index,r.group),o())}function o(){for(var i in r.state=6,r.timer.stop(),delete a[e],a)return;delete t.__transition}a[e]=r,r.timer=rt(function(t){r.state=1,r.timer.restart(s,r.delay,r.time),r.delay<=t&&s(t-r.delay)},0,r.time)}(t,r,{name:e,index:i,group:a,on:rs,tween:rn,time:s.time,delay:s.delay,duration:s.duration,ease:s.ease,timer:null,state:0})}function rl(t,e){var r=rc(t,e);if(r.state>0)throw Error("too late; already scheduled");return r}function rh(t,e){var r=rc(t,e);if(r.state>3)throw Error("too late; already running");return r}function rc(t,e){var r=t.__transition;if(!r||!(r=r[e]))throw Error("transition not found");return r}function rd(t,e){return t*=1,e*=1,function(r){return t*(1-r)+e*r}}var rp=180/Math.PI,ru={translateX:0,translateY:0,rotate:0,skewX:0,scaleX:1,scaleY:1};function rm(t,e,r,i,a,s){var n,o,l;return(n=Math.sqrt(t*t+e*e))&&(t/=n,e/=n),(l=t*r+e*i)&&(r-=t*l,i-=e*l),(o=Math.sqrt(r*r+i*i))&&(r/=o,i/=o,l/=o),t*i<e*r&&(t=-t,e=-e,l=-l,n=-n),{translateX:a,translateY:s,rotate:Math.atan2(e,t)*rp,skewX:Math.atan(l)*rp,scaleX:n,scaleY:o}}function rg(t,e,r,i){function a(t){return t.length?t.pop()+" ":""}return function(s,n){var o,l,h,c,d=[],p=[];return s=t(s),n=t(n),!function(t,i,a,s,n,o){if(t!==a||i!==s){var l=n.push("translate(",null,e,null,r);o.push({i:l-4,x:rd(t,a)},{i:l-2,x:rd(i,s)})}else(a||s)&&n.push("translate("+a+e+s+r)}(s.translateX,s.translateY,n.translateX,n.translateY,d,p),o=s.rotate,l=n.rotate,o!==l?(o-l>180?l+=360:l-o>180&&(o+=360),p.push({i:d.push(a(d)+"rotate(",null,i)-2,x:rd(o,l)})):l&&d.push(a(d)+"rotate("+l+i),h=s.skewX,c=n.skewX,h!==c?p.push({i:d.push(a(d)+"skewX(",null,i)-2,x:rd(h,c)}):c&&d.push(a(d)+"skewX("+c+i),!function(t,e,r,i,s,n){if(t!==r||e!==i){var o=s.push(a(s)+"scale(",null,",",null,")");n.push({i:o-4,x:rd(t,r)},{i:o-2,x:rd(e,i)})}else(1!==r||1!==i)&&s.push(a(s)+"scale("+r+","+i+")")}(s.scaleX,s.scaleY,n.scaleX,n.scaleY,d,p),s=n=null,function(t){for(var e,r=-1,i=p.length;++r<i;)d[(e=p[r]).i]=e.x(t);return d.join("")}}}var rf=rg(function(t){let e=new("function"==typeof DOMMatrix?DOMMatrix:WebKitCSSMatrix)(t+"");return e.isIdentity?ru:rm(e.a,e.b,e.c,e.d,e.e,e.f)},"px, ","px)","deg)"),rv=rg(function(t){return null==t?ru:(en||(en=document.createElementNS("http://www.w3.org/2000/svg","g")),en.setAttribute("transform",t),t=en.transform.baseVal.consolidate())?rm((t=t.matrix).a,t.b,t.c,t.d,t.e,t.f):ru},", ",")",")");function ry(t,e,r){var i=t._id;return t.each(function(){var t=rh(this,i);(t.value||(t.value={}))[e]=r.apply(this,arguments)}),function(t){return rc(t,i).value[e]}}function rb(t,e,r){t.prototype=e.prototype=r,r.constructor=t}function rz(t,e){var r=Object.create(t.prototype);for(var i in e)r[i]=e[i];return r}function rx(){}var rw="\\s*([+-]?\\d+)\\s*",r$="\\s*([+-]?(?:\\d*\\.)?\\d+(?:[eE][+-]?\\d+)?)\\s*",rk="\\s*([+-]?(?:\\d*\\.)?\\d+(?:[eE][+-]?\\d+)?)%\\s*",rS=/^#([0-9a-f]{3,8})$/,r_=RegExp(`^rgb\\(${rw},${rw},${rw}\\)$`),rA=RegExp(`^rgb\\(${rk},${rk},${rk}\\)$`),rM=RegExp(`^rgba\\(${rw},${rw},${rw},${r$}\\)$`),rC=RegExp(`^rgba\\(${rk},${rk},${rk},${r$}\\)$`),rE=RegExp(`^hsl\\(${r$},${rk},${rk}\\)$`),rT=RegExp(`^hsla\\(${r$},${rk},${rk},${r$}\\)$`),rN={aliceblue:0xf0f8ff,antiquewhite:0xfaebd7,aqua:65535,aquamarine:8388564,azure:0xf0ffff,beige:0xf5f5dc,bisque:0xffe4c4,black:0,blanchedalmond:0xffebcd,blue:255,blueviolet:9055202,brown:0xa52a2a,burlywood:0xdeb887,cadetblue:6266528,chartreuse:8388352,chocolate:0xd2691e,coral:0xff7f50,cornflowerblue:6591981,cornsilk:0xfff8dc,crimson:0xdc143c,cyan:65535,darkblue:139,darkcyan:35723,darkgoldenrod:0xb8860b,darkgray:0xa9a9a9,darkgreen:25600,darkgrey:0xa9a9a9,darkkhaki:0xbdb76b,darkmagenta:9109643,darkolivegreen:5597999,darkorange:0xff8c00,darkorchid:0x9932cc,darkred:9109504,darksalmon:0xe9967a,darkseagreen:9419919,darkslateblue:4734347,darkslategray:3100495,darkslategrey:3100495,darkturquoise:52945,darkviolet:9699539,deeppink:0xff1493,deepskyblue:49151,dimgray:6908265,dimgrey:6908265,dodgerblue:2003199,firebrick:0xb22222,floralwhite:0xfffaf0,forestgreen:2263842,fuchsia:0xff00ff,gainsboro:0xdcdcdc,ghostwhite:0xf8f8ff,gold:0xffd700,goldenrod:0xdaa520,gray:8421504,green:32768,greenyellow:0xadff2f,grey:8421504,honeydew:0xf0fff0,hotpink:0xff69b4,indianred:0xcd5c5c,indigo:4915330,ivory:0xfffff0,khaki:0xf0e68c,lavender:0xe6e6fa,lavenderblush:0xfff0f5,lawngreen:8190976,lemonchiffon:0xfffacd,lightblue:0xadd8e6,lightcoral:0xf08080,lightcyan:0xe0ffff,lightgoldenrodyellow:0xfafad2,lightgray:0xd3d3d3,lightgreen:9498256,lightgrey:0xd3d3d3,lightpink:0xffb6c1,lightsalmon:0xffa07a,lightseagreen:2142890,lightskyblue:8900346,lightslategray:7833753,lightslategrey:7833753,lightsteelblue:0xb0c4de,lightyellow:0xffffe0,lime:65280,limegreen:3329330,linen:0xfaf0e6,magenta:0xff00ff,maroon:8388608,mediumaquamarine:6737322,mediumblue:205,mediumorchid:0xba55d3,mediumpurple:9662683,mediumseagreen:3978097,mediumslateblue:8087790,mediumspringgreen:64154,mediumturquoise:4772300,mediumvioletred:0xc71585,midnightblue:1644912,mintcream:0xf5fffa,mistyrose:0xffe4e1,moccasin:0xffe4b5,navajowhite:0xffdead,navy:128,oldlace:0xfdf5e6,olive:8421376,olivedrab:7048739,orange:0xffa500,orangered:0xff4500,orchid:0xda70d6,palegoldenrod:0xeee8aa,palegreen:0x98fb98,paleturquoise:0xafeeee,palevioletred:0xdb7093,papayawhip:0xffefd5,peachpuff:0xffdab9,peru:0xcd853f,pink:0xffc0cb,plum:0xdda0dd,powderblue:0xb0e0e6,purple:8388736,rebeccapurple:6697881,red:0xff0000,rosybrown:0xbc8f8f,royalblue:4286945,saddlebrown:9127187,salmon:0xfa8072,sandybrown:0xf4a460,seagreen:3050327,seashell:0xfff5ee,sienna:0xa0522d,silver:0xc0c0c0,skyblue:8900331,slateblue:6970061,slategray:7372944,slategrey:7372944,snow:0xfffafa,springgreen:65407,steelblue:4620980,tan:0xd2b48c,teal:32896,thistle:0xd8bfd8,tomato:0xff6347,turquoise:4251856,violet:0xee82ee,wheat:0xf5deb3,white:0xffffff,whitesmoke:0xf5f5f5,yellow:0xffff00,yellowgreen:0x9acd32};function rI(){return this.rgb().formatHex()}function rP(){return this.rgb().formatRgb()}function rL(t){var e,r;return t=(t+"").trim().toLowerCase(),(e=rS.exec(t))?(r=e[1].length,e=parseInt(e[1],16),6===r?rR(e):3===r?new rj(e>>8&15|e>>4&240,e>>4&15|240&e,(15&e)<<4|15&e,1):8===r?rD(e>>24&255,e>>16&255,e>>8&255,(255&e)/255):4===r?rD(e>>12&15|e>>8&240,e>>8&15|e>>4&240,e>>4&15|240&e,((15&e)<<4|15&e)/255):null):(e=r_.exec(t))?new rj(e[1],e[2],e[3],1):(e=rA.exec(t))?new rj(255*e[1]/100,255*e[2]/100,255*e[3]/100,1):(e=rM.exec(t))?rD(e[1],e[2],e[3],e[4]):(e=rC.exec(t))?rD(255*e[1]/100,255*e[2]/100,255*e[3]/100,e[4]):(e=rE.exec(t))?rV(e[1],e[2]/100,e[3]/100,1):(e=rT.exec(t))?rV(e[1],e[2]/100,e[3]/100,e[4]):rN.hasOwnProperty(t)?rR(rN[t]):"transparent"===t?new rj(NaN,NaN,NaN,0):null}function rR(t){return new rj(t>>16&255,t>>8&255,255&t,1)}function rD(t,e,r,i){return i<=0&&(t=e=r=NaN),new rj(t,e,r,i)}function rF(t,e,r,i){var a;return 1==arguments.length?((a=t)instanceof rx||(a=rL(a)),a)?new rj((a=a.rgb()).r,a.g,a.b,a.opacity):new rj:new rj(t,e,r,null==i?1:i)}function rj(t,e,r,i){this.r=+t,this.g=+e,this.b=+r,this.opacity=+i}function rH(){return`#${rU(this.r)}${rU(this.g)}${rU(this.b)}`}function rO(){let t=rB(this.opacity);return`${1===t?"rgb(":"rgba("}${rq(this.r)}, ${rq(this.g)}, ${rq(this.b)}${1===t?")":`, ${t})`}`}function rB(t){return isNaN(t)?1:Math.max(0,Math.min(1,t))}function rq(t){return Math.max(0,Math.min(255,Math.round(t)||0))}function rU(t){return((t=rq(t))<16?"0":"")+t.toString(16)}function rV(t,e,r,i){return i<=0?t=e=r=NaN:r<=0||r>=1?t=e=NaN:e<=0&&(t=NaN),new rG(t,e,r,i)}function rW(t){if(t instanceof rG)return new rG(t.h,t.s,t.l,t.opacity);if(t instanceof rx||(t=rL(t)),!t)return new rG;if(t instanceof rG)return t;var e=(t=t.rgb()).r/255,r=t.g/255,i=t.b/255,a=Math.min(e,r,i),s=Math.max(e,r,i),n=NaN,o=s-a,l=(s+a)/2;return o?(n=e===s?(r-i)/o+(r<i)*6:r===s?(i-e)/o+2:(e-r)/o+4,o/=l<.5?s+a:2-s-a,n*=60):o=l>0&&l<1?0:n,new rG(n,o,l,t.opacity)}function rG(t,e,r,i){this.h=+t,this.s=+e,this.l=+r,this.opacity=+i}function rX(t){return(t=(t||0)%360)<0?t+360:t}function rY(t){return Math.max(0,Math.min(1,t||0))}function rZ(t,e,r){return(t<60?e+(r-e)*t/60:t<180?r:t<240?e+(r-e)*(240-t)/60:e)*255}function rK(t,e,r,i,a){var s=t*t,n=s*t;return((1-3*t+3*s-n)*e+(4-6*s+3*n)*r+(1+3*t+3*s-3*n)*i+n*a)/6}rb(rx,rL,{copy(t){return Object.assign(new this.constructor,this,t)},displayable(){return this.rgb().displayable()},hex:rI,formatHex:rI,formatHex8:function(){return this.rgb().formatHex8()},formatHsl:function(){return rW(this).formatHsl()},formatRgb:rP,toString:rP}),rb(rj,rF,rz(rx,{brighter(t){return t=null==t?1.4285714285714286:Math.pow(1.4285714285714286,t),new rj(this.r*t,this.g*t,this.b*t,this.opacity)},darker(t){return t=null==t?.7:Math.pow(.7,t),new rj(this.r*t,this.g*t,this.b*t,this.opacity)},rgb(){return this},clamp(){return new rj(rq(this.r),rq(this.g),rq(this.b),rB(this.opacity))},displayable(){return -.5<=this.r&&this.r<255.5&&-.5<=this.g&&this.g<255.5&&-.5<=this.b&&this.b<255.5&&0<=this.opacity&&this.opacity<=1},hex:rH,formatHex:rH,formatHex8:function(){return`#${rU(this.r)}${rU(this.g)}${rU(this.b)}${rU((isNaN(this.opacity)?1:this.opacity)*255)}`},formatRgb:rO,toString:rO})),rb(rG,function(t,e,r,i){return 1==arguments.length?rW(t):new rG(t,e,r,null==i?1:i)},rz(rx,{brighter(t){return t=null==t?1.4285714285714286:Math.pow(1.4285714285714286,t),new rG(this.h,this.s,this.l*t,this.opacity)},darker(t){return t=null==t?.7:Math.pow(.7,t),new rG(this.h,this.s,this.l*t,this.opacity)},rgb(){var t=this.h%360+(this.h<0)*360,e=isNaN(t)||isNaN(this.s)?0:this.s,r=this.l,i=r+(r<.5?r:1-r)*e,a=2*r-i;return new rj(rZ(t>=240?t-240:t+120,a,i),rZ(t,a,i),rZ(t<120?t+240:t-120,a,i),this.opacity)},clamp(){return new rG(rX(this.h),rY(this.s),rY(this.l),rB(this.opacity))},displayable(){return(0<=this.s&&this.s<=1||isNaN(this.s))&&0<=this.l&&this.l<=1&&0<=this.opacity&&this.opacity<=1},formatHsl(){let t=rB(this.opacity);return`${1===t?"hsl(":"hsla("}${rX(this.h)}, ${100*rY(this.s)}%, ${100*rY(this.l)}%${1===t?")":`, ${t})`}`}}));let rJ=t=>()=>t;function rQ(t,e){var r=e-t;return r?function(e){return t+e*r}:rJ(isNaN(t)?e:t)}let r0=function t(e){var r,i=1==(r=+e)?rQ:function(t,e){var i,a,s;return e-t?(i=t,a=e,i=Math.pow(i,s=r),a=Math.pow(a,s)-i,s=1/s,function(t){return Math.pow(i+t*a,s)}):rJ(isNaN(t)?e:t)};function a(t,e){var r=i((t=rF(t)).r,(e=rF(e)).r),a=i(t.g,e.g),s=i(t.b,e.b),n=rQ(t.opacity,e.opacity);return function(e){return t.r=r(e),t.g=a(e),t.b=s(e),t.opacity=n(e),t+""}}return a.gamma=t,a}(1);function r1(t){return function(e){var r,i,a=e.length,s=Array(a),n=Array(a),o=Array(a);for(r=0;r<a;++r)i=rF(e[r]),s[r]=i.r||0,n[r]=i.g||0,o[r]=i.b||0;return s=t(s),n=t(n),o=t(o),i.opacity=1,function(t){return i.r=s(t),i.g=n(t),i.b=o(t),i+""}}}r1(function(t){var e=t.length-1;return function(r){var i=r<=0?r=0:r>=1?(r=1,e-1):Math.floor(r*e),a=t[i],s=t[i+1],n=i>0?t[i-1]:2*a-s,o=i<e-1?t[i+2]:2*s-a;return rK((r-i/e)*e,n,a,s,o)}}),r1(function(t){var e=t.length;return function(r){var i=Math.floor(((r%=1)<0?++r:r)*e),a=t[(i+e-1)%e],s=t[i%e],n=t[(i+1)%e],o=t[(i+2)%e];return rK((r-i/e)*e,a,s,n,o)}});var r2=/[-+]?(?:\d+\.?\d*|\.?\d+)(?:[eE][-+]?\d+)?/g,r4=RegExp(r2.source,"g");function r3(t,e){var r,i,a,s,n,o=r2.lastIndex=r4.lastIndex=0,l=-1,h=[],c=[];for(t+="",e+="";(a=r2.exec(t))&&(s=r4.exec(e));)(n=s.index)>o&&(n=e.slice(o,n),h[l]?h[l]+=n:h[++l]=n),(a=a[0])===(s=s[0])?h[l]?h[l]+=s:h[++l]=s:(h[++l]=null,c.push({i:l,x:rd(a,s)})),o=r4.lastIndex;return o<e.length&&(n=e.slice(o),h[l]?h[l]+=n:h[++l]=n),h.length<2?c[0]?(r=c[0].x,function(t){return r(t)+""}):(i=e,function(){return i}):(e=c.length,function(t){for(var r,i=0;i<e;++i)h[(r=c[i]).i]=r.x(t);return h.join("")})}function r5(t,e){var r;return("number"==typeof e?rd:e instanceof rL?r0:(r=rL(e))?(e=r,r0):r3)(t,e)}var r8=eV.prototype.constructor;function r6(t){return function(){this.style.removeProperty(t)}}var r9=0;function r7(t,e,r,i){this._groups=t,this._parents=e,this._name=r,this._id=i}var it=eV.prototype;r7.prototype=(function(t){return eV().transition(t)}).prototype={constructor:r7,select:function(t){var e=this._name,r=this._id;"function"!=typeof t&&(t=ee(t));for(var i=this._groups,a=i.length,s=Array(a),n=0;n<a;++n)for(var o,l,h=i[n],c=h.length,d=s[n]=Array(c),p=0;p<c;++p)(o=h[p])&&(l=t.call(o,o.__data__,p,h))&&("__data__"in o&&(l.__data__=o.__data__),d[p]=l,ro(d[p],e,r,p,d,rc(o,r)));return new r7(s,this._parents,e,r)},selectAll:function(t){var e=this._name,r=this._id;"function"!=typeof t&&(t=ei(t));for(var i=this._groups,a=i.length,s=[],n=[],o=0;o<a;++o)for(var l,h=i[o],c=h.length,d=0;d<c;++d)if(l=h[d]){for(var p,u=t.call(l,l.__data__,d,h),m=rc(l,r),g=0,f=u.length;g<f;++g)(p=u[g])&&ro(p,e,r,g,u,m);s.push(u),n.push(l)}return new r7(s,n,e,r)},selectChild:it.selectChild,selectChildren:it.selectChildren,filter:function(t){"function"!=typeof t&&(t=ea(t));for(var e=this._groups,r=e.length,i=Array(r),a=0;a<r;++a)for(var s,n=e[a],o=n.length,l=i[a]=[],h=0;h<o;++h)(s=n[h])&&t.call(s,s.__data__,h,n)&&l.push(s);return new r7(i,this._parents,this._name,this._id)},merge:function(t){if(t._id!==this._id)throw Error();for(var e=this._groups,r=t._groups,i=e.length,a=r.length,s=Math.min(i,a),n=Array(i),o=0;o<s;++o)for(var l,h=e[o],c=r[o],d=h.length,p=n[o]=Array(d),u=0;u<d;++u)(l=h[u]||c[u])&&(p[u]=l);for(;o<i;++o)n[o]=e[o];return new r7(n,this._parents,this._name,this._id)},selection:function(){return new r8(this._groups,this._parents)},transition:function(){for(var t=this._name,e=this._id,r=++r9,i=this._groups,a=i.length,s=0;s<a;++s)for(var n,o=i[s],l=o.length,h=0;h<l;++h)if(n=o[h]){var c=rc(n,e);ro(n,t,r,h,o,{time:c.time+c.delay+c.duration,delay:0,duration:c.duration,ease:c.ease})}return new r7(i,this._parents,t,r)},call:it.call,nodes:it.nodes,node:it.node,size:it.size,empty:it.empty,each:it.each,on:function(t,e){var r,i,a,s,n,o,l=this._id;return arguments.length<2?rc(this.node(),l).on.on(t):this.each((r=l,i=t,a=e,o=(i+"").trim().split(/^|\s+/).every(function(t){var e=t.indexOf(".");return e>=0&&(t=t.slice(0,e)),!t||"start"===t})?rl:rh,function(){var t=o(this,r),e=t.on;e!==s&&(n=(s=e).copy()).on(i,a),t.on=n}))},attr:function(t,e){var r=e$(t),i="transform"===r?rv:r5;return this.attrTween(t,"function"==typeof e?(r.local?function(t,e,r){var i,a,s;return function(){var n,o,l=r(this);return null==l?void this.removeAttributeNS(t.space,t.local):(n=this.getAttributeNS(t.space,t.local))===(o=l+"")?null:n===i&&o===a?s:(a=o,s=e(i=n,l))}}:function(t,e,r){var i,a,s;return function(){var n,o,l=r(this);return null==l?void this.removeAttribute(t):(n=this.getAttribute(t))===(o=l+"")?null:n===i&&o===a?s:(a=o,s=e(i=n,l))}})(r,i,ry(this,"attr."+t,e)):null==e?(r.local?function(t){return function(){this.removeAttributeNS(t.space,t.local)}}:function(t){return function(){this.removeAttribute(t)}})(r):(r.local?function(t,e,r){var i,a,s=r+"";return function(){var n=this.getAttributeNS(t.space,t.local);return n===s?null:n===i?a:a=e(i=n,r)}}:function(t,e,r){var i,a,s=r+"";return function(){var n=this.getAttribute(t);return n===s?null:n===i?a:a=e(i=n,r)}})(r,i,e))},attrTween:function(t,e){var r="attr."+t;if(arguments.length<2)return(r=this.tween(r))&&r._value;if(null==e)return this.tween(r,null);if("function"!=typeof e)throw Error();var i=e$(t);return this.tween(r,(i.local?function(t,e){var r,i;function a(){var a=e.apply(this,arguments);return a!==i&&(r=(i=a)&&function(e){this.setAttributeNS(t.space,t.local,a.call(this,e))}),r}return a._value=e,a}:function(t,e){var r,i;function a(){var a=e.apply(this,arguments);return a!==i&&(r=(i=a)&&function(e){this.setAttribute(t,a.call(this,e))}),r}return a._value=e,a})(i,e))},style:function(t,e,r){var i,a,s,n,o,l,h,c,d,p,u,m,g,f,v,y,b,z,x,w,$,k="transform"==(t+="")?rf:r5;return null==e?this.styleTween(t,(i=t,function(){var t=eS(this,i),e=(this.style.removeProperty(i),eS(this,i));return t===e?null:t===a&&e===s?n:n=k(a=t,s=e)})).on("end.style."+t,r6(t)):"function"==typeof e?this.styleTween(t,(o=t,l=ry(this,"style."+t,e),function(){var t=eS(this,o),e=l(this),r=e+"";return null==e&&(this.style.removeProperty(o),r=e=eS(this,o)),t===r?null:t===h&&r===c?d:(c=r,d=k(h=t,e))})).each((p=this._id,b="end."+(y="style."+(u=t)),function(){var t=rh(this,p),e=t.on,r=null==t.value[y]?v||(v=r6(u)):void 0;(e!==m||f!==r)&&(g=(m=e).copy()).on(b,f=r),t.on=g})):this.styleTween(t,(z=t,$=e+"",function(){var t=eS(this,z);return t===$?null:t===x?w:w=k(x=t,e)}),r).on("end.style."+t,null)},styleTween:function(t,e,r){var i="style."+(t+="");if(arguments.length<2)return(i=this.tween(i))&&i._value;if(null==e)return this.tween(i,null);if("function"!=typeof e)throw Error();return this.tween(i,function(t,e,r){var i,a;function s(){var s=e.apply(this,arguments);return s!==a&&(i=(a=s)&&function(e){this.style.setProperty(t,s.call(this,e),r)}),i}return s._value=e,s}(t,e,null==r?"":r))},text:function(t){var e,r;return this.tween("text","function"==typeof t?(e=ry(this,"text",t),function(){var t=e(this);this.textContent=null==t?"":t}):(r=null==t?"":t+"",function(){this.textContent=r}))},textTween:function(t){var e="text";if(arguments.length<1)return(e=this.tween(e))&&e._value;if(null==t)return this.tween(e,null);if("function"!=typeof t)throw Error();return this.tween(e,function(t){var e,r;function i(){var i=t.apply(this,arguments);return i!==r&&(e=(r=i)&&function(t){this.textContent=i.call(this,t)}),e}return i._value=t,i}(t))},remove:function(){var t;return this.on("end.remove",(t=this._id,function(){var e=this.parentNode;for(var r in this.__transition)if(+r!==t)return;e&&e.removeChild(this)}))},tween:function(t,e){var r=this._id;if(t+="",arguments.length<2){for(var i,a=rc(this.node(),r).tween,s=0,n=a.length;s<n;++s)if((i=a[s]).name===t)return i.value;return null}return this.each((null==e?function(t,e){var r,i;return function(){var a=rh(this,t),s=a.tween;if(s!==r){i=r=s;for(var n=0,o=i.length;n<o;++n)if(i[n].name===e){(i=i.slice()).splice(n,1);break}}a.tween=i}}:function(t,e,r){var i,a;if("function"!=typeof r)throw Error();return function(){var s=rh(this,t),n=s.tween;if(n!==i){a=(i=n).slice();for(var o={name:e,value:r},l=0,h=a.length;l<h;++l)if(a[l].name===e){a[l]=o;break}l===h&&a.push(o)}s.tween=a}})(r,t,e))},delay:function(t){var e=this._id;return arguments.length?this.each(("function"==typeof t?function(t,e){return function(){rl(this,t).delay=+e.apply(this,arguments)}}:function(t,e){return e*=1,function(){rl(this,t).delay=e}})(e,t)):rc(this.node(),e).delay},duration:function(t){var e=this._id;return arguments.length?this.each(("function"==typeof t?function(t,e){return function(){rh(this,t).duration=+e.apply(this,arguments)}}:function(t,e){return e*=1,function(){rh(this,t).duration=e}})(e,t)):rc(this.node(),e).duration},ease:function(t){var e=this._id;return arguments.length?this.each(function(t,e){if("function"!=typeof e)throw Error();return function(){rh(this,t).ease=e}}(e,t)):rc(this.node(),e).ease},easeVarying:function(t){var e;if("function"!=typeof t)throw Error();return this.each((e=this._id,function(){var r=t.apply(this,arguments);if("function"!=typeof r)throw Error();rh(this,e).ease=r}))},end:function(){var t,e,r=this,i=r._id,a=r.size();return new Promise(function(s,n){var o={value:n},l={value:function(){0==--a&&s()}};r.each(function(){var r=rh(this,i),a=r.on;a!==t&&((e=(t=a).copy())._.cancel.push(o),e._.interrupt.push(o),e._.end.push(l)),r.on=e}),0===a&&s()})},[Symbol.iterator]:it[Symbol.iterator]};var ie={time:null,delay:0,duration:250,ease:function(t){return((t*=2)<=1?t*t*t:(t-=2)*t*t+2)/2}};eV.prototype.interrupt=function(t){return this.each(function(){!function(t,e){var r,i,a,s=t.__transition,n=!0;if(s){for(a in e=null==e?null:e+"",s){if((r=s[a]).name!==e){n=!1;continue}i=r.state>2&&r.state<5,r.state=6,r.timer.stop(),r.on.call(i?"interrupt":"cancel",t,t.__data__,r.index,r.group),delete s[a]}n&&delete t.__transition}}(this,t)})},eV.prototype.transition=function(t){var e,r;t instanceof r7?(e=t._id,t=t._name):(e=++r9,(r=ie).time=e6(),t=null==t?null:t+"");for(var i=this._groups,a=i.length,s=0;s<a;++s)for(var n,o=i[s],l=o.length,h=0;h<l;++h)(n=o[h])&&ro(n,t,e,h,o,r||function(t,e){for(var r;!(r=t.__transition)||!(r=r[e]);)if(!(t=t.parentNode))throw Error(`transition ${e} not found`);return r}(n,e));return new r7(i,this._parents,t,e)};let ir=l`
  :host {
    display: block;
    color: var(--smzh-color-text-default);
    font-family: var(--smzh-font-family-sans, sans-serif);
    --smzh-rate-zone-left: color-mix(
      in srgb,
      var(--smzh-color-success) 14%,
      var(--smzh-color-surface)
    );
    --smzh-rate-zone-right: color-mix(
      in srgb,
      var(--smzh-color-error) 10%,
      var(--smzh-color-surface)
    );
    --smzh-rate-marker: var(--smzh-color-text-emphasis);
  }

  .wrap {
    max-width: 550px;
    margin: 0 auto;
    text-align: center;
  }

  .heading {
    margin: 0;
    color: var(--smzh-color-text-default);
    font-size: 18px;
    line-height: 24px;
    letter-spacing: 0;
    font-weight: var(--smzh-font-weight-medium);
  }

  .subheading {
    margin: 8px 0 0;
    color: var(--smzh-color-text-subtle);
    font-size: 18px;
    line-height: 24px;
    letter-spacing: 0;
    font-weight: var(--smzh-rate-range-chart-subheading-font-weight, 450);
  }

  .card {
    margin-top: 28px;
    border-radius: 24px;
    border: 1px solid var(--smzh-color-border-subtle);
    background: var(--smzh-color-surface);
    padding: 22px 20px 18px;
  }

  .base-pill {
    display: inline-block;
    min-width: 260px;
    margin-bottom: 50px;
    border-radius: 30px;
    background: var(--smzh-color-background-subtle);
    padding: 8px;
    color: var(--smzh-color-text-subtle);
    font-size: var(--smzh-typography-text-md-font-size);
    line-height: 16px;
    letter-spacing: var(--smzh-typography-text-md-letter-spacing);
    font-weight: var(--smzh-font-weight-medium);
  }

  .base-pill strong {
    color: var(--smzh-color-text-emphasis);
    font-weight: var(--smzh-font-weight-medium);
  }

  .bar-wrap {
    position: relative;
    width: 100%;
    height: 32px;
    border-radius: 8px;
    overflow: visible;
    background: var(--smzh-color-background);
  }

  .bar-svg {
    display: block;
    width: 100%;
    height: 100%;
    overflow: visible;
  }

  .risk-gradient {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 50%;
    pointer-events: none;
    z-index: 1;
  }

  .safe-gradient {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 50%;
    pointer-events: none;
    z-index: 1;
  }

  .safe-gradient[data-side="left"] {
    left: 0;
    background: linear-gradient(
      to right,
      color-mix(
          in srgb,
          var(--smzh-color-success-accent) 10%,
          var(--smzh-color-background)
        )
        0%,
      var(--smzh-color-background) 72%
    );
    border-top-left-radius: 8px;
    border-bottom-left-radius: 8px;
  }

  .safe-gradient[data-side="right"] {
    right: 0;
    background: linear-gradient(
      to left,
      color-mix(
          in srgb,
          var(--smzh-color-success-accent) 10%,
          var(--smzh-color-background)
        )
        0%,
      var(--smzh-color-background) 72%
    );
    border-top-right-radius: 8px;
    border-bottom-right-radius: 8px;
  }

  .risk-gradient[data-side="right"] {
    right: 0;
    background: linear-gradient(
      to left,
      color-mix(
          in srgb,
          var(--smzh-color-error-accent) 10%,
          var(--smzh-color-background)
        )
        0%,
      var(--smzh-color-background) 72%
    );
    border-top-right-radius: 8px;
    border-bottom-right-radius: 8px;
  }

  .risk-gradient[data-side="left"] {
    left: 0;
    background: linear-gradient(
      to right,
      color-mix(
          in srgb,
          var(--smzh-color-error-accent) 10%,
          var(--smzh-color-background)
        )
        0%,
      var(--smzh-color-background) 72%
    );
    border-top-left-radius: 8px;
    border-bottom-left-radius: 8px;
  }

  .center-divider {
    position: absolute;
    top: 0;
    left: 50%;
    height: 32px;
    width: 1px;
    transform: translateX(-0.5px);
    background: var(--smzh-color-border-subtle);
    z-index: 3;
  }

  .marker-overlay {
    position: absolute;
    top: -3px;
    width: 4px;
    height: 37px;
    border-radius: 999px;
    transform: translateX(-50%);
    background: var(--smzh-color-text-disabled);
    z-index: 4;
    transition: left 320ms ease-out;
  }

  .rates {
    position: absolute;
    inset: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 14px;
    pointer-events: none;
    z-index: 5;
    font-size: var(--smzh-typography-label-md-font-size);
    line-height: 14px;
    letter-spacing: -0.2px;
    font-weight: var(--smzh-font-weight-medium);
  }

  .rates .min {
    color: var(--smzh-color-success-accent);
  }

  .rates .max {
    color: var(--smzh-color-error-accent);
  }

  .bar-wrap[data-risk-side="left"] .rates .min {
    color: var(--smzh-color-error-accent);
  }

  .bar-wrap[data-risk-side="left"] .rates .max {
    color: var(--smzh-color-success-accent);
  }

  .labels {
    margin-top: 10px;
    display: flex;
    justify-content: space-between;
    gap: 16px;
    text-align: left;
    font-size: var(--smzh-typography-label-md-font-size);
    line-height: 16px;
    letter-spacing: -0.2px;
    font-weight: var(--smzh-font-weight-normal);
    color: var(--smzh-color-text-subtle);
  }

  .labels .right {
    text-align: right;
  }

  .status {
    margin-top: 16px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    gap: 4px;
    border-radius: 22px;
    border: 1px solid var(--smzh-color-border-default);
    background: var(--smzh-color-surface);
    padding: 8px;
    font-size: var(--smzh-typography-label-md-font-size);
    line-height: var(--smzh-typography-label-md-font-size);
    letter-spacing: -0.2px;
  }

  .status-lead {
    color: var(--smzh-color-text-strong);
    font-weight: var(--smzh-font-weight-normal);
  }

  .status-emphasis {
    font-weight: var(--smzh-font-weight-medium);
    color: var(--smzh-color-text-strong);
  }

  .status span:first-child {
    color: var(--smzh-color-text-strong);
  }

  .status[data-tone="positive"] .status-emphasis {
    color: var(--smzh-color-success-accent);
  }

  .status[data-tone="negative"] .status-emphasis {
    color: var(--smzh-color-text-error);
  }

  .status[data-tone="neutral"] .status-emphasis {
    color: var(--smzh-color-text-subtle);
  }

  .status-single {
    color: var(--smzh-color-text-strong);
    font-weight: var(--smzh-font-weight-medium);
  }

  .status[data-tone="neutral"] .status-single {
    color: var(--smzh-color-text-subtle);
    font-weight: var(--smzh-font-weight-normal);
  }
`;"u">typeof window&&!customElements.get("smzh-rate-range-chart")&&customElements.define("smzh-rate-range-chart",class extends tp{static styles=ir;static properties={title:{type:String},subtitle:{type:String},baseRate:{type:Number,attribute:"base-rate"},minRate:{type:Number,attribute:"min-rate"},maxRate:{type:Number,attribute:"max-rate"},leftTitle:{type:String,attribute:"left-title"},leftSubtitle:{type:String,attribute:"left-subtitle"},rightTitle:{type:String,attribute:"right-title"},rightSubtitle:{type:String,attribute:"right-subtitle"},statusText:{type:String,attribute:"status-text"},statusTone:{type:String,attribute:"status-tone",reflect:!0},riskSide:{type:String,attribute:"risk-side",reflect:!0}};resizeObserver=null;barWidth=0;constructor(){super(),this.title="",this.subtitle="",this.baseRate=0,this.minRate=0,this.maxRate=0,this.leftTitle="Gunstige Bank",this.leftSubtitle="Tiefer Zinssatz",this.rightTitle="Teure Bank",this.rightSubtitle="Tiefster Zinssatz",this.statusText="Noch keine Daten",this.statusTone="neutral",this.riskSide="right"}connectedCallback(){super.connectedCallback(),this.resizeObserver=new ResizeObserver(t=>{let[e]=t;if(!e)return;let r=Math.max(1,Math.floor(e.contentRect.width));r!==this.barWidth&&(this.barWidth=r,this.requestUpdate())})}firstUpdated(){let t=this.renderRoot.querySelector(".bar-wrap");t instanceof HTMLElement&&(this.resizeObserver?.observe(t),this.barWidth=Math.max(1,Math.floor(t.clientWidth))),this.renderD3Chart()}disconnectedCallback(){this.resizeObserver?.disconnect(),this.resizeObserver=null,super.disconnectedCallback()}getMarkerPositionPercent(){let t=this.minRate,e=this.maxRate;return e>t?Math.min(100,Math.max(0,(this.baseRate-t)/(e-t)*100)):50}formatRate(t,e=""){return`${t.toFixed(2)}%${e}`}updated(t){super.updated(t),this.renderD3Chart()}getSvgSelection(){let t=this.renderRoot.querySelector("svg");if(!(t instanceof SVGSVGElement))throw Error("[smzh-rate-range-chart] Missing SVG element in shadow root.");return eW(t)}renderD3Chart(){let t=Math.max(1,this.barWidth);this.getSvgSelection().attr("viewBox",`0 0 ${t} 48`).selectAll("rect.zone").data([{x:0,width:t/2,fill:"var(--smzh-rate-zone-left)"},{x:t/2,width:t/2,fill:"var(--smzh-color-background)"}]).join("rect").attr("class","zone").attr("y",0).attr("height",48).attr("fill",t=>t.fill).transition().duration(320).attr("x",t=>t.x).attr("width",t=>t.width)}getStatusParts(){let t=this.statusText.trim();if(!t)return{lead:"",emphasis:""};let e=t.split(/\s+/).filter(t=>t.length>0);return e.length<=2?{lead:t,emphasis:""}:{lead:e.slice(0,2).join(" "),emphasis:e.slice(2).join(" ")}}render(){let t=this.getMarkerPositionPercent(),e="right"===this.riskSide?"left":"right",{lead:r,emphasis:i}=this.getStatusParts(),a=this.title.trim().length>0,s=this.subtitle.trim().length>0;return W`
      <section class="wrap">
        ${a?W`<h2 class="heading">${this.title}</h2>`:null}
        ${s?W`<p class="subheading">${this.subtitle}</p>`:null}

        <article class="card">
          <div class="base-pill">
            Ihre Ausgangslage:
            <strong>${this.formatRate(this.baseRate)}</strong>
          </div>

          <div class="bar-wrap" data-risk-side=${this.riskSide}>
            <svg class="bar-svg" aria-hidden="true"></svg>
            <div
              class="safe-gradient"
              data-side=${e}
              aria-hidden="true"
            ></div>
            <div
              class="risk-gradient"
              data-side=${this.riskSide}
              aria-hidden="true"
            ></div>
            <div class="center-divider" aria-hidden="true"></div>
            <div
              class="marker-overlay"
              aria-hidden="true"
              style="left: ${t}%;"
            ></div>
            <div class="rates">
              <span class="min">${this.formatRate(this.minRate)}</span>
              <span class="max">${this.formatRate(this.maxRate," +")}</span>
            </div>
          </div>

          <div class="labels">
            <div>
              <div>${this.leftTitle}</div>
              <div>${this.leftSubtitle}</div>
            </div>
            <div class="right">
              <div>${this.rightTitle}</div>
              <div>${this.rightSubtitle}</div>
            </div>
          </div>

          <div class="status" data-tone=${this.statusTone}>
            ${i?W`
                  <span class="status-lead">${r}</span>
                  <span class="status-emphasis">${i}</span>
                `:W`<span class="status-single">${r}</span>`}
          </div>
        </article>
      </section>
    `}});let ii=l`
  :host {
    display: block;
    font-family: var(--smzh-font-family-sans, sans-serif);
    color: var(--smzh-color-text-default);
  }

  .wrap {
    max-width: 420px;
    min-width: 370px;
    margin: 0 auto;
  }

  /*
   * has-data false: hide title row + legend; hide equity left %, min marker UI; equity right shows 0%.
   * Keep D3 bars (equity + 3-color income). Hide income copy, triangle marker, label under bar.
   */
  .wrap--empty .header {
    display: none !important;
  }

  .wrap--empty .legend {
    display: none !important;
  }

  .wrap--empty .equity-values {
    justify-content: flex-end;
  }

  .wrap--empty .equity-values .left {
    display: none !important;
  }

  .wrap--empty .minimum-dot,
  .wrap--empty .minimum-label {
    display: none !important;
  }

  .wrap--empty .income-copy {
    display: none !important;
  }

  .wrap--empty .income-marker,
  .wrap--empty .income-label {
    display: none !important;
  }

  .wrap--empty .income-row {
    grid-template-columns: auto;
    gap: 0;
  }

  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
  }

  .header h3 {
    margin: 0;
    font-size: var(--smzh-typography-text-md-font-size);
    line-height: 20px;
    letter-spacing: var(--smzh-typography-text-md-letter-spacing);
    font-weight: var(--smzh-font-weight-medium);
    color: var(--smzh-color-text-emphasis);
  }

  .pill {
    border: 1px solid var(--smzh-color-primary-hover);
    border-radius: 32px;
    padding: 4px 10px;
    color: var(--smzh-color-text-emphasis);
    background: var(--smzh-color-primary-subtle-hover);
    font-size: var(--smzh-typography-label-md-font-size);
    line-height: 20px;
    font-weight: var(--smzh-font-weight-medium);
  }

  .card {
    border: 1px solid var(--smzh-color-border-subtle);
    border-radius: 24px;
    background: var(--smzh-color-surface);
    padding: 16px 16px 24px 16px;
  }

  .legend {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 8px;
    font-size: var(--smzh-typography-label-md-font-size);
    line-height: 14px;
    letter-spacing: -0.28px;
    font-weight: var(--smzh-font-weight-normal);
    margin-bottom: 12px;
  }

  .legend .dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 8px;
  }

  .legend .left {
    color: var(--smzh-color-text-emphasis);
  }

  .legend .left .dot {
    background: var(--smzh-color-text-emphasis);
  }

  .legend .right {
    color: var(--smzh-color-text-disabled);
  }

  .legend .right .dot {
    background: var(--smzh-color-text-disabled);
    margin-left: 5px;
    margin-right: 0;
  }

  .equity-bar-wrap {
    position: relative;
    height: 98px;
    border-radius: 18px;
    overflow: hidden;
    background: var(--smzh-color-background-subtle);
  }

  .equity-group {
    position: relative;
    padding-bottom: 14px;
  }

  .minimum-dot {
    position: absolute;
    top: 94px;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    transform: translateX(-50%);
    background: var(--smzh-color-chart-minimum-dot);
    z-index: 4;
  }

  .equity-bar-svg {
    width: 100%;
    height: 100%;
    display: block;
  }

  .equity-values {
    position: absolute;
    inset: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 14px;
    pointer-events: none;
    font-size: 28px;
    line-height: 28px;
    font-weight: var(--smzh-font-weight-medium);
    letter-spacing: -0.56px;
  }

  .equity-values .left {
    color: var(--smzh-color-chart-equity-left);
  }

  .equity-values .right {
    color: var(--smzh-color-chart-equity-right);
  }

  .minimum-label {
    position: absolute;
    top: 105px;
    transform: translateX(-50%);
    width: max-content;
    white-space: nowrap;
    color: var(--smzh-color-text-subtle);
    font-size: var(--smzh-typography-label-sm-font-size);
    line-height: 14px;
    font-weight: var(--smzh-font-weight-normal);
  }

  .minimum-label[data-align="left"] {
    transform: translateX(0);
  }

  .minimum-label[data-align="right"] {
    transform: translateX(-100%);
  }

  .income-card {
    margin-top: 14px;
    border: 1px solid var(--smzh-color-border-subtle);
    border-radius: 24px;
    background: var(--smzh-color-surface);
    padding: 20px;
  }

  .income-row {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 62px;
    align-items: center;
    padding: 0 20px;
    margin-bottom: 20px;
  }

  .income-value {
    font-size: 32px;
    line-height: 32px;
    font-weight: var(--smzh-font-weight-medium);
    color: var(--smzh-color-text-emphasis);
  }

  .income-copy {
    font-size: var(--smzh-typography-text-md-font-size);
    line-height: var(--smzh-typography-text-md-line-height);
    letter-spacing: var(--smzh-typography-text-md-letter-spacing);
    font-weight: var(--smzh-font-weight-normal);
    color: var(--smzh-color-text-subtle);
    hyphens: auto;
    overflow-wrap: normal;
    word-break: normal;
  }

  .income-copy smzh-tooltip {
    display: inline-block;
    vertical-align: baseline;
  }

  .income-tooltip-trigger {
    appearance: none;
    border-width: 0;
    border-style: none;
    background: transparent;
    color: inherit;
    cursor: help;
    font: inherit;
    letter-spacing: inherit;
    line-height: inherit;
    margin: 0;
    padding: 0;
    text-decoration: underline;
    text-underline-offset: 2px;
    text-decoration-thickness: 1px;
  }

  .income-tooltip-content {
    max-width: 320px;
    text-align: left;
  }

  .income-tooltip-content ul {
    margin: 8px 0 0;
    padding-left: 18px;
  }

  .income-bar-wrap {
    margin-top: 10px;
    height: 20px;
    border-radius: 8px;
    overflow: visible;
    position: relative;
    background: var(--smzh-color-background-subtle);
  }

  .income-bar-svg {
    width: 100%;
    height: 100%;
    display: block;
    border-radius: 8px;
    overflow: hidden;
  }

  .income-marker {
    position: absolute;
    top: 20px;
    width: 0;
    height: 0;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 8px solid var(--smzh-color-chart-income-safe);
    transform: translateX(-50%);
  }

  .income-label {
    position: relative;
    width: max-content;
    margin-top: 12px;
    transform: translateX(-50%);
    font-size: var(--smzh-typography-label-md-font-size);
    line-height: 16px;
    letter-spacing: -0.28px;
    color: var(--smzh-color-text-emphasis);
    font-weight: var(--smzh-font-weight-normal);
  }

  .income-label[data-align="left"] {
    transform: translateX(0);
  }

  .income-label[data-align="right"] {
    transform: translateX(-100%);
  }

  .table {
    padding: var(--smzh-spacing-lg) 0 15px 0;
    display: grid;
    gap: 12px;
  }

  .table-row {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    align-items: baseline;
    font-size: var(--smzh-typography-label-md-font-size);
    line-height: 16px;
    letter-spacing: -0.28px;
    font-weight: var(--smzh-font-weight-normal);
  }

  .table-row strong {
    color: var(--smzh-color-text-emphasis);
    font-weight: var(--smzh-font-weight-medium);
    font-size: var(--smzh-typography-text-md-font-size);
    line-height: 20px;
    letter-spacing: var(--smzh-typography-text-md-letter-spacing);
  }

  .table-row .muted {
    color: var(--smzh-color-text-subtle);
    font-size: var(--smzh-typography-label-md-font-size);
    line-height: 16px;
    letter-spacing: -0.28px;
    font-weight: var(--smzh-font-weight-normal);
  }

  .table-row .muted smzh-tooltip {
    display: inline-block;
    vertical-align: baseline;
    --smzh-tooltip-max-width: var(
      --smzh-mortgage-affordability-table-tooltip-max-width,
      320px
    );
  }

  .table-label-with-tooltip {
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }

  .table-tooltip-trigger {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 16px;
    height: 16px;
    appearance: none;
    border-width: 0;
    border-style: none;
    background: transparent;
    color: inherit;
    cursor: help;
    line-height: 0;
    margin: 0;
    padding: 0;
    vertical-align: middle;
  }

  .table-row .value {
    color: var(--smzh-color-text-emphasis);
    font-weight: var(--smzh-font-weight-normal);
    font-size: var(--smzh-typography-label-md-font-size);
    line-height: 16px;
    letter-spacing: -0.28px;
  }

  .table-row:first-child .value {
    font-weight: var(--smzh-font-weight-normal);
    font-size: var(--smzh-typography-label-md-font-size);
    line-height: 16px;
  }
`;"u">typeof window&&!customElements.get("smzh-mortgage-affordability-chart")&&customElements.define("smzh-mortgage-affordability-chart",class extends tp{static styles=ii;static properties={affordabilityLabel:{type:String,attribute:"affordability-label"},affordabilityStatus:{type:String,attribute:"affordability-status"},equityPercent:{type:Number,attribute:"equity-percent"},minimumEquityPercent:{type:Number,attribute:"minimum-equity-percent"},affordabilityPercent:{type:Number,attribute:"affordability-percent"},affordabilityMarkerPercent:{type:Number,attribute:"affordability-marker-percent"},monthlyTotal:{type:String,attribute:"monthly-total"},monthlyInterest:{type:String,attribute:"monthly-interest"},referenceInterestRate:{type:Number,attribute:"reference-interest-rate"},monthlyInterestTooltip:{type:String,attribute:"monthly-interest-tooltip"},monthlyUpkeep:{type:String,attribute:"monthly-upkeep"},monthlyUpkeepTooltip:{type:String,attribute:"monthly-upkeep-tooltip"},monthlyAmortization:{type:String,attribute:"monthly-amortization"},hasData:{type:Boolean,attribute:"has-data",reflect:!0}};resizeObserver=null;equityWidth=0;incomeWidth=0;constructor(){super(),this.affordabilityLabel="Ihre Hypothek ist",this.affordabilityStatus="Noch keine Daten",this.equityPercent=0,this.minimumEquityPercent=0,this.affordabilityPercent=0,this.affordabilityMarkerPercent=0,this.monthlyTotal="CHF 0",this.monthlyInterest="CHF 0",this.referenceInterestRate=5,this.monthlyInterestTooltip="",this.monthlyUpkeep="CHF 0",this.monthlyUpkeepTooltip="",this.monthlyAmortization="CHF 0",this.hasData=!1}connectedCallback(){super.connectedCallback(),this.resizeObserver=new ResizeObserver(()=>{let t=this.renderRoot.querySelector(".equity-bar-wrap"),e=this.renderRoot.querySelector(".income-bar-wrap");t instanceof HTMLElement&&(this.equityWidth=Math.max(1,Math.floor(t.clientWidth))),e instanceof HTMLElement&&(this.incomeWidth=Math.max(1,Math.floor(e.clientWidth))),this.requestUpdate()})}firstUpdated(){let t=this.renderRoot.querySelector(".equity-bar-wrap"),e=this.renderRoot.querySelector(".income-bar-wrap");t instanceof HTMLElement&&(this.resizeObserver?.observe(t),this.equityWidth=Math.max(1,Math.floor(t.clientWidth))),e instanceof HTMLElement&&(this.resizeObserver?.observe(e),this.incomeWidth=Math.max(1,Math.floor(e.clientWidth))),this.renderD3Bars()}disconnectedCallback(){this.resizeObserver?.disconnect(),this.resizeObserver=null,super.disconnectedCallback()}updated(){this.renderD3Bars()}resolveHasData(){let t=this.hasData;return"string"==typeof t?"true"===t.toLowerCase():!!t}getSvg(t){let e=this.renderRoot.querySelector(t);if(!(e instanceof SVGSVGElement))throw Error(`[smzh-mortgage-affordability-chart] Missing ${t}.`);return eW(e)}renderD3Bars(){this.renderEquityBar(),this.renderIncomeBar()}toFiniteNumber(t,e){return"number"==typeof t&&Number.isFinite(t)?t:e}clampPercent(t,e){return Math.max(0,Math.min(100,this.toFiniteNumber(t,e)))}getSafeText(t,e){if("string"!=typeof t)return e;let r=t.trim();return r.length>0?r:e}getSafeEquityPercent(){return this.clampPercent(this.equityPercent,0)}getSafeMinimumEquityPercent(){return this.clampPercent(this.minimumEquityPercent,0)}getSafeAffordabilityPercent(){return Math.max(0,this.toFiniteNumber(this.affordabilityPercent,0))}getSafeReferenceInterestRate(){return Math.max(0,this.toFiniteNumber(this.referenceInterestRate,5))}getClampedAffordabilityMarkerPercent(){return this.clampPercent(this.affordabilityMarkerPercent,0)}getAffordabilityZone(){let t=this.getSafeAffordabilityPercent();return t<29?"green":t<36?"yellow":"blue"}getIncomeMarkerColor(){let t=this.getAffordabilityZone();return"green"===t?"var(--smzh-color-chart-income-safe)":"yellow"===t?"var(--smzh-color-chart-income-warning)":"var(--smzh-color-chart-income-risk)"}getIncomeMarkerAlignedPercent(){let t=this.getAffordabilityZone();return"green"===t?17:"yellow"===t?51:84}getIncomeMarkerSegment(){let t=this.getAffordabilityZone();return"green"===t?"left":"yellow"===t?"middle":"right"}formatCommaDecimal(t){return(Number.isFinite(t)?t:0).toFixed(2).replace(".",",")}getMinimumEquityLabelAlign(){let t=this.getSafeMinimumEquityPercent();return t<=20?"left":t>=90?"right":"middle"}renderEquityBar(){let t=Math.max(1,this.equityWidth),e=this.getSafeEquityPercent(),r=this.getSafeMinimumEquityPercent(),i=e/100*t,a=this.getSvg(".equity-bar-svg").attr("viewBox",`0 0 ${t} 98`),s=a.selectAll("defs").data([null]).join("defs");s.selectAll("linearGradient#smzh-equity-fill").data([null]).join("linearGradient").attr("id","smzh-equity-fill").attr("x1","0%").attr("y1","0%").attr("x2","0%").attr("y2","100%").selectAll("stop").data([{offset:"0%",color:"#07314C"},{offset:"100%",color:"#58819B"}]).join("stop").attr("offset",t=>t.offset).attr("stop-color",t=>t.color),s.selectAll("linearGradient#smzh-equity-right-fill").data([null]).join("linearGradient").attr("id","smzh-equity-right-fill").attr("x1","0%").attr("y1","100%").attr("x2","0%").attr("y2","0%").selectAll("stop").data([{offset:"0%",color:"#DFE1E6"},{offset:"100%",color:"#F2F2F2"}]).join("stop").attr("offset",t=>t.offset).attr("stop-color",t=>t.color),a.selectAll("rect.zone").data([{x:0,width:i,fill:"url(#smzh-equity-fill)"},{x:i,width:Math.max(0,t-i),fill:"url(#smzh-equity-right-fill)"}]).join("rect").attr("class","zone").attr("x",t=>t.x).attr("y",0).attr("width",t=>t.width).attr("height",98).attr("fill",t=>t.fill),this.resolveHasData()?a.selectAll("line.min-line").data([r/100*t]).join("line").attr("class","min-line").attr("x1",t=>t).attr("x2",t=>t).attr("y1",0).attr("y2",98).attr("stroke","#FFFFFF").attr("stroke-opacity",.4).attr("stroke-width",1).attr("stroke-dasharray","4 4"):a.selectAll("line.min-line").remove(),a.selectAll("circle.min-dot").remove()}renderIncomeBar(){let t=Math.max(1,this.incomeWidth),e=0,r=[{width:.34*t,fill:"var(--smzh-color-chart-income-safe)"},{width:.34*t,fill:"var(--smzh-color-chart-income-warning)"},{width:.32*t,fill:"var(--smzh-color-chart-income-risk)"}].map(t=>{let r={...t,x:e};return e+=t.width,r});this.getSvg(".income-bar-svg").attr("viewBox",`0 0 ${t} 20`).selectAll("rect.seg").data(r).join("rect").attr("class","seg").attr("x",t=>t.x).attr("y",0).attr("width",t=>t.width).attr("height",20).attr("fill",t=>t.fill)}render(){var t,e;let r=this.getSafeText(this.affordabilityLabel,"Ihre Hypothek ist"),i=this.getSafeText(this.affordabilityStatus,"Noch keine Daten"),a=this.getSafeText(this.monthlyTotal,"CHF 0"),s=this.getSafeText(this.monthlyInterest,"CHF 0"),n=this.getSafeReferenceInterestRate(),o=this.getSafeText(this.monthlyInterestTooltip,`Indikativer Referenzzinsatz von ${this.formatCommaDecimal(n)} %`),l=this.getSafeText(this.monthlyUpkeep,"CHF 0"),h=this.getSafeText(this.monthlyUpkeepTooltip,"1% vom Kaufpreis"),c=this.getSafeText(this.monthlyAmortization,"CHF 0"),d=this.getSafeAffordabilityPercent(),p=this.getSafeEquityPercent(),u=this.getSafeMinimumEquityPercent(),m=this.getMinimumEquityLabelAlign(),g="left"===m?"0%":"right"===m?"100%":`${u}%`,f=this.getIncomeMarkerSegment(),v=this.getIncomeMarkerAlignedPercent(),y=this.getIncomeMarkerColor(),b="left"===f?"0%":"right"===f?"100%":`${v}%`,z=this.resolveHasData(),x=z?this.formatCommaDecimal(Math.max(0,100-p)):this.formatCommaDecimal(0);return W`
      <section class="wrap ${z?"":"wrap--empty"}">
        <div class="header">
          <h3>${r}</h3>
          <div class="pill">${i}</div>
        </div>

        <article class="card">
          <div class="legend">
            <div class="left"><span class="dot"></span>Eigenmittel</div>
            <div class="right">Höhe der Hypothek<span class="dot"></span></div>
          </div>

          <div class="equity-group">
            <div class="equity-bar-wrap">
              <svg class="equity-bar-svg" aria-hidden="true"></svg>
              <div class="equity-values" aria-hidden="true">
                <span class="left"
                  >${z?`${this.formatCommaDecimal(p)}%`:""}</span
                >
                <span class="right">${x}%</span>
              </div>
            </div>
            <div
              class="minimum-dot"
              aria-hidden="true"
              style="left: ${u}%;"
            ></div>
            <div
              class="minimum-label"
              data-align=${m}
              style="left: ${g};"
            >
              Minimum an Eigenmitteln
            </div>
          </div>
        </article>

        <article class="income-card">
          <div class="income-row">
            <div class="income-value">
              ${this.formatCommaDecimal(d)}%
            </div>
            <div class="income-copy" lang="de">
              Ihres Einkommens werden zur Deckung der Hypotheken­kosten
              <smzh-tooltip placement="top" mode="dark">
                <button
                  type="button"
                  slot="trigger"
                  class="income-tooltip-trigger"
                  aria-label="Information zur Einkommensbelastung"
                >
                  benötigt
                </button>
                <div class="income-tooltip-content">
                  <div>
                    Die Einkommensbelastung bezeichnet das Total folgender
                    Aufwendungen im Verhältnis zu Ihrem Nettoeinkommen:
                  </div>
                  <ul>
                    <li>
                      Hypothekarzinsen auf Basis eines langfristigen
                      Durchschnittszinssatzes von 5%
                    </li>
                    <li>Amortisationen</li>
                    <li>Unterhalts- &amp; Nebenkosten</li>
                  </ul>
                </div>
              </smzh-tooltip>
              .
            </div>
          </div>

          <div class="income-bar-wrap">
            <svg class="income-bar-svg" aria-hidden="true"></svg>
            <div
              class="income-marker"
              aria-hidden="true"
              style="left: ${v}%; border-top-color: ${y};"
            ></div>
          </div>
          <div
            class="income-label"
            data-align=${f}
            style="left: ${b};"
          >
            Ihre Einkommensbelastung
          </div>

          <div class="table">
            <div class="table-row">
              <strong>Monatliche Zahlungen gesamt</strong>
              <span class="value">${a}</span>
            </div>
            <div class="table-row">
              <span class="muted">
                <span class="table-label-with-tooltip">
                  <span>Monatliche Zinszahlung</span>
                  <smzh-tooltip placement="top" mode="dark">
                    <button
                      type="button"
                      slot="trigger"
                      class="table-tooltip-trigger"
                      aria-label="Information zur monatlichen Zinszahlung"
                    >
                      ${t={size:16},tS.info(t)}
                    </button>
                    ${o}
                  </smzh-tooltip>
                </span>
              </span>
              <span class="value">${s}</span>
            </div>
            <div class="table-row">
              <span class="muted">
                <span class="table-label-with-tooltip">
                  <span>Unterhalts - und Nebenkosten</span>
                  <smzh-tooltip placement="top" mode="dark">
                    <button
                      type="button"
                      slot="trigger"
                      class="table-tooltip-trigger"
                      aria-label="Information zu Unterhalts- und Nebenkosten"
                    >
                      ${e={size:16},tS.info(e)}
                    </button>
                    ${h}
                  </smzh-tooltip>
                </span>
              </span>
              <span class="value">${l}</span>
            </div>
            <div class="table-row">
              <span class="muted">Amortisationskosten</span>
              <span class="value">${c}</span>
            </div>
          </div>
        </article>
      </section>
    `}});let ia=Symbol.for(""),is=t=>{if(t?.r===ia)return t?._$litStatic$},io=new Map,il=t=>(e,...r)=>{let i,a,s=r.length,n=[],o=[],l,h=0,c=!1;for(;h<s;){for(l=e[h];h<s&&void 0!==(i=is(a=r[h]));)l+=i+e[++h],c=!0;h!==s&&o.push(a),n.push(l),h++}if(h===s&&n.push(e[s]),c){let t=n.join("$$lit$$");void 0===(e=io.get(t))&&(n.raw=n,io.set(t,e=n)),r=o}return t(e,...r)},ih=il(W);il(G),il(X);let ic=l`
  :host {
    display: inline;
    color: var(--smzh-color-text-default);
    text-align: inherit;
  }

  .typography {
    margin: 0;
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-size);
    line-height: var(--smzh-typography-line-height);
    letter-spacing: var(--smzh-typography-letter-spacing, 0em);
    font-weight: var(--smzh-typography-weight);
    text-align: inherit;
    color: inherit;
  }

  :host([align="inherit"]) {
    text-align: inherit;
  }
  :host([align="left"]) {
    display: block;
    width: 100%;
    text-align: left;
  }
  :host([align="center"]) {
    display: block;
    width: 100%;
    text-align: center;
  }
  :host([align="right"]) {
    display: block;
    width: 100%;
    text-align: right;
  }

  .typography[data-weight="normal"] {
    --smzh-typography-weight: var(--smzh-font-weight-normal);
  }
  .typography[data-weight="regular"] {
    --smzh-typography-weight: var(--smzh-font-weight-regular);
  }
  .typography[data-weight="medium"] {
    --smzh-typography-weight: var(--smzh-font-weight-medium);
  }
  .typography[data-decoration="none"] {
    text-decoration: none;
  }
  .typography[data-decoration="underline"] {
    text-decoration: underline;
  }
  .typography[data-decoration="line-through"] {
    text-decoration: line-through;
  }
  .typography[data-font-style="normal"] {
    font-style: normal;
  }
  .typography[data-font-style="italic"] {
    font-style: italic;
  }

  .typography[data-variant="heading-h1"] {
    --smzh-typography-size: var(--smzh-typography-heading-h1-font-size);
    --smzh-typography-line-height: var(
      --smzh-typography-heading-h1-line-height
    );
    --smzh-typography-letter-spacing: var(
      --smzh-typography-heading-h1-letter-spacing-book
    );
  }
  .typography[data-variant="heading-h1"][data-weight="medium"] {
    --smzh-typography-letter-spacing: var(
      --smzh-typography-heading-h1-letter-spacing-medium
    );
  }
  .typography[data-variant="heading-h2"] {
    --smzh-typography-size: var(--smzh-typography-heading-h2-font-size);
    --smzh-typography-line-height: var(
      --smzh-typography-heading-h2-line-height
    );
    --smzh-typography-letter-spacing: var(
      --smzh-typography-heading-h2-letter-spacing-book
    );
  }
  .typography[data-variant="heading-h2"][data-weight="medium"] {
    --smzh-typography-letter-spacing: var(
      --smzh-typography-heading-h2-letter-spacing-medium
    );
  }
  .typography[data-variant="heading-h3"] {
    --smzh-typography-size: var(--smzh-typography-heading-h3-font-size);
    --smzh-typography-line-height: var(
      --smzh-typography-heading-h3-line-height
    );
    --smzh-typography-letter-spacing: var(
      --smzh-typography-heading-h3-letter-spacing
    );
  }
  .typography[data-variant="heading-h4"] {
    --smzh-typography-size: var(--smzh-typography-heading-h4-font-size);
    --smzh-typography-line-height: var(
      --smzh-typography-heading-h4-line-height
    );
    --smzh-typography-letter-spacing: var(
      --smzh-typography-heading-h4-letter-spacing
    );
  }
  .typography[data-variant="text-xl"] {
    --smzh-typography-size: var(--smzh-typography-text-xl-font-size);
    --smzh-typography-line-height: var(--smzh-typography-text-xl-line-height);
    --smzh-typography-letter-spacing: var(
      --smzh-typography-text-xl-letter-spacing
    );
  }
  .typography[data-variant="text-lg"] {
    --smzh-typography-size: var(--smzh-typography-text-lg-font-size);
    --smzh-typography-line-height: var(--smzh-typography-text-lg-line-height);
    --smzh-typography-letter-spacing: var(
      --smzh-typography-text-lg-letter-spacing
    );
  }
  .typography[data-variant="text-md"] {
    --smzh-typography-size: var(--smzh-typography-text-md-font-size);
    --smzh-typography-line-height: var(--smzh-typography-text-md-line-height);
    --smzh-typography-letter-spacing: var(
      --smzh-typography-text-md-letter-spacing
    );
  }
  .typography[data-variant="text-sm"] {
    --smzh-typography-size: var(--smzh-typography-text-sm-font-size);
    --smzh-typography-line-height: var(--smzh-typography-text-sm-line-height);
    --smzh-typography-letter-spacing: var(
      --smzh-typography-text-sm-letter-spacing
    );
  }
  .typography[data-variant="text-xs"] {
    --smzh-typography-size: var(--smzh-typography-text-xs-font-size);
    --smzh-typography-line-height: var(--smzh-typography-text-xs-line-height);
    --smzh-typography-letter-spacing: var(
      --smzh-typography-text-xs-letter-spacing
    );
  }
  .typography[data-variant="label-lg"] {
    --smzh-typography-size: var(--smzh-typography-label-lg-font-size);
    --smzh-typography-line-height: var(--smzh-typography-label-lg-line-height);
    --smzh-typography-letter-spacing: var(
      --smzh-typography-label-lg-letter-spacing
    );
  }
  .typography[data-variant="label-md"] {
    --smzh-typography-size: var(--smzh-typography-label-md-font-size);
    --smzh-typography-line-height: var(--smzh-typography-label-md-line-height);
    --smzh-typography-letter-spacing: var(
      --smzh-typography-label-md-letter-spacing
    );
  }
  .typography[data-variant="label-sm"] {
    --smzh-typography-size: var(--smzh-typography-label-sm-font-size);
    --smzh-typography-line-height: var(--smzh-typography-label-sm-line-height);
    --smzh-typography-letter-spacing: var(
      --smzh-typography-label-sm-letter-spacing
    );
  }
  .typography[data-variant="label-xs"] {
    --smzh-typography-size: var(--smzh-typography-label-xs-font-size);
    --smzh-typography-line-height: var(--smzh-typography-label-xs-line-height);
    --smzh-typography-letter-spacing: var(
      --smzh-typography-label-xs-letter-spacing
    );
  }
  .typography[data-variant="overline-lg"] {
    --smzh-typography-size: var(--smzh-typography-overline-lg-font-size);
    --smzh-typography-line-height: var(
      --smzh-typography-overline-lg-line-height
    );
    --smzh-typography-letter-spacing: var(
      --smzh-typography-overline-lg-letter-spacing
    );
    text-transform: uppercase;
  }
  .typography[data-variant="overline-sm"] {
    --smzh-typography-size: var(--smzh-typography-overline-sm-font-size);
    --smzh-typography-line-height: var(
      --smzh-typography-overline-sm-line-height
    );
    --smzh-typography-letter-spacing: var(
      --smzh-typography-overline-sm-letter-spacing
    );
    text-transform: uppercase;
  }

  /* Mobile heading scale from Mobile Headings */
  @media (max-width: 767px) {
    .typography[data-variant="heading-h1"] {
      --smzh-typography-size: var(
        --smzh-typography-heading-h1-mobile-font-size
      );
      --smzh-typography-line-height: var(
        --smzh-typography-heading-h1-mobile-line-height
      );
      --smzh-typography-letter-spacing: var(
        --smzh-typography-heading-h1-mobile-letter-spacing
      );
    }
    .typography[data-variant="heading-h2"] {
      --smzh-typography-size: var(
        --smzh-typography-heading-h2-mobile-font-size
      );
      --smzh-typography-line-height: var(
        --smzh-typography-heading-h2-mobile-line-height
      );
      --smzh-typography-letter-spacing: var(
        --smzh-typography-heading-h2-mobile-letter-spacing-book
      );
    }
    .typography[data-variant="heading-h2"][data-weight="medium"] {
      --smzh-typography-letter-spacing: var(
        --smzh-typography-heading-h2-mobile-letter-spacing-medium
      );
    }
    .typography[data-variant="heading-h3"] {
      --smzh-typography-size: var(
        --smzh-typography-heading-h3-mobile-font-size
      );
      --smzh-typography-line-height: var(
        --smzh-typography-heading-h3-mobile-line-height
      );
      --smzh-typography-letter-spacing: var(
        --smzh-typography-heading-h3-mobile-letter-spacing
      );
    }
    .typography[data-variant="heading-h4"] {
      --smzh-typography-size: var(
        --smzh-typography-heading-h4-mobile-font-size
      );
      --smzh-typography-line-height: var(
        --smzh-typography-heading-h4-mobile-line-height
      );
      --smzh-typography-letter-spacing: var(
        --smzh-typography-heading-h4-mobile-letter-spacing
      );
    }
  }
`,id=["h1","h2","h3","h4","p","span"],ip=["text-xl","text-lg","text-md","text-sm","text-xs","label-lg","label-md","label-sm","label-xs","overline-lg","overline-sm"],iu=["regular","normal","medium"],im="normal",ig=["none","underline","line-through"],iv="none",iy=["normal","italic"],ib="normal",iz=["inherit","left","center","right"],ix="inherit",iw={h1:"heading-h1",h2:"heading-h2",h3:"heading-h3",h4:"heading-h4",p:"text-md",span:"text-md"};"u">typeof window&&!customElements.get("smzh-typography")&&customElements.define("smzh-typography",class extends tp{static styles=ic;static properties={as:{type:String,reflect:!0},variant:{type:String,reflect:!0},weight:{type:String,reflect:!0},decoration:{type:String,reflect:!0},fontStyle:{type:String,attribute:"font-style",reflect:!0},align:{type:String,reflect:!0}};constructor(){super(),this.variant=void 0,this.weight=im,this.decoration=iv,this.fontStyle=ib,this.align=ix}resolveTag(){var t;return"string"==typeof(t=this.as)&&id.includes(t)?this.as:"p"}resolveVariant(t){var e;return"string"==typeof(e=this.variant)&&ip.includes(e)?this.variant:iw[t]??"text-md"}resolveWeight(){var t;return"string"==typeof(t=this.weight)&&iu.includes(t)?this.weight:im}resolveAlign(){var t;return"string"==typeof(t=this.align)&&iz.includes(t)?this.align:ix}resolveDecoration(){var t;return"string"==typeof(t=this.decoration)&&ig.includes(t)?this.decoration:iv}resolveFontStyle(){var t;return"string"==typeof(t=this.fontStyle)&&iy.includes(t)?this.fontStyle:ib}render(){let t=this.resolveTag(),e={_$litStatic$:t,r:ia},r=this.resolveVariant(t),i=this.resolveWeight(),a=this.resolveDecoration(),s=this.resolveFontStyle(),n=this.resolveAlign();return ih`<${e}
      class="typography"
      data-variant=${r}
      data-weight=${i}
      data-decoration=${a}
      data-font-style=${s}
      data-align=${n}
    >
      <slot></slot>
    </${e}>`}});let i$=l`
  :host {
    box-sizing: border-box;
    color: var(--smzh-color-error);
    display: block;
    width: 100%;
  }

  :host([hidden]) {
    display: none !important;
  }

  .root {
    align-items: flex-start;
    background: var(--smzh-color-error-subtle);
    border-radius: var(--smzh-error-callout-radius, var(--smzh-spacing-sm));
    box-sizing: border-box;
    color: inherit;
    display: flex;
    gap: var(--smzh-spacing-sm);
    padding: var(--smzh-spacing-sm) var(--smzh-spacing-x-sm);
    width: 100%;
  }

  .icon {
    color: inherit;
    display: inline-flex;
    flex: 0 0 auto;
    line-height: 0;
    margin-top: 3px;
  }

  .icon svg {
    display: block;
  }

  .content {
    color: inherit;
    display: flex;
    flex: 1 1 auto;
    flex-direction: column;
    gap: var(--smzh-spacing-xxx-sm);
    min-width: 0;
  }

  .title smzh-typography,
  .body smzh-typography {
    color: inherit;
    display: block;
  }
`;"u">typeof window&&!customElements.get("smzh-error-callout")&&customElements.define("smzh-error-callout",class extends tp{static styles=i$;static properties={title:{type:String,reflect:!0},body:{type:String,reflect:!0}};constructor(){super(),this.title="Error state",this.body="Error description"}hasSlottedContent(t){return Array.from(this.children).some(e=>e.getAttribute("slot")===t)}hasTextContent(t){return"string"==typeof t&&t.trim().length>0}render(){var t;let e=this.hasSlottedContent("title")||this.hasTextContent(this.title),r=this.hasSlottedContent("body")||this.hasTextContent(this.body),i=e||r;return i?W`
      <article class="root" role="alert">
        <div class="icon">
          <slot name="icon"
            >${t={stroke:"var(--smzh-color-error)"},tS["alert-circle"](t)}</slot
          >
        </div>

        ${i?W`
              <div class="content">
                ${e?W`
                      <div class="title">
                        <slot name="title">
                          <smzh-typography
                            as="p"
                            variant="text-sm"
                            weight="medium"
                          >
                            ${this.title}
                          </smzh-typography>
                        </slot>
                      </div>
                    `:Z}
                ${r?W`
                      <div class="body">
                        <slot name="body">
                          <smzh-typography
                            as="p"
                            variant="text-sm"
                            weight="normal"
                          >
                            ${this.body}
                          </smzh-typography>
                        </slot>
                      </div>
                    `:Z}
              </div>
            `:Z}
      </article>
    `:Z}});let ik=l`
  :host {
    display: inline-block;
    width: var(--smzh-link-host-width, auto);
  }

  .link[data-full-width="true"] {
    width: 100%;
    box-sizing: border-box;
  }

  .link {
    --smzh-link-radius: 24px;
    --smzh-link-px: var(--smzh-spacing-x-sm);
    --smzh-link-py: var(--smzh-spacing-xxx-sm);
    --smzh-link-resolved-font-size: var(
      --smzh-link-font-size,
      var(--smzh-typography-text-md-font-size)
    );
    --smzh-link-resolved-line-height: var(
      --smzh-link-line-height,
      var(--smzh-typography-text-md-line-height)
    );
    --smzh-link-resolved-letter-spacing: var(
      --smzh-link-letter-spacing,
      var(--smzh-typography-text-md-letter-spacing)
    );

    align-items: center;
    background: transparent;
    border: 1px solid var(--smzh-color-primary-subtle);
    border-radius: var(--smzh-link-radius);
    color: var(--smzh-link-color, var(--smzh-color-primary-active));
    cursor: pointer;
    display: inline-flex;
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-link-resolved-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    justify-content: center;
    letter-spacing: var(--smzh-link-resolved-letter-spacing);
    line-height: var(--smzh-link-resolved-line-height);
    padding: var(--smzh-link-py) var(--smzh-link-px);
    text-align: center;
    text-decoration: none;
    transition:
      background-color 140ms ease,
      border-color 140ms ease,
      color 140ms ease,
      box-shadow 140ms ease,
      opacity 140ms ease;
    white-space: nowrap;
  }

  .icon {
    align-items: center;
    display: inline-flex;
    flex: 0 0 auto;
    height: 20px;
    justify-content: center;
    width: 20px;
  }

  .link[data-has-icon="true"] {
    gap: var(--smzh-spacing-xx-sm);
  }

  .link[data-size="sm"] {
    padding: var(--smzh-spacing-xxx-sm) var(--smzh-spacing-x-sm);
  }

  .link[data-size="md"] {
    padding: var(--smzh-spacing-xx-sm) var(--smzh-spacing-md);
  }

  .link[data-size="lg"] {
    padding: var(--smzh-spacing-x-sm) var(--smzh-spacing-x-md);
  }

  .link[data-shape="pill"] {
    --smzh-link-radius: 24px;
  }

  .link[data-shape="rounded"] {
    --smzh-link-radius: var(--smzh-spacing-xxx-sm);
  }

  .link[data-variant="primary"] {
    background: var(--smzh-color-primary-active);
    border-color: var(--smzh-color-primary-active);
    color: var(--smzh-color-text-on-primary);
  }

  .link[data-variant="primary"]:hover:not([aria-disabled="true"]) {
    background: var(--smzh-color-primary);
    border-color: var(--smzh-color-primary);
  }

  .link[data-variant="primary"]:active:not([aria-disabled="true"]) {
    background: var(--smzh-color-primary-hover);
    border-color: var(--smzh-color-primary-hover);
  }

  .link[data-variant="secondary"] {
    background: var(--smzh-color-surface);
    border-color: var(--smzh-color-border-focus);
    color: var(--smzh-color-primary-active);
  }

  .link[data-variant="secondary"]:hover:not([aria-disabled="true"]) {
    border-color: var(--smzh-color-primary);
    box-shadow: var(--smzh-color-shadow-xs);
    color: var(--smzh-color-primary);
  }

  .link[data-variant="secondary"]:active:not([aria-disabled="true"]) {
    border-color: var(--smzh-color-primary-active);
    box-shadow: none;
    color: var(--smzh-color-primary-active);
  }

  .link[data-variant="link"] {
    background: transparent;
    border-width: 0;
    color: var(--smzh-link-link-color, var(--smzh-color-primary-active));
    padding: 0;
  }

  .link[data-variant="link"][data-has-icon="true"][data-icon-position="leading"] {
    padding-left: 0;
  }

  .link[data-variant="link"][data-has-icon="true"][data-icon-position="trailing"] {
    padding-right: 0;
  }

  .link[data-variant="link"]:hover:not([aria-disabled="true"]) {
    color: var(--smzh-link-link-hover-color, var(--smzh-color-primary-hover));
  }

  .link[data-variant="link"]:active:not([aria-disabled="true"]) {
    color: var(--smzh-link-link-active-color, var(--smzh-color-primary));
  }

  .link[data-variant="link"]:hover:not([aria-disabled="true"]),
  .link[data-variant="link"]:active:not([aria-disabled="true"]) {
    text-decoration: underline;
  }

  .link[aria-disabled="true"] {
    cursor: default;
    opacity: 0.56;
    pointer-events: none;
    text-decoration: none;
  }

  .link:focus-visible {
    outline: 2px solid var(--smzh-color-border-focus);
    outline-offset: 2px;
  }
`,iS=["_self","_blank"],i_=["primary","secondary","link"],iA=["sm","md","lg"],iM=["pill","rounded"],iC=["leading","trailing"],iE="link",iT="pill",iN="leading";"u">typeof window&&!customElements.get("smzh-link")&&customElements.define("smzh-link",class extends tp{static styles=ik;static properties={href:{type:String,reflect:!0},target:{type:String,reflect:!0},rel:{type:String,reflect:!0},variant:{type:String,reflect:!0},size:{type:String,reflect:!0},shape:{type:String,reflect:!0},icon:{type:String,reflect:!0},iconPosition:{type:String,attribute:"icon-position",reflect:!0},fullWidth:{type:Boolean,attribute:"full-width",reflect:!0},disabled:{type:Boolean,reflect:!0},ariaLabel:{type:String,attribute:"aria-label"}};constructor(){super(),this.href=void 0,this.target=void 0,this.rel=void 0,this.variant=iE,this.size="sm",this.shape=iT,this.icon=void 0,this.iconPosition=iN,this.fullWidth=!1,this.disabled=!1,this.ariaLabel=null}disconnectedCallback(){this.style.removeProperty("--smzh-link-host-width"),super.disconnectedCallback()}willUpdate(t){super.willUpdate(t),t.has("fullWidth")&&this.syncHostFullWidth()}resolveVariant(){var t;return"string"==typeof(t=this.variant)&&i_.includes(t)?this.variant:iE}isFullWidthActive(){return!0===this.fullWidth}syncHostFullWidth(){this.isFullWidthActive()?this.style.setProperty("--smzh-link-host-width","100%"):this.style.removeProperty("--smzh-link-host-width")}resolveSize(){var t;return"string"==typeof(t=this.size)&&iA.includes(t)?this.size:"sm"}resolveShape(){var t;return"string"==typeof(t=this.shape)&&iM.includes(t)?this.shape:iT}resolveIconPosition(){var t;return"string"==typeof(t=this.iconPosition)&&iC.includes(t)?this.iconPosition:iN}resolveIcon(){if(t_(this.icon))return this.icon}resolveTarget(){var t;if("string"==typeof(t=this.target)&&iS.includes(t))return this.target}resolveRel(t){return"string"==typeof this.rel&&this.rel.trim().length>0?this.rel:"_blank"===t?"noreferrer noopener":void 0}resolveAriaLabel(){if("string"==typeof this.ariaLabel&&this.ariaLabel.trim().length>0)return this.ariaLabel;let t=this.getAttribute("aria-label");if("string"==typeof t&&t.trim().length>0)return t}renderIcon(){let t=this.resolveIcon();return t?W`<span class="icon" aria-hidden="true"
      >${tS[t](void 0)}</span
    >`:null}render(){let t=this.resolveTarget(),e=this.resolveRel(t),r=this.disabled?void 0:this.href,i=this.resolveAriaLabel(),a=this.renderIcon(),s=this.resolveIconPosition();return W`
      <a
        class="link"
        href=${r??Z}
        target=${t??Z}
        rel=${e??Z}
        aria-label=${i??Z}
        aria-disabled=${this.disabled?"true":"false"}
        tabindex=${(this.disabled?"-1":void 0)??Z}
        data-variant=${this.resolveVariant()}
        data-size=${this.resolveSize()}
        data-shape=${this.resolveShape()}
        data-has-icon=${a?"true":"false"}
        data-icon-position=${s}
        data-full-width=${this.fullWidth?"true":"false"}
      >
        ${a&&"leading"===s?a:null}
        <slot></slot>
        ${a&&"trailing"===s?a:null}
      </a>
    `}});let iI=l`
  :host {
    box-sizing: border-box;
    color: var(--smzh-color-text-default);
    display: block;
    width: 100%;
  }

  :host([hidden]) {
    display: none !important;
  }

  .root {
    align-items: flex-start;
    background: var(--smzh-color-surface);
    border: 1px solid var(--smzh-color-border-default);
    border-radius: var(
      --smzh-recommendation-callout-radius,
      var(--smzh-spacing-sm)
    );
    box-sizing: border-box;
    display: flex;
    gap: var(--smzh-spacing-sm);
    overflow: clip;
    padding: var(--smzh-spacing-x-sm);
    width: 100%;
  }

  .icon-tile {
    align-items: center;
    background: var(--smzh-color-recommendation-callout-icon-background);
    border-radius: var(--smzh-spacing-x-sm);
    color: var(--smzh-color-recommendation-callout-icon-stroke);
    display: inline-flex;
    flex: 0 0 auto;
    justify-content: center;
    padding: var(--smzh-recommendation-callout-icon-padding, 18px);
  }

  .icon-tile svg {
    display: block;
  }

  .content {
    display: flex;
    flex: 1 1 auto;
    flex-direction: column;
    gap: var(--smzh-spacing-xxx-sm);
    min-width: 0;
  }

  .title smzh-typography {
    color: var(--smzh-color-text-strong);
    display: block;
  }

  .body smzh-typography {
    color: var(
      --smzh-recommendation-callout-body-color,
      var(--smzh-color-text-disabled)
    );
    display: block;
  }

  .action-text {
    color: var(--smzh-color-primary);
    display: inline-flex;
  }

  .action-text smzh-typography {
    color: inherit;
    display: block;
  }
`,iP=["_self","_blank"],iL="thumbs-up";"u">typeof window&&!customElements.get("smzh-recommendation-callout")&&customElements.define("smzh-recommendation-callout",class extends tp{static styles=iI;static properties={title:{type:String,reflect:!0},body:{type:String,reflect:!0},ctaLabel:{type:String,attribute:"cta-label",reflect:!0},ctaHref:{type:String,attribute:"cta-href",reflect:!0},ctaTarget:{type:String,attribute:"cta-target",reflect:!0},icon:{type:String,reflect:!0},iconBackground:{type:String,attribute:"icon-background",reflect:!0},iconStroke:{type:String,attribute:"icon-stroke",reflect:!0}};constructor(){super(),this.title="Ihr offerierter Zinssatz ist über Marktniveau",this.body="Fordern Sie jetzt eine Offerte bei uns an – wir senken Ihre Finanzierungskosten.",this.ctaLabel="Jetzt bessere Konditionen finden",this.ctaHref=void 0,this.ctaTarget=void 0,this.icon=iL,this.iconBackground="var(--smzh-color-success-subtle)",this.iconStroke="var(--smzh-success-500)"}resolveCtaTarget(){var t;if("string"==typeof(t=this.ctaTarget)&&iP.includes(t))return this.ctaTarget}resolveCtaRel(t){return"_blank"===t?"noreferrer noopener":void 0}resolveIcon(){return t_(this.icon)?this.icon:iL}hasSlottedContent(t){return Array.from(this.children).some(e=>e.getAttribute("slot")===t)}hasTextContent(t){return"string"==typeof t&&t.trim().length>0}renderAction(){if(!this.ctaLabel)return Z;let t=this.resolveCtaTarget();return this.ctaHref?W`
        <smzh-link
          href=${this.ctaHref}
          target=${t??Z}
          rel=${this.resolveCtaRel(t)??Z}
          variant="link"
          size="md"
          icon="chevron-right"
          icon-position="trailing"
        >
          ${this.ctaLabel}
        </smzh-link>
      `:W`
      <span class="action-text">
        <smzh-typography as="span" variant="text-sm" weight="medium">
          ${this.ctaLabel}
        </smzh-typography>
      </span>
    `}render(){var t;let e=this.resolveIcon(),r=this.hasSlottedContent("title")||this.hasTextContent(this.title),i=this.hasSlottedContent("body")||this.hasTextContent(this.body),a=this.hasSlottedContent("action")||this.hasTextContent(this.ctaLabel);return W`
      <article
        class="root"
        style=${`--smzh-color-recommendation-callout-icon-background: ${this.iconBackground}; --smzh-color-recommendation-callout-icon-stroke: ${this.iconStroke};`}
      >
        <div class="icon-tile">
          <slot name="icon"
            >${t={stroke:this.iconStroke,size:20},tS[e](t)}</slot
          >
        </div>

        ${r||i||a?W`
              <div class="content">
                ${r?W`
                      <div class="title">
                        <slot name="title">
                          <smzh-typography
                            as="p"
                            variant="text-sm"
                            weight="medium"
                          >
                            ${this.title}
                          </smzh-typography>
                        </slot>
                      </div>
                    `:Z}
                ${i?W`
                      <div class="body">
                        <slot name="body">
                          <smzh-typography
                            as="p"
                            variant="text-sm"
                            weight="regular"
                          >
                            ${this.body}
                          </smzh-typography>
                        </slot>
                      </div>
                    `:Z}
                ${a?W`
                      <div class="action-row">
                        <slot name="action">${this.renderAction()}</slot>
                      </div>
                    `:Z}
              </div>
            `:Z}
      </article>
    `}});let iR=l`
  :host {
    display: inline-flex;
    vertical-align: middle;
  }

  :host([hidden]) {
    display: none !important;
  }

  .avatar {
    align-items: center;
    border-radius: 50%;
    box-sizing: border-box;
    display: inline-flex;
    flex-shrink: 0;
    justify-content: center;
    overflow: hidden;
  }

  :host([data-grouped]) .avatar {
    box-shadow: 0 0 0 var(--smzh-avatar-ring-width, 2px)
      var(--smzh-color-surface);
  }

  .avatar[data-size="xs"] {
    height: var(--smzh-spacing-x-big);
    width: var(--smzh-spacing-x-big);
  }

  .avatar[data-size="sm"] {
    height: var(--smzh-spacing-xxx-big);
    width: var(--smzh-spacing-xxx-big);
  }

  .avatar[data-size="md"] {
    height: var(--smzh-spacing-lg);
    width: var(--smzh-spacing-lg);
  }

  .avatar[data-size="xl"] {
    height: 44px;
    width: 44px;
  }

  .avatar[data-type="image"] {
    background: var(--smzh-color-background);
  }

  .avatar[data-type="placeholder"],
  .avatar[data-type="initials"] {
    background: var(--smzh-color-primary-subtle);
  }

  .image {
    border-radius: 50%;
    display: block;
    height: 100%;
    object-fit: cover;
    width: 100%;
  }

  .initials {
    color: var(--smzh-color-primary);
    font-family: var(--smzh-font-family-sans);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    line-height: 1;
    text-transform: uppercase;
    user-select: none;
  }

  .avatar[data-size="xs"] .initials {
    font-size: var(--smzh-typography-text-xs-font-size);
  }

  .avatar[data-size="sm"] .initials {
    font-size: var(--smzh-typography-text-sm-font-size);
  }

  .avatar[data-size="md"] .initials {
    font-size: var(--smzh-typography-text-md-font-size);
  }

  .avatar[data-size="xl"] .initials {
    font-size: var(--smzh-typography-text-md-font-size);
  }

  .placeholder-icon {
    color: var(--smzh-color-primary);
    display: flex;
  }

  .avatar[data-size="xs"] .placeholder-icon {
    height: var(--smzh-spacing-sm);
    width: var(--smzh-spacing-sm);
  }

  .avatar[data-size="sm"] .placeholder-icon {
    height: 18px;
    width: 18px;
  }

  .avatar[data-size="md"] .placeholder-icon {
    height: 22px;
    width: 22px;
  }

  .avatar[data-size="xl"] .placeholder-icon {
    height: var(--smzh-spacing-x-big);
    width: var(--smzh-spacing-x-big);
  }

  .placeholder-icon svg {
    height: 100%;
    width: 100%;
  }
`,iD=["xs","sm","md","xl"];class iF extends tp{static styles=iR;static properties={src:{type:String,reflect:!0},alt:{type:String,reflect:!0},initials:{type:String,reflect:!0},size:{type:String,reflect:!0}};imageError=!1;constructor(){super(),this.src=void 0,this.alt=void 0,this.initials=void 0,this.size="md"}resolveSize(){var t;return"string"==typeof(t=this.size)&&iD.includes(t)?this.size:"md"}resolveType(){return this.src&&!this.imageError?"image":this.initials&&this.initials.trim().length>0?"initials":"placeholder"}accessibleName(){if(void 0===this.alt||null===this.alt)return;let t=String(this.alt).trim();return t.length>0?t:void 0}handleImageError(){this.imageError=!0,this.requestUpdate()}willUpdate(t){t.has("src")&&(this.imageError=!1)}renderInitialsOrPlaceholder(t){if("initials"===t){let t=(this.initials??"").trim().slice(0,2).toUpperCase();return W`<span class="initials" aria-hidden="true">${t}</span>`}return W`<span class="placeholder-icon" aria-hidden="true"
      >${iF.userIcon}</span
    >`}render(){let t=this.resolveSize(),e=this.resolveType(),r=this.accessibleName();if("image"===e)return W`
        <span class="avatar" data-size=${t} data-type="image">
          <img
            class="image"
            src=${this.src}
            alt=${r??""}
            @error=${this.handleImageError}
          />
        </span>
      `;let i=void 0===r;return W`
      <span
        class="avatar"
        data-size=${t}
        data-type=${e}
        role=${i?Z:"img"}
        aria-label=${i?Z:r}
        aria-hidden=${i?"true":Z}
      >
        ${this.renderInitialsOrPlaceholder(e)}
      </span>
    `}static userIcon=G`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>`}"u">typeof window&&!customElements.get("smzh-avatar")&&customElements.define("smzh-avatar",iF);let ij=l`
  :host {
    display: inline-flex;
    vertical-align: middle;
    --smzh-avatar-group-overlap: -12px;
  }

  :host([size="xs"]) {
    --smzh-avatar-group-overlap: -6px;
  }

  :host([size="sm"]) {
    --smzh-avatar-group-overlap: -10px;
  }

  :host([size="md"]) {
    --smzh-avatar-group-overlap: -12px;
  }

  :host([size="xl"]) {
    --smzh-avatar-group-overlap: -14px;
  }

  :host([hidden]) {
    display: none !important;
  }

  .group {
    align-items: center;
    display: flex;
    flex-direction: row;
    isolation: isolate;
  }

  ::slotted(smzh-avatar) {
    position: relative;
  }

  :host([size="xs"]) ::slotted(smzh-avatar) {
    --smzh-avatar-ring-width: 1.5px;
  }

  .overflow {
    align-items: center;
    background: var(--smzh-color-primary-subtle);
    border-radius: 50%;
    box-shadow: 0 0 0 2px var(--smzh-color-surface);
    box-sizing: border-box;
    color: var(--smzh-color-primary);
    display: inline-flex;
    font-family: var(--smzh-font-family-sans);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    justify-content: center;
    line-height: 1;
    position: relative;
    user-select: none;
  }

  :host([size="xs"]) .overflow {
    box-shadow: 0 0 0 1.5px var(--smzh-color-surface);
    font-size: var(--smzh-typography-text-xs-font-size);
    height: var(--smzh-spacing-x-big);
    width: var(--smzh-spacing-x-big);
  }

  :host([size="sm"]) .overflow {
    font-size: var(--smzh-typography-text-xs-font-size);
    height: var(--smzh-spacing-xxx-big);
    width: var(--smzh-spacing-xxx-big);
  }

  :host([size="md"]) .overflow,
  .overflow {
    font-size: var(--smzh-typography-text-sm-font-size);
    height: var(--smzh-spacing-lg);
    width: var(--smzh-spacing-lg);
  }

  :host([size="xl"]) .overflow {
    font-size: var(--smzh-typography-text-md-font-size);
    height: 44px;
    width: 44px;
  }
`,iH=["xs","sm","md","xl"];"u">typeof window&&!customElements.get("smzh-avatar-group")&&customElements.define("smzh-avatar-group",class extends tp{static styles=ij;static properties={size:{type:String,reflect:!0},max:{type:Number,reflect:!0},_overflowCount:{state:!0}};lastSyncedAvatars=[];childListObserver;constructor(){super(),this.size="md",this.max=void 0,this._overflowCount=0}resolveSize(){var t;return"string"==typeof(t=this.size)&&iH.includes(t)?this.size:"md"}syncAvatarChildren(){let t=this.getAvatarChildren();for(let e of this.lastSyncedAvatars)t.includes(e)||(e.removeAttribute("data-grouped"),e.style.removeProperty("margin-left"),e.style.removeProperty("display"));let e=this.resolveSize(),r="number"==typeof this.max&&this.max>0?this.max:t.length;this._overflowCount=Math.max(0,t.length-r);for(let i=0;i<t.length;i++){let a=t[i];a.size=e,a.setAttribute("data-grouped",""),i>0?a.style.setProperty("margin-left","var(--smzh-avatar-group-overlap)"):a.style.removeProperty("margin-left"),i<r?a.style.removeProperty("display"):a.style.display="none"}this.lastSyncedAvatars=[...t]}connectedCallback(){super.connectedCallback(),this.childListObserver=new MutationObserver(()=>{this.syncAvatarChildren()}),this.childListObserver.observe(this,{childList:!0})}disconnectedCallback(){for(let t of(this.childListObserver?.disconnect(),this.childListObserver=void 0,super.disconnectedCallback(),this.lastSyncedAvatars))t.removeAttribute("data-grouped"),t.style.removeProperty("margin-left"),t.style.removeProperty("display");this.lastSyncedAvatars=[]}getAvatarChildren(){return Array.from(this.querySelectorAll(":scope > smzh-avatar"))}handleSlotChange=()=>{this.syncAvatarChildren()};firstUpdated(){this.syncAvatarChildren()}updated(t){(t.has("size")||t.has("max"))&&this.syncAvatarChildren()}render(){return W`
      <div
        class="group"
        role="group"
        aria-label=${this.getAttribute("aria-label")??"Avatar group"}
      >
        <slot @slotchange=${this.handleSlotChange}></slot>
        ${this._overflowCount>0?W`<span
              class="overflow"
              style="margin-left: var(--smzh-avatar-group-overlap)"
              aria-label="${this._overflowCount} more"
              >+${this._overflowCount}</span
            >`:Z}
      </div>
    `}});let iO=l`
  :host {
    box-sizing: border-box;
    color: var(--smzh-color-text-strong);
    display: block;
    max-width: var(--smzh-advisor-callout-max-width, 476px);
    width: 100%;
  }

  :host([hidden]) {
    display: none !important;
  }

  .root {
    background: var(
      --smzh-advisor-callout-surface,
      var(--smzh-color-advisor-callout-surface)
    );
    border: 1px solid
      var(--smzh-advisor-callout-border-color, var(--smzh-color-border-default));
    border-radius: var(
      --smzh-advisor-callout-radius,
      var(--smzh-spacing-xxx-sm)
    );
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    gap: var(--smzh-spacing-xx-sm);
    padding: var(--smzh-advisor-callout-padding, var(--smzh-spacing-x-sm));
    width: 100%;
  }

  .avatars {
    display: inline-flex;
    width: fit-content;
  }

  .content {
    display: flex;
    flex-direction: column;
    gap: var(--smzh-spacing-xx-sm);
    width: 100%;
  }

  .title smzh-typography {
    color: var(--smzh-color-text-strong);
    display: block;
  }

  .body smzh-typography {
    color: var(--smzh-color-text-strong);
    display: block;
  }

  .action-row {
    display: inline-flex;
    width: fit-content;
  }

  .root[data-alignment="center"] {
    align-items: center;
    text-align: center;
  }

  .root[data-surface="subtle"],
  .root[data-surface="plain"] {
    border-color: var(
      --smzh-advisor-callout-border-color,
      var(--smzh-color-advisor-callout-contextual-border)
    );
  }

  .root[data-shape="rounded"] {
    border-radius: var(--smzh-advisor-callout-radius, var(--smzh-spacing-md));
  }

  .root[data-surface="subtle"] {
    background: var(
      --smzh-advisor-callout-surface,
      var(--smzh-color-advisor-callout-subtle-surface)
    );
  }

  .root[data-surface="plain"] {
    background: var(
      --smzh-advisor-callout-surface,
      var(--smzh-color-advisor-callout-plain-surface)
    );
  }

  .root[data-alignment="center"] .avatars,
  .root[data-alignment="center"] .action-row {
    margin-inline: auto;
  }

  .root[data-alignment="center"] ::slotted(*) {
    text-align: center;
  }

  .root[data-alignment="center"] .title smzh-typography {
    --smzh-typography-line-height: var(--smzh-spacing-x-big);

    color: var(--smzh-color-advisor-callout-centered-text);
  }

  .action-row smzh-link {
    font-weight: var(--smzh-font-weight-medium);
  }

  .root[data-alignment="center"] .action-row smzh-link {
    --smzh-link-font-size: var(--smzh-typography-text-sm-font-size);
    --smzh-link-link-color: var(--smzh-color-primary);
    --smzh-link-line-height: var(--smzh-spacing-big);
  }
`,iB=["_self","_blank"],iq=["start","center"],iU=["default","subtle","plain"],iV=["default","rounded"],iW=["button","link"],iG=new t.U(t.r(935627)).href,iX=new t.U(t.r(574443)).href,iY=new t.U(t.r(38793)).href,iZ="start",iK="default",iJ="default",iQ="button";"u">typeof window&&!customElements.get("smzh-advisor-callout")&&customElements.define("smzh-advisor-callout",class extends tp{static styles=iO;static properties={alignment:{type:String,reflect:!0},surface:{type:String,reflect:!0},shape:{type:String,reflect:!0},hideAvatars:{type:Boolean,attribute:"hide-avatars",reflect:!0},heading:{type:String,reflect:!0},body:{type:String,reflect:!0},ctaLabel:{type:String,attribute:"cta-label",reflect:!0},ctaHref:{type:String,attribute:"cta-href",reflect:!0},ctaTarget:{type:String,attribute:"cta-target",reflect:!0},actionVariant:{type:String,attribute:"action-variant",reflect:!0}};constructor(){super(),this.alignment=iZ,this.surface=iK,this.shape=iJ,this.hideAvatars=!1,this.heading="Bereits eine Offerte erhalten?",this.body="Wir analysieren sie für Sie und prüfen, ob Sie von besseren Zinsen oder Konditionen profitieren können.",this.ctaLabel="Jetzt Beratungsgespräch vereinbaren",this.ctaHref=void 0,this.ctaTarget=void 0,this.actionVariant=iQ}resolveAlignment(){var t;return"string"==typeof(t=this.alignment)&&iq.includes(t)?this.alignment:iZ}resolveSurface(){var t;return"string"==typeof(t=this.surface)&&iU.includes(t)?this.surface:iK}resolveShape(){var t;return"string"==typeof(t=this.shape)&&iV.includes(t)?this.shape:iJ}resolveActionVariant(){var t;return"string"==typeof(t=this.actionVariant)&&iW.includes(t)?this.actionVariant:iQ}resolveCtaTarget(){var t;if("string"==typeof(t=this.ctaTarget)&&iB.includes(t))return this.ctaTarget}hasSlottedContent(t){return Array.from(this.children).some(e=>e.getAttribute("slot")===t)}hasTextContent(t){return"string"==typeof t&&t.trim().length>0}handleActionClick(t){t.preventDefault();let e=this.resolveCtaTarget();if(!this.dispatchEvent(new CustomEvent("smzh-advisor-callout-action",{bubbles:!0,cancelable:!0,composed:!0,detail:{href:this.ctaHref,originalEvent:t,target:e}}))||!this.ctaHref||"u"<typeof window)return;if("_blank"===e)return void window.open(this.ctaHref,"_blank","noreferrer,noopener");let r=document.createElement("a");r.href=this.ctaHref,r.target="_self",r.rel="noopener",r.style.display="none",document.body.appendChild(r),r.click(),r.remove()}renderAction(){return this.ctaLabel?"link"===this.resolveActionVariant()?W`
        <smzh-link
          href=${this.ctaHref??Z}
          target=${this.resolveCtaTarget()??Z}
          variant="link"
          size="md"
          @click=${this.handleActionClick}
        >
          ${this.ctaLabel}
        </smzh-link>
      `:W`
      <smzh-button
        variant="secondary"
        size="sm"
        shape="pill"
        @click=${this.handleActionClick}
      >
        ${this.ctaLabel}
      </smzh-button>
    `:Z}render(){let t=this.hasSlottedContent("title")||this.hasTextContent(this.heading),e=this.hasSlottedContent("body")||this.hasTextContent(this.body),r=this.hasSlottedContent("action")||this.hasTextContent(this.ctaLabel),i=!this.hideAvatars;return W`
      <article
        class="root"
        data-alignment=${this.resolveAlignment()}
        data-surface=${this.resolveSurface()}
        data-shape=${this.resolveShape()}
      >
        ${i?W`
              <div class="avatars">
                <slot name="avatars">
                  <smzh-avatar-group size="xl" aria-label="Advisors">
                    <smzh-avatar
                      src=${iG}
                      alt="Samira"
                    ></smzh-avatar>
                    <smzh-avatar
                      src=${iX}
                      alt="Flavio Retica"
                    ></smzh-avatar>
                    <smzh-avatar
                      src=${iY}
                      alt="Jenni Huber"
                    ></smzh-avatar>
                  </smzh-avatar-group>
                </slot>
              </div>
            `:Z}
        ${t||e||r?W`
              <div class="content">
                ${t?W`
                      <div class="title">
                        <slot name="title">
                          <smzh-typography
                            as="p"
                            variant=${"center"===this.resolveAlignment()?"text-md":"text-lg"}
                            weight=${"center"===this.resolveAlignment()?"regular":"medium"}
                          >
                            ${this.heading}
                          </smzh-typography>
                        </slot>
                      </div>
                    `:Z}
                ${e?W`
                      <div class="body">
                        <slot name="body">
                          <smzh-typography
                            as="p"
                            variant="text-md"
                            weight="regular"
                          >
                            ${this.body}
                          </smzh-typography>
                        </slot>
                      </div>
                    `:Z}
                ${r?W`
                      <div class="action-row">
                        <slot name="action">${this.renderAction()}</slot>
                      </div>
                    `:Z}
              </div>
            `:Z}
      </article>
    `}});let i0=l`
  :host {
    box-sizing: border-box;
    color: var(--smzh-color-text-default);
    display: block;
    max-width: var(--smzh-blog-card-max-width, 412px);
    width: 100%;
  }

  :host([hidden]) {
    display: none !important;
  }

  :host([variant="teaser"]) {
    max-width: var(--smzh-blog-card-teaser-max-width, 400px);
  }

  .root {
    border-radius: var(--smzh-blog-card-radius, var(--smzh-spacing-x-sm));
    box-sizing: border-box;
    overflow: clip;
    width: 100%;
  }

  .root[data-variant="teaser"] {
    border-radius: 0;
    display: flex;
    flex-direction: column;
    gap: var(--smzh-blog-card-teaser-gap, var(--smzh-spacing-big));
    overflow: visible;
  }

  .media {
    align-items: center;
    background: var(
      --smzh-blog-card-media-surface,
      var(--smzh-color-background)
    );
    display: flex;
    height: var(--smzh-blog-card-image-height, 250px);
    justify-content: center;
    overflow: hidden;
    width: 100%;
  }

  .root[data-variant="teaser"] .media {
    border-radius: var(
      --smzh-blog-card-teaser-media-radius,
      var(--smzh-spacing-x-sm)
    );
    height: var(--smzh-blog-card-teaser-image-height, 267px);
  }

  .media img,
  .media ::slotted(img) {
    display: block;
    height: 100%;
    object-fit: cover;
    width: 100%;
  }

  .content {
    background: var(--smzh-color-surface);
    border: 1px solid var(--smzh-color-border-default);
    border-radius: 0 0 var(--smzh-blog-card-radius, var(--smzh-spacing-x-sm))
      var(--smzh-blog-card-radius, var(--smzh-spacing-x-sm));
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    gap: var(--smzh-spacing-md);
    padding: var(--smzh-spacing-x-big);
    width: 100%;
  }

  .content[data-variant="teaser"] {
    background: transparent;
    border-width: 0;
    border-radius: 0;
    gap: var(--smzh-blog-card-teaser-gap, var(--smzh-spacing-big));
    padding: 0;
  }

  .copy {
    display: flex;
    flex-direction: column;
    gap: var(--smzh-spacing-xxx-sm);
    min-width: 0;
    width: 100%;
  }

  .copy[data-variant="teaser"] {
    gap: var(--smzh-blog-card-teaser-copy-gap, var(--smzh-spacing-x-sm));
  }

  .eyebrow,
  .title,
  .body,
  .action-row {
    min-width: 0;
    width: 100%;
  }

  .root[data-variant="teaser"] .action-row {
    width: auto;
  }

  .eyebrow smzh-typography {
    color: var(--smzh-blog-card-eyebrow-color, var(--smzh-color-text-subtle));
    display: block;
  }

  .title smzh-typography {
    color: var(--smzh-blog-card-title-color, var(--smzh-color-primary-active));
    display: -webkit-box;
    overflow: hidden;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: var(--smzh-blog-card-title-lines, 2);
  }

  .body smzh-typography {
    color: var(--smzh-blog-card-body-color, var(--smzh-color-text-default));
    display: -webkit-box;
    overflow: hidden;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: var(--smzh-blog-card-body-lines, 2);
  }

  .root[data-variant="teaser"] .title smzh-typography {
    color: var(
      --smzh-blog-card-teaser-title-color,
      var(--smzh-color-text-strong)
    );
    -webkit-line-clamp: var(--smzh-blog-card-teaser-title-lines, 3);
  }

  .action-button {
    align-items: center;
    background: var(--smzh-color-surface);
    border: 1px solid
      var(--smzh-blog-card-action-border-color, var(--smzh-color-border-focus));
    border-radius: var(
      --smzh-blog-card-action-radius,
      var(--smzh-spacing-xxx-sm)
    );
    box-sizing: border-box;
    color: var(--smzh-blog-card-action-color, var(--smzh-color-primary-active));
    cursor: pointer;
    display: inline-flex;
    justify-content: center;
    min-height: 50px;
    padding: 11px 18px;
    text-align: center;
    text-decoration: none;
    transition:
      border-color 140ms ease,
      box-shadow 140ms ease,
      color 140ms ease;
    width: 100%;
  }

  .action-button {
    font: inherit;
  }

  .action-button:hover {
    border-color: var(
      --smzh-blog-card-action-border-hover-color,
      var(--smzh-color-primary)
    );
    box-shadow: var(--smzh-color-shadow-xs);
    color: var(--smzh-blog-card-action-hover-color, var(--smzh-color-primary));
  }

  .action-button:active {
    border-color: var(
      --smzh-blog-card-action-border-active-color,
      var(--smzh-color-primary-active)
    );
    box-shadow: none;
    color: var(
      --smzh-blog-card-action-active-color,
      var(--smzh-color-primary-active)
    );
  }

  .action-link {
    display: block;
    width: 100%;
  }

  .action-button:focus-visible,
  .action-link:focus-visible {
    outline: 2px solid var(--smzh-color-border-focus);
    outline-offset: 2px;
  }

  .action-button smzh-typography {
    color: inherit;
    display: block;
  }

  .action-inline {
    align-items: center;
    background: transparent;
    border-width: 0;
    color: var(--smzh-blog-card-teaser-action-color, var(--smzh-color-primary));
    cursor: pointer;
    display: inline-flex;
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-md-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-regular);
    gap: var(--smzh-spacing-xx-sm);
    letter-spacing: -0.01em;
    line-height: 24px;
    padding: 0;
    text-align: left;
    text-decoration: none;
    transition:
      color 140ms ease,
      opacity 140ms ease;
  }

  .action-inline:hover {
    color: var(
      --smzh-blog-card-teaser-action-hover-color,
      var(--smzh-color-primary-hover)
    );
  }

  .action-inline:active {
    color: var(
      --smzh-blog-card-teaser-action-active-color,
      var(--smzh-color-primary-active)
    );
  }

  .action-inline:focus-visible {
    outline: 2px solid var(--smzh-color-border-focus);
    outline-offset: 2px;
  }

  .teaser-action-label {
    display: inline-block;
  }

  .teaser-action-icon {
    align-items: center;
    display: inline-flex;
    flex: 0 0 auto;
    height: 18px;
    justify-content: center;
    width: 18px;
  }

  .teaser-action-icon svg {
    display: block;
    height: 18px;
    width: 18px;
  }
`,i1=["_self","_blank"],i2=["default","teaser"],i4=new t.U(t.r(656799)).href,i3="default";"u">typeof window&&!customElements.get("smzh-blog-card")&&customElements.define("smzh-blog-card",class extends tp{static styles=i0;static properties={variant:{type:String,reflect:!0},imageSrc:{type:String,attribute:"image-src",reflect:!0},imageAlt:{type:String,attribute:"image-alt",reflect:!0},eyebrow:{type:String,reflect:!0},title:{type:String,reflect:!0},body:{type:String,reflect:!0},ctaLabel:{type:String,attribute:"cta-label",reflect:!0},ctaHref:{type:String,attribute:"cta-href",reflect:!0},ctaTarget:{type:String,attribute:"cta-target",reflect:!0}};constructor(){super(),this.variant=i3,this.imageSrc=i4,this.imageAlt="Hypotheken factsheet preview",this.eyebrow="",this.title="Die langjährigen Zinsen fallen weiter",this.body="In ihrer geldpolitischen Lagebeurteilung vom September beliess die Schweizerische...",this.ctaLabel="Read factsheet",this.ctaHref=void 0,this.ctaTarget=void 0}hasSlottedContent(t){return Array.from(this.children).some(e=>e.getAttribute("slot")===t)}hasTextContent(t){return"string"==typeof t&&t.trim().length>0}resolveCtaTarget(){var t;if("string"==typeof(t=this.ctaTarget)&&i1.includes(t))return this.ctaTarget}resolveCtaRel(t){if("_blank"===t)return"noreferrer noopener"}resolveVariant(){var t;return"string"==typeof(t=this.variant)&&i2.includes(t)?this.variant:i3}handleActionClick(t){this.dispatchEvent(new CustomEvent("smzh-blog-card-action",{bubbles:!0,composed:!0,detail:{originalEvent:t}}))}renderTeaserActionLabel(){return W`
      <span class="teaser-action-label">${this.ctaLabel}</span>
      <span class="teaser-action-icon" aria-hidden="true">
        ${tS["chevron-right"](void 0)}
      </span>
    `}renderAction(t){if(!this.hasTextContent(this.ctaLabel))return Z;if("teaser"===t){if(this.ctaHref){let t=this.resolveCtaTarget(),e=this.resolveCtaRel(t);return W`
          <a
            class="action-inline"
            href=${this.ctaHref}
            target=${t??Z}
            rel=${e??Z}
          >
            ${this.renderTeaserActionLabel()}
          </a>
        `}return W`
        <button
          class="action-inline"
          type="button"
          @click=${this.handleActionClick}
        >
          ${this.renderTeaserActionLabel()}
        </button>
      `}let e=W`
      <smzh-typography as="span" variant="label-lg" weight="normal">
        ${this.ctaLabel}
      </smzh-typography>
    `;if(this.ctaHref){let t=this.resolveCtaTarget();return W`
        <smzh-link
          class="action-link"
          href=${this.ctaHref}
          target=${t??Z}
          variant="secondary"
          size="lg"
          shape="rounded"
          full-width
        >
          ${e}
        </smzh-link>
      `}return W`
      <button
        class="action-button"
        type="button"
        @click=${this.handleActionClick}
      >
        ${e}
      </button>
    `}render(){let t=this.resolveVariant(),e=this.hasSlottedContent("image")||this.hasTextContent(this.imageSrc),r=this.hasSlottedContent("eyebrow")||this.hasTextContent(this.eyebrow),i=this.hasSlottedContent("title")||this.hasTextContent(this.title),a=this.hasSlottedContent("body")||this.hasTextContent(this.body),s=this.hasSlottedContent("action")||this.hasTextContent(this.ctaLabel);return W`
      <article class="root" data-variant=${t}>
        ${e?W`
              <div class="media">
                <slot name="image">
                  ${this.imageSrc?W`
                        <img
                          src=${this.imageSrc}
                          alt=${this.imageAlt}
                          loading="lazy"
                        />
                      `:Z}
                </slot>
              </div>
            `:Z}

        <div class="content" data-variant=${t}>
          ${r||i||a?W`
                <div class="copy" data-variant=${t}>
                  ${r?W`
                        <div class="eyebrow">
                          <slot name="eyebrow">
                            <smzh-typography
                              as="p"
                              variant="label-sm"
                              weight="normal"
                            >
                              ${this.eyebrow}
                            </smzh-typography>
                          </slot>
                        </div>
                      `:Z}
                  ${i?W`
                        <div class="title">
                          <slot name="title">
                            <smzh-typography
                              as="p"
                              variant=${"teaser"===t?"text-xl":"text-lg"}
                              weight="medium"
                            >
                              ${this.title}
                            </smzh-typography>
                          </slot>
                        </div>
                      `:Z}
                  ${a?W`
                        <div class="body">
                          <slot name="body">
                            <smzh-typography
                              as="p"
                              variant="text-md"
                              weight="regular"
                            >
                              ${this.body}
                            </smzh-typography>
                          </slot>
                        </div>
                      `:Z}
                </div>
              `:Z}
          ${s?W`<div class="action-row">
                <slot name="action">${this.renderAction(t)}</slot>
              </div>`:Z}
        </div>
      </article>
    `}});let i5=l`
  :host {
    box-sizing: border-box;
    color: var(--smzh-color-text-emphasis);
    display: block;
    max-width: var(--smzh-success-state-max-width, 540px);
    width: 100%;
  }

  :host([hidden]) {
    display: none !important;
  }

  .root {
    align-items: center;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    gap: var(--smzh-success-state-gap, 30px);
    justify-content: center;
    width: 100%;
  }

  .root[data-alignment="start"] {
    align-items: flex-start;
    text-align: left;
  }

  .icon,
  .icon ::slotted(img) {
    display: block;
    flex: 0 0 auto;
    height: var(--smzh-success-state-icon-size, 46px);
    width: var(--smzh-success-state-icon-size, 46px);
  }

  .copy {
    align-items: center;
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  .root[data-alignment="start"] .copy {
    align-items: flex-start;
  }

  .root[data-alignment="start"] ::slotted(*) {
    text-align: left;
  }

  .title,
  .subtitle {
    width: 100%;
  }
`,i8=["center","start"],i6=new t.U(t.r(241913)).href,i9="center";"u">typeof window&&!customElements.get("smzh-success-state")&&customElements.define("smzh-success-state",class extends tp{static styles=i5;static properties={alignment:{type:String,reflect:!0},iconSrc:{type:String,attribute:"icon-src",reflect:!0},iconAlt:{type:String,attribute:"icon-alt",reflect:!0},title:{type:String,reflect:!0},subtitle:{type:String,reflect:!0}};constructor(){super(),this.alignment=i9,this.iconSrc=i6,this.iconAlt="",this.title="Vielen Dank!",this.subtitle="Wir werden uns bei Ihnen melden."}hasSlottedContent(t){return Array.from(this.children).some(e=>e.getAttribute("slot")===t)}hasTextContent(t){return"string"==typeof t&&t.trim().length>0}resolveAlignment(){var t;return"string"==typeof(t=this.alignment)&&i8.includes(t)?this.alignment:i9}resolveTextAlign(){return"start"===this.resolveAlignment()?"left":"center"}render(){let t=this.hasSlottedContent("icon")||this.hasTextContent(this.iconSrc),e=this.hasSlottedContent("title")||this.hasTextContent(this.title),r=this.hasSlottedContent("subtitle")||this.hasTextContent(this.subtitle);if(!t&&!e&&!r)return Z;let i=this.resolveAlignment(),a=this.resolveTextAlign();return W`
      <section
        class="root"
        role="status"
        aria-live="polite"
        data-alignment=${i}
      >
        ${t?W`
              <div class="icon">
                <slot name="icon">
                  ${this.iconSrc?W`
                        <img
                          src=${this.iconSrc}
                          alt=${this.iconAlt}
                          loading="lazy"
                        />
                      `:Z}
                </slot>
              </div>
            `:Z}
        ${e||r?W`
              <div class="copy">
                ${e?W`
                      <div class="title">
                        <slot name="title">
                          <smzh-typography
                            as="h3"
                            weight="medium"
                            align=${a}
                            style="color: var(--smzh-success-state-title-color, var(--smzh-color-text-emphasis));"
                          >
                            ${this.title}
                          </smzh-typography>
                        </slot>
                      </div>
                    `:Z}
                ${r?W`
                      <div class="subtitle">
                        <slot name="subtitle">
                          <smzh-typography
                            as="h3"
                            weight="normal"
                            align=${a}
                            style="color: var(--smzh-success-state-subtitle-color, var(--smzh-color-text-subtle));"
                          >
                            ${this.subtitle}
                          </smzh-typography>
                        </slot>
                      </div>
                    `:Z}
              </div>
            `:Z}
      </section>
    `}});let i7=l`
  :host {
    box-sizing: border-box;
    color: var(--smzh-color-text-default);
    display: block;
    max-width: var(--smzh-tip-card-max-width, none);
    width: 100%;
  }

  :host([hidden]) {
    display: none !important;
  }

  .root {
    background: var(--smzh-color-surface);
    border: 1px solid var(--smzh-color-border-default);
    border-radius: var(--smzh-tip-card-radius, var(--smzh-spacing-md));
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    padding: var(--smzh-tip-card-padding, var(--smzh-spacing-x-sm));
    width: 100%;
  }

  .content {
    border-radius: var(--smzh-tip-card-content-radius, var(--smzh-spacing-sm));
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    gap: var(--smzh-tip-card-gap, var(--smzh-spacing-xx-sm));
    min-width: 0;
    padding: var(--smzh-tip-card-content-padding, var(--smzh-spacing-xxx-sm));
    width: 100%;
  }

  .title,
  .description {
    min-width: 0;
  }

  .title ::slotted(*),
  .description ::slotted(*) {
    display: block;
    margin: 0;
  }

  .fallback-title,
  .fallback-description {
    color: var(--smzh-color-text-default);
    display: block;
  }
`;"u">typeof window&&!customElements.get("smzh-tip-card")&&customElements.define("smzh-tip-card",class extends tp{static styles=i7;static properties={heading:{type:String,reflect:!0},description:{type:String,reflect:!0}};constructor(){super(),this.heading="",this.description=""}hasSlottedContent(t){return Array.from(this.children).some(e=>e.getAttribute("slot")===t)}hasTextContent(t){return"string"==typeof t&&t.trim().length>0}render(){let t=this.hasSlottedContent("title")||this.hasTextContent(this.heading),e=this.hasSlottedContent("description")||this.hasTextContent(this.description);return W`
      <article class="root">
        <div class="content">
          ${t?W`
                <div class="title">
                  <slot name="title">
                    <smzh-typography
                      class="fallback-title"
                      as="p"
                      variant="text-md"
                      weight="medium"
                    >
                      ${this.heading}
                    </smzh-typography>
                  </slot>
                </div>
              `:Z}
          ${e?W`
                <div class="description">
                  <slot name="description">
                    <smzh-typography
                      class="fallback-description"
                      as="p"
                      variant="text-md"
                      weight="regular"
                    >
                      ${this.description}
                    </smzh-typography>
                  </slot>
                </div>
              `:Z}
        </div>
      </article>
    `}});let at=l`
  :host {
    display: block;
    width: 100%;
  }

  :host([hidden]) {
    display: none !important;
  }

  .tile {
    align-items: center;
    background: var(--smzh-color-surface);
    border: 1px solid var(--smzh-color-tile-border);
    border-radius: var(--smzh-spacing-xxx-sm);
    box-sizing: border-box;
    color: var(--smzh-color-tile-title);
    cursor: pointer;
    display: flex;
    font-family: var(--smzh-font-family-sans);
    gap: var(--smzh-spacing-x-sm);
    margin: 0;
    min-width: 0;
    padding: var(--smzh-spacing-md);
    text-align: left;
    transition:
      border-color 140ms ease,
      background-color 140ms ease;
    width: 100%;
  }

  .tile:disabled {
    cursor: not-allowed;
    opacity: 0.6;
  }

  .tile:hover:not(:disabled) {
    border-color: var(--smzh-color-border-strong);
  }

  .tile:focus {
    outline: none;
  }

  .tile:focus-visible {
    outline: 2px solid var(--smzh-color-border-focus);
    outline-offset: 2px;
  }

  :host([selected]) .tile {
    border-color: var(--smzh-color-tile-border-selected);
  }

  .icon-slot {
    display: none;
    flex: 0 0 auto;
    height: var(--smzh-spacing-x-big);
    width: var(--smzh-spacing-x-big);
  }

  :host([has-icon]) .icon-slot {
    align-items: center;
    display: inline-flex;
    justify-content: center;
  }

  .icon-slot ::slotted(*) {
    display: block;
    line-height: 0;
  }

  .text-wrap {
    display: flex;
    flex: 1 1 auto;
    flex-direction: column;
    gap: var(--smzh-spacing-xxx-sm);
    min-width: 0;
  }

  .title {
    font-size: var(--smzh-typography-text-sm-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-medium);
    letter-spacing: var(--smzh-typography-text-sm-letter-spacing);
    line-height: var(--smzh-typography-text-sm-line-height);
  }

  .description {
    color: var(--smzh-color-text-subtle);
    display: none;
    font-size: var(--smzh-typography-text-sm-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    letter-spacing: var(--smzh-typography-text-sm-letter-spacing);
    line-height: var(--smzh-typography-text-sm-line-height);
  }

  :host([has-description]) .description {
    display: block;
  }
`;"u">typeof window&&!customElements.get("smzh-tile")&&customElements.define("smzh-tile",class extends tp{static styles=at;static properties={selected:{type:Boolean,reflect:!0},disabled:{type:Boolean,reflect:!0},value:{type:String,reflect:!0},hasIcon:{type:Boolean,reflect:!0,attribute:"has-icon"},hasDescription:{type:Boolean,reflect:!0,attribute:"has-description"}};selectionModeContextInternal;constructor(){super(),this.selected=!1,this.disabled=!1,this.value="",this.hasIcon=!1,this.hasDescription=!1,this.selectionModeContextInternal=void 0}setSelectionModeContext(t){this.selectionModeContextInternal!==t&&(this.selectionModeContextInternal=t,this.requestUpdate())}firstUpdated(){this.syncSlotFlags()}slotHasContent(t){return!!t&&t.assignedNodes({flatten:!0}).some(t=>t.nodeType===Node.TEXT_NODE?!!t.textContent?.trim():t.nodeType===Node.ELEMENT_NODE)}syncSlotFlags(){let t=this.renderRoot.querySelector('slot[name="icon"]'),e=this.renderRoot.querySelector('slot[name="description"]');this.hasIcon=this.slotHasContent(t),this.hasDescription=this.slotHasContent(e)}handleSlotChange=()=>{this.syncSlotFlags()};handlePress=()=>{if(this.disabled)return;let t=new CustomEvent("smzh-tile-press",{bubbles:!0,composed:!0,cancelable:!0,detail:{value:this.value}});this.dispatchEvent(t),t.defaultPrevented||(this.selected=!this.selected)};get roleForControl(){return"single"===this.selectionModeContextInternal?"radio":"multiple"===this.selectionModeContextInternal?"checkbox":"button"}render(){let t=this.roleForControl,e="button"===t?this.selected?"true":"false":void 0,r="button"!==t?this.selected?"true":"false":void 0;return W`
      <button
        class="tile"
        part="control"
        type="button"
        role=${t}
        ?disabled=${this.disabled}
        aria-pressed=${e??Z}
        aria-checked=${r??Z}
        @click=${this.handlePress}
      >
        <span class="icon-slot" aria-hidden="true">
          <slot name="icon" @slotchange=${this.handleSlotChange}></slot>
        </span>
        <span class="text-wrap">
          <span class="title">
            <slot @slotchange=${this.handleSlotChange}></slot>
          </span>
          <span class="description">
            <slot
              name="description"
              @slotchange=${this.handleSlotChange}
            ></slot>
          </span>
        </span>
      </button>
    `}});let ae=l`
  :host {
    display: block;
    width: 100%;
  }

  :host([hidden]) {
    display: none !important;
  }

  .root {
    display: flex;
    flex-direction: column;
    gap: var(--smzh-spacing-md);
    width: 100%;
  }

  .header {
    display: flex;
    flex-direction: column;
    gap: var(--smzh-spacing-xxx-sm);
    width: 100%;
  }

  .label ::slotted(*) {
    color: var(--smzh-color-tile-title);
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-lg-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-medium);
    letter-spacing: var(--smzh-typography-text-lg-letter-spacing);
    line-height: var(--smzh-typography-text-lg-line-height);
    margin: 0;
  }

  .helper {
    color: var(--smzh-color-text-subtle);
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-sm-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    letter-spacing: var(--smzh-typography-text-sm-letter-spacing);
    line-height: var(--smzh-typography-text-sm-line-height);
  }

  .tiles {
    display: flex;
    flex-direction: column;
    gap: var(--smzh-spacing-md);
    width: 100%;
  }
`,ar=["single","multiple"],ai="single";class aa extends tp{static styles=ae;labelId=`smzh-tile-group-label-${Math.random().toString(36).slice(2,10)}`;static properties={selectionMode:{type:String,attribute:"selection-mode",reflect:!0},value:{type:String,reflect:!0},values:{type:String,reflect:!0},multiSelectHint:{type:Boolean,attribute:"multi-select-hint",reflect:!0}};constructor(){super(),this.selectionMode=ai,this.value="",this.values="",this.multiSelectHint=!0}connectedCallback(){super.connectedCallback(),this.addEventListener("smzh-tile-press",this.handleTileSelect)}disconnectedCallback(){this.removeEventListener("smzh-tile-press",this.handleTileSelect),super.disconnectedCallback()}updated(){this.syncTileSelection()}resolveSelectionMode(){var t;return"string"==typeof(t=this.selectionMode)&&ar.includes(t)?this.selectionMode:ai}parseValues(t){if("string"!=typeof t||0===t.trim().length)return[];let e=t.trim();if(e.startsWith("[")&&e.endsWith("]"))try{let t=JSON.parse(e);if(Array.isArray(t))return t.filter(t=>"string"==typeof t).map(t=>t.trim()).filter(t=>t.length>0)}catch{}return e.split(",").map(t=>t.trim()).filter(t=>t.length>0)}getTileChildren(){return Array.from(this.querySelectorAll("smzh-tile"))}syncTileSelection(){let t=this.getTileChildren(),e=this.resolveSelectionMode();for(let r of t)r.setSelectionModeContext(e);if("single"===e){let e=this.value??"";for(let r of t)r.selected=!!r.value&&r.value===e;return}let r=new Set(this.parseValues(this.values));for(let e of t){let t=e.value??"";e.selected=t.length>0&&r.has(t)}}emitChange(){let t=this.resolveSelectionMode(),e="single"===t?this.value:void 0,r="single"===t?this.value?[this.value]:[]:this.parseValues(this.values);this.dispatchEvent(new CustomEvent("smzh-tile-group-change",{bubbles:!0,composed:!0,detail:{value:e,values:r}}))}handleTileSelect=t=>{let e=t.target;if(!e||!this.contains(e))return;t.stopPropagation(),t.preventDefault();let r=t.detail?.value?.trim()??"";if(0===r.length)return;if("single"===this.resolveSelectionMode()){this.value=r,this.emitChange();return}let i=new Set(this.parseValues(this.values));i.has(r)?i.delete(r):i.add(r),this.values=JSON.stringify(Array.from(i)),this.emitChange()};get selectedCount(){return"single"===this.resolveSelectionMode()?+!!this.value?.trim():this.parseValues(this.values).length}renderHelper(){if("multiple"!==this.resolveSelectionMode()||!1===this.multiSelectHint)return Z;let t=this.selectedCount>0?`${this.selectedCount} selected`:"Select all that apply";return W`
      <div class="helper" part="helper">
        <slot name="helper">${t}</slot>
      </div>
    `}handleDefaultSlotChange=()=>{this.syncTileSelection()};render(){let t=this.resolveSelectionMode();return W`
      <div
        class="root"
        part="root"
        role=${"single"===t?"radiogroup":"group"}
        aria-labelledby=${this.labelId}
      >
        <div class="header">
          <div class="label" part="label" id=${this.labelId}>
            <slot name="label"></slot>
          </div>
          ${this.renderHelper()}
        </div>
        <div class="tiles" part="tiles">
          <slot @slotchange=${this.handleDefaultSlotChange}></slot>
        </div>
      </div>
    `}}"u">typeof window&&!customElements.get("smzh-tile-group")&&customElements.define("smzh-tile-group",aa);let as=l`
  :host {
    --smzh-slider-width: 320px;
    --smzh-slider-track-height: var(--smzh-spacing-xxx-sm);
    --smzh-slider-thumb-size: var(--smzh-spacing-md);
    --smzh-slider-tooltip-radius: var(--smzh-spacing-xxx-sm);
    --smzh-slider-tooltip-padding-y: var(--smzh-spacing-xxx-sm);
    --smzh-slider-tooltip-padding-x: var(--smzh-spacing-x-sm);
    --smzh-slider-arrow-span: var(--smzh-spacing-xxx-sm);
    --smzh-slider-arrow-depth: 6px;
    --smzh-slider-wrap-gap: var(--smzh-spacing-xx-sm);
    --smzh-slider-tooltip-offset-top: var(--smzh-spacing-lg);
    --smzh-slider-progress: 0%;
    display: inline-block;
    width: min(100%, var(--smzh-slider-width));
  }

  .wrap {
    display: flex;
    flex-direction: column;
    gap: var(--smzh-slider-wrap-gap);
  }

  .slider {
    padding-top: var(--smzh-slider-tooltip-offset-top);
    position: relative;
  }

  .track {
    background: var(--smzh-color-background-subtle);
    border-radius: 999px;
    height: var(--smzh-slider-track-height);
    overflow: hidden;
    position: relative;
    width: 100%;
  }

  .progress {
    background: linear-gradient(
      90deg,
      var(--smzh-color-primary) 0%,
      var(--smzh-color-primary-subtle-active) 100%
    );
    border-radius: inherit;
    height: 100%;
    width: var(--smzh-slider-progress);
  }

  .input {
    appearance: none;
    background: transparent;
    cursor: pointer;
    height: var(--smzh-slider-thumb-size);
    left: 0;
    margin: 0;
    position: absolute;
    right: 0;
    top: calc(
      var(--smzh-slider-tooltip-offset-top) -
        (var(--smzh-slider-thumb-size) / 2) + 4px
    );
    width: 100%;
  }

  .input:focus-visible {
    outline: none;
  }

  .input::-webkit-slider-thumb {
    appearance: none;
    background: var(--smzh-color-surface);
    border: 1px solid var(--smzh-color-border-default);
    border-radius: 50%;
    box-shadow: var(--smzh-color-shadow-xs);
    height: var(--smzh-slider-thumb-size);
    width: var(--smzh-slider-thumb-size);
  }

  .input::-moz-range-thumb {
    background: var(--smzh-color-surface);
    border: 1px solid var(--smzh-color-border-default);
    border-radius: 50%;
    box-shadow: var(--smzh-color-shadow-xs);
    height: var(--smzh-slider-thumb-size);
    width: var(--smzh-slider-thumb-size);
  }

  .input:focus-visible::-webkit-slider-thumb {
    box-shadow:
      0 0 0 2px var(--smzh-color-surface),
      0 0 0 4px var(--smzh-color-border-focus);
  }

  .input:focus-visible::-moz-range-thumb {
    box-shadow:
      0 0 0 2px var(--smzh-color-surface),
      0 0 0 4px var(--smzh-color-border-focus);
  }

  .tooltip {
    background: var(--smzh-color-surface);
    border-radius: var(--smzh-slider-tooltip-radius);
    box-shadow: var(--smzh-color-tooltip-shadow);
    color: var(--smzh-color-text-subtle);
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-label-sm-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    left: var(--smzh-slider-progress);
    letter-spacing: var(--smzh-typography-label-sm-letter-spacing);
    line-height: 14px;
    padding: var(--smzh-slider-tooltip-padding-y)
      var(--smzh-slider-tooltip-padding-x);
    position: absolute;
    top: 0;
    transform: translateX(-50%);
    white-space: nowrap;
  }

  .tooltip::after {
    border-left: var(--smzh-slider-arrow-span) solid transparent;
    border-right: var(--smzh-slider-arrow-span) solid transparent;
    border-top: var(--smzh-slider-arrow-depth) solid var(--smzh-color-surface);
    content: "";
    left: 50%;
    position: absolute;
    top: 100%;
    transform: translateX(-50%);
  }

  .labels {
    color: var(--smzh-color-text-subtle);
    display: flex;
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-md-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    justify-content: space-between;
    letter-spacing: var(--smzh-typography-text-md-letter-spacing);
    line-height: var(--smzh-typography-text-md-line-height);
    width: 100%;
  }

  :host([disabled]) .input {
    cursor: not-allowed;
    opacity: 0.8;
  }

  :host([disabled]) .progress {
    background: var(--smzh-color-border-default);
  }
`;function an(t){return t}function ao(t){return"translate("+t+",0)"}function al(t){return"translate(0,"+t+")"}function ah(){return!this.__axis}function ac(t,e){var r=[],i=null,a=null,s=6,n=6,o=3,l="u">typeof window&&window.devicePixelRatio>1?0:.5,h=1===t||4===t?-1:1,c=4===t||2===t?"x":"y",d=1===t||3===t?ao:al;function p(p){var u=null==i?e.ticks?e.ticks.apply(e,r):e.domain():i,m=null==a?e.tickFormat?e.tickFormat.apply(e,r):an:a,g=Math.max(s,0)+o,f=e.range(),v=+f[0]+l,y=+f[f.length-1]+l,b=(e.bandwidth?function(t,e){return e=Math.max(0,t.bandwidth()-2*e)/2,t.round()&&(e=Math.round(e)),r=>+t(r)+e}:function(t){return e=>+t(e)})(e.copy(),l),z=p.selection?p.selection():p,x=z.selectAll(".domain").data([null]),w=z.selectAll(".tick").data(u,e).order(),$=w.exit(),k=w.enter().append("g").attr("class","tick"),S=w.select("line"),_=w.select("text");x=x.merge(x.enter().insert("path",".tick").attr("class","domain").attr("stroke","currentColor")),w=w.merge(k),S=S.merge(k.append("line").attr("stroke","currentColor").attr(c+"2",h*s)),_=_.merge(k.append("text").attr("fill","currentColor").attr(c,h*g).attr("dy",1===t?"0em":3===t?"0.71em":"0.32em")),p!==z&&(x=x.transition(p),w=w.transition(p),S=S.transition(p),_=_.transition(p),$=$.transition(p).attr("opacity",1e-6).attr("transform",function(t){return isFinite(t=b(t))?d(t+l):this.getAttribute("transform")}),k.attr("opacity",1e-6).attr("transform",function(t){var e=this.parentNode.__axis;return d((e&&isFinite(e=e(t))?e:b(t))+l)})),$.remove(),x.attr("d",4===t||2===t?n?"M"+h*n+","+v+"H"+l+"V"+y+"H"+h*n:"M"+l+","+v+"V"+y:n?"M"+v+","+h*n+"V"+l+"H"+y+"V"+h*n:"M"+v+","+l+"H"+y),w.attr("opacity",1).attr("transform",function(t){return d(b(t)+l)}),S.attr(c+"2",h*s),_.attr(c,h*g).text(m),z.filter(ah).attr("fill","none").attr("font-size",10).attr("font-family","sans-serif").attr("text-anchor",2===t?"start":4===t?"end":"middle"),z.each(function(){this.__axis=b})}return p.scale=function(t){return arguments.length?(e=t,p):e},p.ticks=function(){return r=Array.from(arguments),p},p.tickArguments=function(t){return arguments.length?(r=null==t?[]:Array.from(t),p):r.slice()},p.tickValues=function(t){return arguments.length?(i=null==t?null:Array.from(t),p):i&&i.slice()},p.tickFormat=function(t){return arguments.length?(a=t,p):a},p.tickSize=function(t){return arguments.length?(s=n=+t,p):s},p.tickSizeInner=function(t){return arguments.length?(s=+t,p):s},p.tickSizeOuter=function(t){return arguments.length?(n=+t,p):n},p.tickPadding=function(t){return arguments.length?(o=+t,p):o},p.offset=function(t){return arguments.length?(l=+t,p):l},p}"u">typeof window&&!customElements.get("smzh-slider")&&customElements.define("smzh-slider",class extends tp{static styles=as;static properties={ariaLabel:{type:String,attribute:"aria-label"},value:{type:Number,reflect:!0},min:{type:Number,reflect:!0},max:{type:Number,reflect:!0},step:{type:Number,reflect:!0},unit:{type:String,reflect:!0},leftLabel:{type:String,attribute:"left-label"},rightLabel:{type:String,attribute:"right-label"},showTooltip:{type:Boolean,attribute:"show-tooltip",reflect:!0},disabled:{type:Boolean,reflect:!0}};constructor(){super(),this.ariaLabel=null,this.value=25,this.min=0,this.max=100,this.step=1,this.unit="%",this.leftLabel=void 0,this.rightLabel=void 0,this.showTooltip=!0,this.disabled=!1}willUpdate(t){super.willUpdate(t),(t.has("step")||t.has("value")||t.has("min")||t.has("max"))&&(this.value=this.normalizeValueToStep(this.value,this.normalizedMin,this.normalizedMax,this.normalizedStep)),t.has("step")&&this.step<=0&&(console.warn("[smzh-slider] 'step' must be > 0. Falling back to 1."),this.step=1)}get normalizedMin(){return Number.isFinite(this.min)?this.min:0}get normalizedMax(){let t=Number.isFinite(this.max)?this.max:100;return t<this.normalizedMin?this.normalizedMin:t}get normalizedStep(){return!Number.isFinite(this.step)||this.step<=0?1:this.step}clamp(t,e,r){return Math.min(r,Math.max(e,t))}normalizeValueToStep(t,e,r,i){let a=Math.round((this.clamp(t,e,r)-e)/i),s=e+a*i,n=this.getDecimalPrecision(i);return this.clamp(Number(s.toFixed(n)),e,r)}getDecimalPrecision(t){let e=String(t);return e.includes(".")?e.split(".")[1]?.length??0:0}resolveAriaLabel(){return"string"==typeof this.ariaLabel&&this.ariaLabel.trim().length>0?this.ariaLabel.trim():"Slider"}get progressRatio(){let t=this.normalizedMin,e=this.normalizedMax,r=e-t;return r<=0?0:(this.clamp(this.value,t,e)-t)/r}get progressPercent(){return`${100*this.progressRatio}%`}formatValue(t){let e=Number.isFinite(t)?t:0;return`${e}${this.unit}`}get effectiveLeftLabel(){return this.leftLabel?.trim()||this.formatValue(this.normalizedMin)}get effectiveRightLabel(){return this.rightLabel?.trim()||this.formatValue(this.normalizedMax)}handleInput(t){let e=t.currentTarget;if(!(e instanceof HTMLInputElement))return;let r=Number(e.value);Number.isFinite(r)&&(this.value=this.normalizeValueToStep(r,this.normalizedMin,this.normalizedMax,this.normalizedStep),this.dispatchEvent(new CustomEvent("smzh-input",{detail:{value:this.value},bubbles:!0,composed:!0})))}handleChange(t){let e=t.currentTarget;if(!(e instanceof HTMLInputElement))return;let r=Number(e.value);Number.isFinite(r)&&(this.value=this.normalizeValueToStep(r,this.normalizedMin,this.normalizedMax,this.normalizedStep),this.dispatchEvent(new CustomEvent("smzh-change",{detail:{value:this.value},bubbles:!0,composed:!0})))}render(){let t=this.formatValue(this.value),e=this.resolveAriaLabel();return W`
      <div
        class="wrap"
        style=${`--smzh-slider-progress:${this.progressPercent};`}
      >
        <div class="slider">
          ${this.showTooltip?W`<div class="tooltip">${this.formatValue(this.value)}</div>`:null}
          <div class="track" aria-hidden="true">
            <div class="progress"></div>
          </div>
          <input
            class="input"
            type="range"
            min=${String(this.normalizedMin)}
            max=${String(this.normalizedMax)}
            step=${String(this.normalizedStep)}
            .value=${String(this.value)}
            aria-label=${e}
            aria-valuetext=${t??Z}
            ?disabled=${this.disabled}
            @input=${this.handleInput}
            @change=${this.handleChange}
          />
        </div>
        <div class="labels">
          <span>${this.effectiveLeftLabel}</span>
          <span>${this.effectiveRightLabel}</span>
        </div>
      </div>
    `}});let ad=Math.sqrt(50),ap=Math.sqrt(10),au=Math.sqrt(2);function am(t,e,r){let i,a,s,n=(e-t)/Math.max(0,r),o=Math.floor(Math.log10(n)),l=n/Math.pow(10,o),h=l>=ad?10:l>=ap?5:l>=au?2:1;return(o<0?(i=Math.round(t*(s=Math.pow(10,-o)/h)),a=Math.round(e*s),i/s<t&&++i,a/s>e&&--a,s=-s):(i=Math.round(t/(s=Math.pow(10,o)*h)),a=Math.round(e/s),i*s<t&&++i,a*s>e&&--a),a<i&&.5<=r&&r<2)?am(t,e,2*r):[i,a,s]}function ag(t,e,r){return am(t*=1,e*=1,r*=1)[2]}function af(t,e){return null==t||null==e?NaN:t<e?-1:t>e?1:t>=e?0:NaN}function av(t,e){return null==t||null==e?NaN:e<t?-1:e>t?1:e>=t?0:NaN}function ay(t){let e,r,i;function a(t,i,s=0,n=t.length){if(s<n){if(0!==e(i,i))return n;do{let e=s+n>>>1;0>r(t[e],i)?s=e+1:n=e}while(s<n)}return s}return 2!==t.length?(e=af,r=(e,r)=>af(t(e),r),i=(e,r)=>t(e)-r):(e=t===af||t===av?t:ab,r=t,i=t),{left:a,center:function(t,e,r=0,s=t.length){let n=a(t,e,r,s-1);return n>r&&i(t[n-1],e)>-i(t[n],e)?n-1:n},right:function(t,i,a=0,s=t.length){if(a<s){if(0!==e(i,i))return s;do{let e=a+s>>>1;0>=r(t[e],i)?a=e+1:s=e}while(a<s)}return a}}}function ab(){return 0}let az=ay(af),ax=az.right;az.left,ay(function(t){return null===t?NaN:+t}).center;function aw(t,e){return t*=1,e*=1,function(r){return Math.round(t*(1-r)+e*r)}}function a$(t){return+t}var ak=[0,1];function aS(t){return t}function a_(t,e){var r;return(e-=t*=1)?function(r){return(r-t)/e}:(r=isNaN(e)?NaN:.5,function(){return r})}function aA(t,e,r){var i=t[0],a=t[1],s=e[0],n=e[1];return a<i?(i=a_(a,i),s=r(n,s)):(i=a_(i,a),s=r(s,n)),function(t){return s(i(t))}}function aM(t,e,r){var i=Math.min(t.length,e.length)-1,a=Array(i),s=Array(i),n=-1;for(t[i]<t[0]&&(t=t.slice().reverse(),e=e.slice().reverse());++n<i;)a[n]=a_(t[n],t[n+1]),s[n]=r(e[n],e[n+1]);return function(e){var r=ax(t,e,1,i)-1;return s[r](a[r](e))}}function aC(t,e){switch(arguments.length){case 0:break;case 1:this.range(t);break;default:this.range(e).domain(t)}return this}function aE(t,e){if(!isFinite(t)||0===t)return null;var r=(t=e?t.toExponential(e-1):t.toExponential()).indexOf("e"),i=t.slice(0,r);return[i.length>1?i[0]+i.slice(2):i,+t.slice(r+1)]}function aT(t){return(t=aE(Math.abs(t)))?t[1]:NaN}var aN=/^(?:(.)?([<>=^]))?([+\-( ])?([$#])?(0)?(\d+)?(,)?(\.\d+)?(~)?([a-z%])?$/i;function aI(t){var e;if(!(e=aN.exec(t)))throw Error("invalid format: "+t);return new aP({fill:e[1],align:e[2],sign:e[3],symbol:e[4],zero:e[5],width:e[6],comma:e[7],precision:e[8]&&e[8].slice(1),trim:e[9],type:e[10]})}function aP(t){this.fill=void 0===t.fill?" ":t.fill+"",this.align=void 0===t.align?">":t.align+"",this.sign=void 0===t.sign?"-":t.sign+"",this.symbol=void 0===t.symbol?"":t.symbol+"",this.zero=!!t.zero,this.width=void 0===t.width?void 0:+t.width,this.comma=!!t.comma,this.precision=void 0===t.precision?void 0:+t.precision,this.trim=!!t.trim,this.type=void 0===t.type?"":t.type+""}function aL(t,e){var r=aE(t,e);if(!r)return t+"";var i=r[0],a=r[1];return a<0?"0."+Array(-a).join("0")+i:i.length>a+1?i.slice(0,a+1)+"."+i.slice(a+1):i+Array(a-i.length+2).join("0")}aI.prototype=aP.prototype,aP.prototype.toString=function(){return this.fill+this.align+this.sign+this.symbol+(this.zero?"0":"")+(void 0===this.width?"":Math.max(1,0|this.width))+(this.comma?",":"")+(void 0===this.precision?"":"."+Math.max(0,0|this.precision))+(this.trim?"~":"")+this.type};let aR={"%":(t,e)=>(100*t).toFixed(e),b:t=>Math.round(t).toString(2),c:t=>t+"",d:function(t){return Math.abs(t=Math.round(t))>=1e21?t.toLocaleString("en").replace(/,/g,""):t.toString(10)},e:(t,e)=>t.toExponential(e),f:(t,e)=>t.toFixed(e),g:(t,e)=>t.toPrecision(e),o:t=>Math.round(t).toString(8),p:(t,e)=>aL(100*t,e),r:aL,s:function(t,e){var r=aE(t,e);if(!r)return eo=void 0,t.toPrecision(e);var i=r[0],a=r[1],s=a-(eo=3*Math.max(-8,Math.min(8,Math.floor(a/3))))+1,n=i.length;return s===n?i:s>n?i+Array(s-n+1).join("0"):s>0?i.slice(0,s)+"."+i.slice(s):"0."+Array(1-s).join("0")+aE(t,Math.max(0,e+s-1))[0]},X:t=>Math.round(t).toString(16).toUpperCase(),x:t=>Math.round(t).toString(16)};function aD(t){return t}var aF=Array.prototype.map,aj=["y","z","a","f","p","n","µ","m","","k","M","G","T","P","E","Z","Y"];eh=(el=function(t){var e,r,i,a=void 0===t.grouping||void 0===t.thousands?aD:(e=aF.call(t.grouping,Number),r=t.thousands+"",function(t,i){for(var a=t.length,s=[],n=0,o=e[0],l=0;a>0&&o>0&&(l+o+1>i&&(o=Math.max(1,i-l)),s.push(t.substring(a-=o,a+o)),!((l+=o+1)>i));)o=e[n=(n+1)%e.length];return s.reverse().join(r)}),s=void 0===t.currency?"":t.currency[0]+"",n=void 0===t.currency?"":t.currency[1]+"",o=void 0===t.decimal?".":t.decimal+"",l=void 0===t.numerals?aD:(i=aF.call(t.numerals,String),function(t){return t.replace(/[0-9]/g,function(t){return i[+t]})}),h=void 0===t.percent?"%":t.percent+"",c=void 0===t.minus?"−":t.minus+"",d=void 0===t.nan?"NaN":t.nan+"";function p(t,e){var r=(t=aI(t)).fill,i=t.align,p=t.sign,u=t.symbol,m=t.zero,g=t.width,f=t.comma,v=t.precision,y=t.trim,b=t.type;"n"===b?(f=!0,b="g"):aR[b]||(void 0===v&&(v=12),y=!0,b="g"),(m||"0"===r&&"="===i)&&(m=!0,r="0",i="=");var z=(e&&void 0!==e.prefix?e.prefix:"")+("$"===u?s:"#"===u&&/[boxX]/.test(b)?"0"+b.toLowerCase():""),x=("$"===u?n:/[%p]/.test(b)?h:"")+(e&&void 0!==e.suffix?e.suffix:""),w=aR[b],$=/[defgprs%]/.test(b);function k(t){var e,s,n,h=z,u=x;if("c"===b)u=w(t)+u,t="";else{var k=(t*=1)<0||1/t<0;if(t=isNaN(t)?d:w(Math.abs(t),v),y&&(t=function(t){t:for(var e,r=t.length,i=1,a=-1;i<r;++i)switch(t[i]){case".":a=e=i;break;case"0":0===a&&(a=i),e=i;break;default:if(!+t[i])break t;a>0&&(a=0)}return a>0?t.slice(0,a)+t.slice(e+1):t}(t)),k&&0==+t&&"+"!==p&&(k=!1),h=(k?"("===p?p:c:"-"===p||"("===p?"":p)+h,u=("s"!==b||isNaN(t)||void 0===eo?"":aj[8+eo/3])+u+(k&&"("===p?")":""),$){for(e=-1,s=t.length;++e<s;)if(48>(n=t.charCodeAt(e))||n>57){u=(46===n?o+t.slice(e+1):t.slice(e))+u,t=t.slice(0,e);break}}}f&&!m&&(t=a(t,1/0));var S=h.length+t.length+u.length,_=S<g?Array(g-S+1).join(r):"";switch(f&&m&&(t=a(_+t,_.length?g-u.length:1/0),_=""),i){case"<":t=h+t+u+_;break;case"=":t=h+_+t+u;break;case"^":t=_.slice(0,S=_.length>>1)+h+t+u+_.slice(S);break;default:t=_+h+t+u}return l(t)}return v=void 0===v?6:/[gprs]/.test(b)?Math.max(1,Math.min(21,v)):Math.max(0,Math.min(20,v)),k.toString=function(){return t+""},k}return{format:p,formatPrefix:function(t,e){var r=3*Math.max(-8,Math.min(8,Math.floor(aT(e)/3))),i=Math.pow(10,-r),a=p(((t=aI(t)).type="f",t),{suffix:aj[8+r/3]});return function(t){return a(i*t)}}}}({thousands:",",grouping:[3],currency:["$",""]})).format,ec=el.formatPrefix;class aH extends Map{constructor(t,e=aB){if(super(),Object.defineProperties(this,{_intern:{value:new Map},_key:{value:e}}),null!=t)for(const[e,r]of t)this.set(e,r)}get(t){return super.get(aO(this,t))}has(t){return super.has(aO(this,t))}set(t,e){return super.set(function({_intern:t,_key:e},r){let i=e(r);return t.has(i)?t.get(i):(t.set(i,r),r)}(this,t),e)}delete(t){return super.delete(function({_intern:t,_key:e},r){let i=e(r);return t.has(i)&&(r=t.get(i),t.delete(i)),r}(this,t))}}function aO({_intern:t,_key:e},r){let i=e(r);return t.has(i)?t.get(i):r}function aB(t){return null!==t&&"object"==typeof t?t.valueOf():t}let aq=Symbol("implicit"),aU=l`
  :host {
    display: block;
    width: 100%;
    background: var(--smzh-color-chart-savings-background);
  }

  .chart-wrap {
    position: relative;
    width: 100%;
    min-height: 280px;
    background: var(--smzh-color-chart-savings-background);
  }

  .chart-svg {
    display: block;
    width: 100%;
    height: 100%;
    overflow: visible;
    background: var(--smzh-color-chart-savings-background);
  }

  .chart-svg .plot-background {
    fill: var(--smzh-color-chart-savings-background);
  }
  .chart-svg :is(.axis-x text, .axis-y text, .y-axis-unit) {
    fill: var(--smzh-color-chart-savings-text);
    font-family: var(
      --smzh-font-family-sans,
      system-ui,
      -apple-system,
      sans-serif
    );
    font-size: 12px;
    font-weight: 400;
  }

  .chart-svg .y-axis-unit {
    font-size: 11px;
  }

  .chart-svg .axis-x path,
  .chart-svg .axis-y path,
  .chart-svg .axis-x line,
  .chart-svg .axis-y line {
    display: none;
  }

  .chart-svg .segment-line {
    shape-rendering: crispEdges;
  }

  .chart-svg .projection-area {
    shape-rendering: geometricPrecision;
  }
  .chart-svg .interaction-hit {
    cursor: pointer;
  }

  .chart-svg .interaction-hit:focus-visible {
    outline: none;
    stroke: var(--smzh-color-border-focus);
    stroke-width: 2px;
  }

  .chart-tooltip {
    position: absolute;
    z-index: 1;
    min-width: 116px;
    padding: var(--smzh-spacing-xx-sm) var(--smzh-spacing-sm);
    border: 1px solid var(--smzh-color-border-default);
    border-radius: var(--smzh-radius-sm);
    background: var(--smzh-color-surface);
    box-shadow: var(--smzh-color-tooltip-shadow);
    color: var(--smzh-color-text-default);
    transform: translate(-50%, calc(-100% - var(--smzh-spacing-sm)));
    pointer-events: none;
    opacity: 0;
    transition: opacity 120ms ease-in-out;
  }

  .chart-tooltip::before,
  .chart-tooltip::after {
    content: "";
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 0;
    pointer-events: none;
  }

  /* Border triangle */
  .chart-tooltip::before {
    bottom: -7px;
    border-left: 7px solid transparent;
    border-right: 7px solid transparent;
    border-top: 7px solid var(--smzh-color-border-default);
  }

  /* White fill triangle */
  .chart-tooltip::after {
    bottom: -6px;
    border-left: 6px solid transparent;
    border-right: 6px solid transparent;
    border-top: 6px solid var(--smzh-color-surface);
  }

  .chart-tooltip[data-visible="true"] {
    opacity: 1;
  }

  .chart-tooltip__year {
    margin: 0 0 calc(var(--smzh-spacing-xx-sm) / 2);
    font-size: var(--smzh-typography-text-xs-font-size);
    color: var(--smzh-color-text-subtle);
  }

  .chart-tooltip__line {
    margin: 0;
    font-size: var(--smzh-typography-text-xs-font-size);
    line-height: 1.2;
  }

  .chart-tooltip__line strong {
    font-weight: var(--smzh-font-weight-medium);
  }
`,aV="#6b7280";"u">typeof window&&!customElements.get("smzh-savings-chart")&&customElements.define("smzh-savings-chart",class extends tp{static styles=aU;static properties={startYear:{type:Number,attribute:"start-year"},periodYears:{type:Number,attribute:"period-years"},yAxisUnit:{type:String,attribute:"y-axis-unit"},hasData:{type:Boolean,attribute:"has-data",reflect:!0},projectionData:{type:String,attribute:"projection-data"},points:{attribute:!1}};resizeObserver=null;chartWidth=0;chartHeight=280;renderIdCounter=0;hasRenderedProjection=!1;projectionSnapshot=null;tooltipState={visible:!1,x:0,y:0,point:null};constructor(){super(),this.startYear=new Date().getFullYear(),this.periodYears=10,this.yAxisUnit="KCHF",this.hasData=!1,this.projectionData="",this.points=[]}connectedCallback(){super.connectedCallback(),this.resizeObserver=new ResizeObserver(t=>{let[e]=t;if(!e)return;let r=Math.max(1,Math.floor(e.contentRect.width)),i=Math.max(280,Math.floor(e.contentRect.height));(r!==this.chartWidth||i!==this.chartHeight)&&(this.chartWidth=r,this.chartHeight=i,this.requestUpdate())})}firstUpdated(){let t=this.renderRoot.querySelector(".chart-wrap");t instanceof HTMLElement&&(this.resizeObserver?.observe(t),this.chartWidth=Math.max(1,Math.floor(t.clientWidth)),this.chartHeight=Math.max(280,Math.floor(t.clientHeight)))}disconnectedCallback(){this.resizeObserver?.disconnect(),this.resizeObserver=null,super.disconnectedCallback()}updated(t){if(super.updated(t),this.chartWidth>0){let e=this.getResolvedPoints(),r=this.shouldRenderArea(e);this.renderD3Chart({animate:this.shouldAnimateProjection(t,r)}),r?this.hasRenderedProjection=!0:t.has("hasData")&&(this.hasRenderedProjection=!1,this.projectionSnapshot=null)}}prefersReducedMotion(){return"u">typeof window&&window.matchMedia("(prefers-reduced-motion: reduce)").matches}shouldAnimateProjection(t,e){return!(!e||this.prefersReducedMotion())&&0!==t.size&&(!!(t.has("hasData")||t.has("points")||t.has("projectionData"))||!this.hasRenderedProjection)}getProjectionSnapshot(t){let e=t[0],r=t[t.length-1];return{lowStart:e.low,lowEnd:r.low,highStart:e.high,highEnd:r.high}}getCollapsedSnapshot(){return{lowStart:0,lowEnd:0,highStart:0,highEnd:0}}getAnimationFromSnapshot(t,e,r){return e?t?this.projectionSnapshot??this.getCollapsedSnapshot():this.getCollapsedSnapshot():r}createWedgePathTween(t,e,r,i,a,s){return n=>{let o=i.lowStart+(a.lowStart-i.lowStart)*n,l=i.lowEnd+(a.lowEnd-i.lowEnd)*n,h=i.highStart+(a.highStart-i.highStart)*n,c=i.highEnd+(a.highEnd-i.highEnd)*n;return"base"===s?this.buildStraightWedgePath(t,e,r,0,0,o,l):this.buildStraightWedgePath(t,e,r,o,l,h,c)}}resolveHasData(){let t=this.hasData;return"string"==typeof t?"true"===t.toLowerCase():!!t}getSafeStartYear(){let t=this.startYear;return"number"==typeof t&&Number.isFinite(t)?Math.round(t):new Date().getFullYear()}getSafePeriodYears(){let t=this.periodYears;return"number"==typeof t&&Number.isFinite(t)?Math.max(0,Math.round(t)):10}getYearDomain(){let t=this.getSafeStartYear();return Array.from({length:this.getSafePeriodYears()+1},(e,r)=>t+r)}isValidPoint(t){return"object"==typeof t&&null!==t&&"number"==typeof t.year&&Number.isFinite(t.year)&&"number"==typeof t.low&&Number.isFinite(t.low)&&"number"==typeof t.high&&Number.isFinite(t.high)&&t.low<=t.high}parseProjectionDataAttribute(t){let e=t.trim();if(0===e.length)return[];try{let t=JSON.parse(e);if(!Array.isArray(t))return[];return t.filter(t=>this.isValidPoint(t))}catch{return[]}}getResolvedPoints(){return Array.isArray(this.points)&&this.points.length>0?this.points.filter(t=>this.isValidPoint(t)):this.parseProjectionDataAttribute(this.projectionData)}shouldRenderArea(t){return this.resolveHasData()&&t.length>=2}getSvgSelection(){let t=this.renderRoot.querySelector("svg.chart-svg");if(!(t instanceof SVGSVGElement))throw Error("[smzh-savings-chart] Missing SVG element in shadow root.");return eW(t)}getYMax(t,e){if(!e||0===t.length)return 60;let r=Math.max(...t.map(t=>t.high));return!Number.isFinite(r)||r<=0?60:Math.max(60,10*Math.ceil(1.2*r/10))}getPointsForDomain(t,e){let r=new Map(e.map(t=>[t.year,t]));return t.map(t=>r.get(t)??{year:t,low:0,high:0})}getSegmentX(t,e){if(t<=0)return 0;let r=e[t]??0;return((e[t-1]??0)+r)/2}snapCoordinate(t){return Math.round(100*t)/100}buildStraightWedgePath(t,e,r,i,a,s,n){let o=this.snapCoordinate(t),l=this.snapCoordinate(e),h=this.snapCoordinate(r(i)),c=this.snapCoordinate(r(a)),d=this.snapCoordinate(r(s)),p=this.snapCoordinate(r(n));return`M ${o} ${h} L ${l} ${c} L ${l} ${p} L ${o} ${d} Z`}appendLayerGradient(t,e,r,i,a,s,n,o){let l=t.append("linearGradient").attr("id",e).attr("gradientUnits","userSpaceOnUse").attr("x1",this.snapCoordinate(r)).attr("y1",this.snapCoordinate(i)).attr("x2",this.snapCoordinate(a)).attr("y2",this.snapCoordinate(s));l.append("stop").attr("offset","0%").attr("stop-color",n),l.append("stop").attr("offset","100%").attr("stop-color",o)}appendStartDot(t,e,r){let i=this.getSafeStartYear();t.append("circle").attr("class","start-dot").attr("cx",e(i)??0).attr("cy",r(0)).attr("r",7).attr("fill","#afd9f4")}formatKchf(t){return new Intl.NumberFormat("de-CH",{maximumFractionDigits:0}).format(Math.round(t))}getTooltipAriaLabel(t){return`Year ${t.year}. Base ${this.formatKchf(t.low)} ${this.yAxisUnit}. Total ${this.formatKchf(t.high)} ${this.yAxisUnit}.`}showTooltip(t,e,r){this.tooltipState={visible:!0,x:e,y:r,point:t},this.requestUpdate()}hideTooltip(){this.tooltipState.visible&&(this.tooltipState={visible:!1,x:0,y:0,point:null},this.requestUpdate())}renderInteractionLayer(t,e,r,i,a,s){let n=e.map((t,i)=>{let s=this.getSegmentX(i,r),n=r[i]??0,o=r[i+1]??a,l=i===e.length-1?a:(n+o)/2;return{point:t,xStart:s,xEnd:l,xCenter:(s+l)/2}}),o=t.append("g").attr("class","interaction-layer").selectAll("rect").data(n).join("rect").attr("class","interaction-hit").attr("x",t=>Math.max(0,t.xStart)).attr("y",0).attr("width",t=>Math.max(8,t.xEnd-t.xStart)).attr("height",s).attr("fill","transparent").attr("tabindex",0).attr("aria-label",t=>this.getTooltipAriaLabel(t.point));o.append("title").text(t=>this.getTooltipAriaLabel(t.point)),o.on("mouseenter",(t,e)=>{this.showTooltip(e.point,56+e.xCenter,28+i(e.point.high))}).on("mousemove",(t,e)=>{this.showTooltip(e.point,56+e.xCenter,28+i(e.point.high))}).on("mouseleave",()=>this.hideTooltip()).on("focus",(t,e)=>{this.showTooltip(e.point,56+e.xCenter,28+i(e.point.high))}).on("blur",()=>this.hideTooltip()).on("keydown",t=>{"Escape"===t.key&&this.hideTooltip()})}renderD3Chart(t={}){let e=t.animate??!1,r=Math.max(1,this.chartWidth),i=Math.max(280,this.chartHeight),a=this.getYearDomain(),s=this.getResolvedPoints().sort((t,e)=>t.year-e.year),n=this.shouldRenderArea(s),o=this.getYMax(s,n),l=this.getPointsForDomain(a,s),h=Math.max(1,r-56-16),c=Math.max(1,i-28-36),d=(function(){return function t(e){var r=e.copy;return e.padding=e.paddingOuter,delete e.paddingInner,delete e.paddingOuter,e.copy=function(){return t(r())},e}((function t(){var e,r,i=(function t(){var e=new aH,r=[],i=[],a=aq;function s(t){let s=e.get(t);if(void 0===s){if(a!==aq)return a;e.set(t,s=r.push(t)-1)}return i[s%i.length]}return s.domain=function(t){if(!arguments.length)return r.slice();for(let i of(r=[],e=new aH,t))e.has(i)||e.set(i,r.push(i)-1);return s},s.range=function(t){return arguments.length?(i=Array.from(t),s):i.slice()},s.unknown=function(t){return arguments.length?(a=t,s):a},s.copy=function(){return t(r,i).unknown(a)},aC.apply(s,arguments),s})().unknown(void 0),a=i.domain,s=i.range,n=0,o=1,l=!1,h=0,c=0,d=.5;function p(){var t=a().length,i=o<n,p=i?o:n,u=i?n:o;e=(u-p)/Math.max(1,t-h+2*c),l&&(e=Math.floor(e)),p+=(u-p-e*(t-h))*d,r=e*(1-h),l&&(p=Math.round(p),r=Math.round(r));var m=(function(t,e,r){t*=1,e*=1,r=(a=arguments.length)<2?(e=t,t=0,1):a<3?1:+r;for(var i=-1,a=0|Math.max(0,Math.ceil((e-t)/r)),s=Array(a);++i<a;)s[i]=t+i*r;return s})(t).map(function(t){return p+e*t});return s(i?m.reverse():m)}return delete i.unknown,i.domain=function(t){return arguments.length?(a(t),p()):a()},i.range=function(t){return arguments.length?([n,o]=t,n*=1,o*=1,p()):[n,o]},i.rangeRound=function(t){return[n,o]=t,n*=1,o*=1,l=!0,p()},i.bandwidth=function(){return r},i.step=function(){return e},i.round=function(t){return arguments.length?(l=!!t,p()):l},i.padding=function(t){return arguments.length?(h=Math.min(1,c=+t),p()):h},i.paddingInner=function(t){return arguments.length?(h=Math.min(1,t),p()):h},i.paddingOuter=function(t){return arguments.length?(c=+t,p()):c},i.align=function(t){return arguments.length?(d=Math.max(0,Math.min(1,t)),p()):d},i.copy=function(){return t(a(),[n,o]).round(l).paddingInner(h).paddingOuter(c).align(d)},aC.apply(p(),arguments)}).apply(null,arguments).paddingInner(1))})().domain(a).range([20,h]).padding(0),p=(function t(){var e,r=(function(){var t,e,r,i,a,s,n=ak,o=ak,l=function t(e,r){var i,a,s=typeof r;return null==r||"boolean"===s?rJ(r):("number"===s?rd:"string"===s?(a=rL(r))?(r=a,r0):r3:r instanceof rL?r0:r instanceof Date?function(t,e){var r=new Date;return t*=1,e*=1,function(i){return r.setTime(t*(1-i)+e*i),r}}:!ArrayBuffer.isView(i=r)||i instanceof DataView?Array.isArray(r)?function(e,r){var i,a=r?r.length:0,s=e?Math.min(a,e.length):0,n=Array(s),o=Array(a);for(i=0;i<s;++i)n[i]=t(e[i],r[i]);for(;i<a;++i)o[i]=r[i];return function(t){for(i=0;i<s;++i)o[i]=n[i](t);return o}}:"function"!=typeof r.valueOf&&"function"!=typeof r.toString||isNaN(r)?function(e,r){var i,a={},s={};for(i in(null===e||"object"!=typeof e)&&(e={}),(null===r||"object"!=typeof r)&&(r={}),r)i in e?a[i]=t(e[i],r[i]):s[i]=r[i];return function(t){for(i in a)s[i]=a[i](t);return s}}:rd:function(t,e){e||(e=[]);var r,i=t?Math.min(e.length,t.length):0,a=e.slice();return function(s){for(r=0;r<i;++r)a[r]=t[r]*(1-s)+e[r]*s;return a}})(e,r)},h=aS;function c(){var t,e,r,l=Math.min(n.length,o.length);return h!==aS&&(t=n[0],e=n[l-1],t>e&&(r=t,t=e,e=r),h=function(r){return Math.max(t,Math.min(e,r))}),i=l>2?aM:aA,a=s=null,d}function d(e){return null==e||isNaN(e*=1)?r:(a||(a=i(n.map(t),o,l)))(t(h(e)))}return d.invert=function(r){return h(e((s||(s=i(o,n.map(t),rd)))(r)))},d.domain=function(t){return arguments.length?(n=Array.from(t,a$),c()):n.slice()},d.range=function(t){return arguments.length?(o=Array.from(t),c()):o.slice()},d.rangeRound=function(t){return o=Array.from(t),l=aw,c()},d.clamp=function(t){return arguments.length?(h=!!t||aS,c()):h!==aS},d.interpolate=function(t){return arguments.length?(l=t,c()):l},d.unknown=function(t){return arguments.length?(r=t,d):r},function(r,i){return t=r,e=i,c()}})()(aS,aS);return r.copy=function(){return t().domain(r.domain()).range(r.range()).interpolate(r.interpolate()).clamp(r.clamp()).unknown(r.unknown())},aC.apply(r,arguments),e=r.domain,r.ticks=function(t){var r=e();return function(t,e,r){if(e*=1,t*=1,!((r*=1)>0))return[];if(t===e)return[t];let i=e<t,[a,s,n]=i?am(e,t,r):am(t,e,r);if(!(s>=a))return[];let o=s-a+1,l=Array(o);if(i)if(n<0)for(let t=0;t<o;++t)l[t]=-((s-t)/n);else for(let t=0;t<o;++t)l[t]=(s-t)*n;else if(n<0)for(let t=0;t<o;++t)l[t]=-((a+t)/n);else for(let t=0;t<o;++t)l[t]=(a+t)*n;return l}(r[0],r[r.length-1],null==t?10:t)},r.tickFormat=function(t,r){var i=e();return function(t,e,r,i){let a,s;var n,o,l,h,c,d=(o=t,l=+e,o*=1,h=+r,s=(a=l<o)?ag(l,o,h):ag(o,l,h),(a?-1:1)*(s<0?-(1/s):s));switch((i=aI(null==i?",f":i)).type){case"s":var p=Math.max(Math.abs(t),Math.abs(e));return null!=i.precision||isNaN(c=Math.max(0,3*Math.max(-8,Math.min(8,Math.floor(aT(p)/3)))-aT(Math.abs(d))))||(i.precision=c),ec(i,p);case"":case"e":case"g":case"p":case"r":null!=i.precision||isNaN(c=Math.max(0,aT(Math.abs(Math.max(Math.abs(t),Math.abs(e)))-(n=Math.abs(n=d)))-aT(n))+1)||(i.precision=c-("e"===i.type));break;case"f":case"%":null!=i.precision||isNaN(c=Math.max(0,-aT(Math.abs(d))))||(i.precision=c-("%"===i.type)*2)}return eh(i)}(i[0],i[i.length-1],null==t?10:t,r)},r.nice=function(t){null==t&&(t=10);var i,a,s=e(),n=0,o=s.length-1,l=s[n],h=s[o],c=10;for(h<l&&(a=l,l=h,h=a,a=n,n=o,o=a);c-- >0;){if((a=ag(l,h,t))===i)return s[n]=l,s[o]=h,e(s);if(a>0)l=Math.floor(l/a)*a,h=Math.ceil(h/a)*a;else if(a<0)l=Math.ceil(l*a)/a,h=Math.floor(h*a)/a;else break;i=a}return r},r})().domain([0,o]).range([c,0]),u=this.getSvgSelection();u.selectAll("*").remove(),u.attr("viewBox",`0 0 ${r} ${i}`);let m=u.append("g").attr("class","plot").attr("transform","translate(56,28)");m.append("rect").attr("class","plot-background").attr("width",h).attr("height",c);let g=a.map(t=>d(t)??0);if(n){this.renderIdCounter+=1;let t=this.renderIdCounter,r=m.append("defs"),i=l[0],s=l[l.length-1],o=g[0]??0,d=g[g.length-1]??0,u=`savings-base-gradient-${t}`,f=`savings-top-gradient-${t}`;this.appendLayerGradient(r,u,o,p(i.low),d,p(s.low),"#fbfdfe","#eef7fd"),this.appendLayerGradient(r,f,o,p(i.high),d,p(s.high),"#afd9f4","#e3f2fb");let v=this.getProjectionSnapshot(l),y=this.getAnimationFromSnapshot(n,e,v),b=this.buildStraightWedgePath(o,d,p,0,0,y.lowStart,y.lowEnd),z=this.buildStraightWedgePath(o,d,p,y.lowStart,y.lowEnd,y.highStart,y.highEnd),x=m.append("path").attr("class","projection-area projection-area--base").attr("fill",`url(#${u})`).attr("d",b),w=m.append("path").attr("class","projection-area projection-area--top").attr("fill",`url(#${f})`).attr("d",z);if(e){let t=()=>{this.projectionSnapshot=v};x.transition().duration(720).attrTween("d",()=>this.createWedgePathTween(o,d,p,y,v,"base")).on("end",t),w.transition().duration(720).attrTween("d",()=>this.createWedgePathTween(o,d,p,y,v,"top"))}else x.attr("d",this.buildStraightWedgePath(o,d,p,0,0,v.lowStart,v.lowEnd)),w.attr("d",this.buildStraightWedgePath(o,d,p,v.lowStart,v.lowEnd,v.highStart,v.highEnd)),this.projectionSnapshot=v;this.renderInteractionLayer(m,l,g,p,h,c);let $=m.append("g").attr("class","dividers").selectAll("line").data(a.map((t,e)=>e).filter(t=>t>0)).join("line").attr("class","segment-line").attr("x1",t=>this.getSegmentX(t,g)).attr("x2",t=>this.getSegmentX(t,g)).attr("y1",0).attr("y2",c).attr("stroke","#f8f8fa").attr("stroke-width",2).attr("opacity",+!e);e&&$.transition().delay(360).duration(360).attr("opacity",1)}else this.hideTooltip();let f=ac(3,d).tickSize(0).tickPadding(10).tickFormat(t=>String(t)),v=ac(4,p).ticks(6).tickSize(0).tickPadding(12).tickFormat(t=>String(Math.round(Number(t))));m.append("g").attr("class","axis-x").attr("transform",`translate(0,${c})`).call(f).selectAll("text").attr("fill",aV),m.append("g").attr("class","axis-y").call(v).selectAll("text").attr("fill",aV),m.append("text").attr("class","y-axis-unit").attr("x",0).attr("y",-10).attr("fill",aV).text(this.yAxisUnit.trim()||"KCHF"),this.appendStartDot(m,d,p)}render(){let t=this.tooltipState.point,e=this.tooltipState.visible&&null!==t,r=`left:${this.tooltipState.x}px;top:${this.tooltipState.y}px;`;return W`
      <section class="chart-wrap" aria-label="Savings projection chart">
        <svg class="chart-svg" role="img" aria-hidden="true"></svg>
        <div
          class="chart-tooltip"
          style=${r}
          data-visible=${e?"true":"false"}
          aria-hidden=${e?"false":"true"}
        >
          ${t?W`
                <p class="chart-tooltip__year">${t.year}</p>
                <p class="chart-tooltip__line">
                  Base:
                  <strong
                    >${this.formatKchf(t.low)}
                    ${this.yAxisUnit}</strong
                  >
                </p>
                <p class="chart-tooltip__line">
                  Total:
                  <strong
                    >${this.formatKchf(t.high)}
                    ${this.yAxisUnit}</strong
                  >
                </p>
              `:null}
        </div>
      </section>
    `}});let aW=l`
  :host {
    display: inline-block;
    max-width: 100%;
    vertical-align: top;
  }

  :host([hidden]) {
    display: none !important;
  }

  .tab {
    background: var(--smzh-color-tabs-surface);
    border: 1px solid var(--smzh-color-tabs-border);
    border-radius: var(--smzh-spacing-x-big);
    box-sizing: border-box;
    color: var(--smzh-color-tabs-text);
    cursor: pointer;
    display: inline-flex;
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-sm-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-medium);
    letter-spacing: 0;
    line-height: var(--smzh-spacing-big);
    margin: 0;
    max-width: 100%;
    min-width: 0;
    padding: calc(var(--smzh-spacing-sm) - 1px)
      calc(var(--smzh-spacing-big) - 1px);
    text-align: center;
    transition:
      border-color 140ms ease,
      background-color 140ms ease,
      box-shadow 140ms ease,
      color 140ms ease,
      opacity 140ms ease;
    white-space: nowrap;
  }

  .tab:disabled {
    cursor: not-allowed;
    opacity: 0.45;
  }

  .tab:hover:not(:disabled) {
    border-color: var(--smzh-color-tabs-border-selected);
  }

  .tab:focus {
    outline: none;
  }

  .tab:focus-visible {
    outline: 2px solid var(--smzh-color-border-focus);
    outline-offset: 2px;
  }

  :host([selected]) .tab {
    background: var(--smzh-color-tabs-surface);
    border-color: var(--smzh-color-tabs-border-selected);
    box-shadow: var(--smzh-color-tabs-shadow);
    color: var(--smzh-color-tabs-text);
  }

  .label {
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .tab--switcher {
    background: transparent;
    border: 0 solid var(--smzh-color-tabs-switcher-surface);
    border-radius: var(--smzh-spacing-big);
    color: var(--smzh-color-tabs-switcher-text);
    justify-content: center;
    letter-spacing: var(--smzh-typography-text-sm-letter-spacing);
    line-height: var(--smzh-typography-text-sm-line-height);
    min-height: var(--smzh-spacing-lg);
    min-width: var(--smzh-tabs-min-width, 0);
    padding: var(--smzh-spacing-xxx-sm) var(--smzh-spacing-x-sm);
  }

  .tab--switcher:hover:not(:disabled) {
    background: var(--smzh-color-tabs-switcher-surface-hover);
    border-color: var(--smzh-color-tabs-switcher-surface-hover);
    color: var(--smzh-color-tabs-switcher-text-hover);
  }

  :host([selected]) .tab--switcher {
    background: var(--smzh-color-tabs-switcher-surface);
    border-color: var(--smzh-color-tabs-switcher-surface);
    box-shadow: var(--smzh-color-tabs-switcher-shadow);
    color: var(--smzh-color-tabs-switcher-text-selected);
  }

  :host([selected]) .tab--switcher:hover:not(:disabled) {
    background: var(--smzh-color-tabs-switcher-surface);
    color: var(--smzh-color-tabs-switcher-text-selected);
  }
`;"u">typeof window&&!customElements.get("smzh-tabs")&&customElements.define("smzh-tabs",class extends tp{static styles=aW;static properties={value:{type:String,reflect:!0},selected:{type:Boolean,reflect:!0},disabled:{type:Boolean,reflect:!0},groupMode:{type:Boolean,state:!0},visualVariant:{type:String,state:!0}};constructor(){super(),this.value="",this.selected=!1,this.disabled=!1,this.groupMode=!1,this.visualVariant="default"}setGroupMode(t,e="default"){(this.groupMode!==t||this.visualVariant!==e)&&(this.groupMode=t,this.visualVariant=e,this.requestUpdate())}roleForTab(){return this.groupMode?"tab":"button"}handleClick=()=>{if(this.disabled)return;let t=this.value?.trim()??"";if(0===t.length)return;let e=new CustomEvent("smzh-tabs-press",{bubbles:!0,composed:!0,cancelable:!0,detail:{value:t}});this.dispatchEvent(e),!e.defaultPrevented&&(this.groupMode||(this.selected=!this.selected))};render(){let t=this.roleForTab(),e="tab"===t?this.selected?"true":"false":void 0,r="button"===t?this.selected?"true":"false":void 0;return W`
      <button
        class=${"switcher"===this.visualVariant?"tab tab--switcher":"tab"}
        part="control"
        type="button"
        role=${t}
        ?disabled=${this.disabled}
        aria-selected=${e??Z}
        aria-pressed=${r??Z}
        @click=${this.handleClick}
      >
        <span class="label" part="label">
          <slot></slot>
        </span>
      </button>
    `}});let aG=l`
  :host {
    display: block;
    width: 100%;
  }

  :host([hidden]) {
    display: none !important;
  }

  .root {
    display: flex;
    flex-direction: column;
    gap: var(--smzh-spacing-x-sm);
    width: 100%;
  }

  .label.is-empty {
    display: none;
  }

  .label::slotted(*) {
    color: var(--smzh-tabs-group-label-color, var(--smzh-color-text-brand));
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-md-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    letter-spacing: var(--smzh-typography-text-md-letter-spacing);
    line-height: var(--smzh-typography-text-md-line-height);
    margin: 0;
  }

  .tabs {
    display: flex;
    flex-wrap: wrap;
    gap: var(--smzh-spacing-x-big);
    width: 100%;
  }

  :host([variant="switcher"]) .tabs {
    align-items: center;
    background: var(--smzh-color-tabs-switcher-track-surface);
    border-radius: var(--smzh-spacing-x-big);
    box-sizing: border-box;
    display: inline-flex;
    flex-wrap: nowrap;
    gap: 6px;
    max-width: 100%;
    overflow-x: auto;
    padding: 4px;
    width: max-content;
  }
`;class aX extends tp{static styles=aG;labelId=`smzh-tabs-group-label-${Math.random().toString(36).slice(2,10)}`;static properties={value:{type:String,reflect:!0},variant:{type:String,reflect:!0},hasLabel:{type:Boolean,state:!0}};constructor(){super(),this.value="",this.variant="default",this.hasLabel=!1}connectedCallback(){super.connectedCallback(),this.addEventListener("smzh-tabs-press",this.handleTabPress)}disconnectedCallback(){this.removeEventListener("smzh-tabs-press",this.handleTabPress),super.disconnectedCallback()}updated(){this.syncTabs()}getTabChildren(){return Array.from(this.querySelectorAll("smzh-tabs"))}syncTabs(){let t=this.getTabChildren(),e=this.value?.trim()??"",r="switcher"===this.variant?"switcher":"default";for(let i of t){i.setGroupMode(!0,r);let t=i.value?.trim()??"";i.selected=t.length>0&&t===e}}emitChange(){this.dispatchEvent(new CustomEvent("smzh-tabs-group-change",{bubbles:!0,composed:!0,detail:{value:this.value?.trim()??""}}))}handleTabPress=t=>{let e=t.target;if(!e||!this.contains(e))return;t.stopPropagation(),t.preventDefault();let r=t.detail?.value?.trim()??"";0!==r.length&&(this.value=r,this.emitChange())};handleSlotChange=()=>{this.syncTabs()};handleLabelSlotChange=t=>{let e=t.target;this.hasLabel=e.assignedNodes({flatten:!0}).some(t=>t.textContent?.trim()||t.nodeType===Node.ELEMENT_NODE)};render(){let t=this.hasLabel?this.labelId:void 0;return W`
      <div
        class="root"
        part="root"
        role="tablist"
        aria-labelledby=${t??Z}
      >
        <slot
          name="label"
          class=${this.hasLabel?"label":"label is-empty"}
          part="label"
          id=${this.labelId}
          @slotchange=${this.handleLabelSlotChange}
        ></slot>
        <div class="tabs" part="tabs">
          <slot @slotchange=${this.handleSlotChange}></slot>
        </div>
      </div>
    `}}"u">typeof window&&!customElements.get("smzh-tabs-group")&&customElements.define("smzh-tabs-group",aX);let aY=l`
  :host {
    --smzh-budget-line-item-gap: var(--smzh-spacing-md);
    --smzh-budget-line-item-leading-gap: var(--smzh-spacing-xxx-sm);
    --smzh-budget-line-item-icon-size: 32px;
    --smzh-budget-line-item-icon-radius: 8px;
    --smzh-budget-line-item-field-width: 194px;
    --smzh-budget-line-item-field-min-width: 160px;
    --smzh-budget-line-item-summary-padding: 12px;
    --smzh-budget-line-item-summary-radius: 16px;
    --smzh-budget-line-item-summary-field-radius: 14px;

    display: block;
    width: 100%;
  }

  :host([hidden]) {
    display: none !important;
  }

  .stack {
    display: flex;
    flex-direction: column;
    gap: var(--smzh-spacing-xxx-sm);
    width: 100%;
  }

  .root {
    align-items: center;
    display: flex;
    flex-wrap: wrap;
    gap: var(--smzh-budget-line-item-gap);
    justify-content: space-between;
    width: 100%;
  }

  :host([variant="summary"]) .root {
    background: var(--smzh-color-surface);
    border-radius: var(--smzh-budget-line-item-summary-radius);
    box-shadow: var(
      --smzh-budget-line-item-summary-shadow,
      var(--smzh-color-budget-line-item-summary-shadow)
    );
    padding: var(--smzh-budget-line-item-summary-padding);
  }

  .leading {
    align-items: center;
    display: flex;
    flex: 0 1 auto;
    gap: var(--smzh-budget-line-item-leading-gap);
    min-width: 0;
  }

  .icon-chip {
    align-items: center;
    background: var(
      --smzh-budget-line-item-icon-surface,
      var(
        --smzh-color-budget-line-item-icon-surface-accent,
        var(--smzh-color-primary)
      )
    );
    border-radius: var(--smzh-budget-line-item-icon-radius);
    color: var(
      --smzh-budget-line-item-icon-color,
      var(
        --smzh-color-budget-line-item-icon-foreground,
        var(--smzh-color-text-inverse)
      )
    );
    display: inline-flex;
    flex: 0 0 auto;
    height: var(--smzh-budget-line-item-icon-size);
    justify-content: center;
    width: var(--smzh-budget-line-item-icon-size);
  }

  .icon-chip[data-variant="summary"] {
    background: var(
      --smzh-budget-line-item-icon-surface,
      linear-gradient(
        90deg,
        var(
            --smzh-budget-line-item-icon-gradient-start,
            var(--smzh-color-budget-line-item-icon-gradient-start)
          )
          15.705%,
        var(
            --smzh-budget-line-item-icon-gradient-end,
            var(--smzh-color-budget-line-item-icon-gradient-end)
          )
          95.192%
      )
    );
  }

  .icon-chip[data-tone="warning"] {
    background: var(
      --smzh-budget-line-item-icon-surface,
      var(
        --smzh-color-budget-line-item-icon-surface-warning,
        var(--smzh-color-warning)
      )
    );
  }

  .icon-chip[data-tone="neutral"] {
    background: var(
      --smzh-budget-line-item-icon-surface,
      var(
        --smzh-color-budget-line-item-icon-surface-neutral,
        var(--smzh-color-border-default)
      )
    );
  }

  .icon-chip ::slotted(*) {
    display: block;
    flex: 0 0 auto;
    max-height: 20px;
    max-width: 20px;
  }

  .label {
    min-width: 0;
  }

  .label ::slotted(*) {
    margin: 0;
  }

  .field {
    flex: 0 0 var(--smzh-budget-line-item-field-width);
    margin-inline-start: auto;
    max-width: 100%;
    min-width: min(100%, var(--smzh-budget-line-item-field-min-width));
    width: min(100%, var(--smzh-budget-line-item-field-width));
  }

  .field smzh-input {
    --smzh-input-value-color: var(--smzh-color-text-form-value);
    --smzh-input-readonly-value-color: var(--smzh-color-text-form-value);
    --smzh-input-placeholder-color: var(--smzh-color-text-input-soft);

    width: 100%;
  }

  .field ::slotted(smzh-select) {
    --smzh-select-value-color: var(--smzh-color-text-form-value);
    --smzh-select-chevron-color: var(--smzh-color-text-form-value);

    width: 100%;
  }

  .field smzh-input[variant="filled"] {
    --smzh-color-background-subtle: var(--smzh-color-surface);
    --smzh-color-border-default: transparent;
  }

  .summary-value {
    align-items: center;
    border-radius: var(--smzh-budget-line-item-summary-field-radius);
    box-sizing: border-box;
    color: var(--smzh-color-text-form-value);
    display: flex;
    gap: var(--smzh-spacing-x-sm);
    justify-content: flex-end;
    min-height: calc(
      var(--smzh-typography-text-sm-line-height) + 2 *
        var(--smzh-budget-line-item-summary-padding)
    );
    padding: var(--smzh-budget-line-item-summary-padding);
    width: 100%;
  }

  .summary-value-text {
    color: var(--smzh-color-text-form-value);
    flex: 1 1 auto;
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-sm-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-medium);
    letter-spacing: calc(var(--smzh-typography-text-sm-letter-spacing) * 0.14);
    line-height: 24px;
    min-width: 0;
    text-align: right;
  }

  .summary-suffix {
    color: var(--smzh-color-text-input-soft);
    flex: 0 0 auto;
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-sm-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    letter-spacing: calc(var(--smzh-typography-text-sm-letter-spacing) * 0.14);
    line-height: 24px;
    white-space: nowrap;
  }

  :host([variant="filled"]) .field ::slotted(smzh-select) {
    --smzh-select-border-color: transparent;
  }

  .field ::slotted(*) {
    width: 100%;
  }

  .supporting-text {
    color: var(--smzh-color-text-input-soft);
    font-family: var(--smzh-font-family-sans);
    font-size: var(--smzh-typography-text-sm-font-size);
    font-style: normal;
    font-weight: var(--smzh-font-weight-normal);
    letter-spacing: var(--smzh-typography-text-sm-letter-spacing);
    line-height: var(--smzh-typography-text-sm-line-height);
    margin-inline-start: calc(
      var(--smzh-budget-line-item-icon-size) +
        var(--smzh-budget-line-item-leading-gap)
    );
  }

  .supporting-text ::slotted(*) {
    margin: 0;
  }

  @media (max-width: 520px) {
    .leading,
    .field {
      flex-basis: 100%;
    }

    .field {
      margin-inline-start: 0;
      width: 100%;
    }

    .supporting-text {
      margin-inline-start: 0;
    }
  }
`,aZ=["default","filled","summary"],aK=["accent","warning","neutral"],aJ="accent";function aQ(t){return function(){return t}}"u">typeof window&&!customElements.get("smzh-budget-line-item")&&customElements.define("smzh-budget-line-item",class extends tp{static styles=aY;static properties={icon:{type:String,reflect:!0},label:{type:String},value:{type:String},placeholder:{type:String},ariaLabel:{type:String,attribute:"aria-label"},iconBackground:{type:String,attribute:"icon-background",reflect:!0},iconColor:{type:String,attribute:"icon-color",reflect:!0},fieldWidth:{type:String,attribute:"field-width",reflect:!0},name:{type:String,reflect:!0},inputmode:{type:String},amountFormat:{type:String,attribute:"amount-format"},disabled:{type:Boolean,reflect:!0},readonly:{type:Boolean,reflect:!0},variant:{type:String,reflect:!0},suffix:{type:String,reflect:!0},maxlength:{type:String,reflect:!0},digitsOnly:{type:Boolean,reflect:!0,attribute:"digits-only"},destructive:{type:Boolean,reflect:!0},iconTone:{type:String,reflect:!0,attribute:"icon-tone"}};constructor(){super(),this.icon=void 0,this.label="",this.value="",this.placeholder="",this.ariaLabel=null,this.iconBackground="",this.iconColor="",this.fieldWidth="",this.name="",this.inputmode=void 0,this.amountFormat=void 0,this.disabled=!1,this.readonly=!1,this.variant=tB,this.suffix="CHF",this.maxlength="",this.digitsOnly=!1,this.destructive=!1,this.iconTone=aJ}hasSlottedContent(t){return Array.from(this.children).some(e=>e.getAttribute("slot")===t)}slottedTextContent(t){return Array.from(this.children).filter(e=>e.getAttribute("slot")===t).map(t=>t.textContent?.trim()??"").find(t=>t.length>0)??""}resolveIcon(){return t_(this.icon)?this.icon:void 0}resolveVariant(){var t;return"string"==typeof(t=this.variant)&&aZ.includes(t)?this.variant:tB}resolveInputVariant(){return tq(this.variant)?this.variant:tB}resolveIconTone(){var t;return"string"==typeof(t=this.iconTone)&&aK.includes(t)?this.iconTone:aJ}resolveAmountFormat(){return tX(this.amountFormat)?this.amountFormat:void 0}resolveInputMode(){return tG(this.inputmode)?this.inputmode:void 0}resolveAriaLabel(){let t=this.ariaLabel?.trim();if(t)return t;let e=this.label?.trim();if(e)return e;let r=this.slottedTextContent("label");return r||this.getAttribute("aria-label")?.trim()||void 0}resolveSuffix(){let t=this.suffix?.trim();return t&&t.length>0?t:"CHF"}resolveDisplayValue(){let t=this.value?.trim();if(t&&t.length>0)return t;let e=this.placeholder?.trim();return e&&e.length>0?e:""}resolveIconStyle(){let t=[],e=this.iconBackground?.trim(),r=this.iconColor?.trim();return e&&t.push(`--smzh-budget-line-item-icon-surface: ${e};`),r&&t.push(`--smzh-budget-line-item-icon-color: ${r};`),t.length>0?t.join(" "):void 0}resolveFieldStyle(){let t=this.fieldWidth?.trim();return t?`--smzh-budget-line-item-field-width: ${t};`:void 0}handleInput=t=>{t.stopPropagation();let e=t.currentTarget;this.value=e?.value??"",this.dispatchEvent(new Event("input",{bubbles:!0,composed:!0}))};handleChange=t=>{t.stopPropagation();let e=t.currentTarget;this.value=e?.value??"",this.dispatchEvent(new Event("change",{bubbles:!0,composed:!0}))};render(){var t;let e=this.hasSlottedContent("icon"),r=this.resolveIcon(),i=this.hasSlottedContent("label"),a=this.hasSlottedContent("field"),s=this.hasSlottedContent("supporting-text"),n=this.label?.trim()??"",o=this.resolveVariant(),l=this.resolveIconStyle(),h=this.resolveFieldStyle();return W`
      <div class="stack" part="stack">
        <div class="root" part="root">
          <div class="leading" part="leading">
            ${e||r?W`
                  <span
                    class="icon-chip"
                    part="icon-chip"
                    data-tone=${this.resolveIconTone()}
                    data-variant=${o}
                    style=${l??Z}
                    aria-hidden="true"
                  >
                    <slot name="icon">
                      ${r?(t={size:20,stroke:"var(--smzh-budget-line-item-icon-color, var(--smzh-color-budget-line-item-icon-foreground, var(--smzh-color-text-inverse)))"},tS[r](t)):Z}
                    </slot>
                  </span>
                `:Z}

            <div class="label" part="label">
              <slot name="label">
                ${i?Z:W`
                      <smzh-typography as="p" variant="text-sm" weight="normal">
                        ${n}
                      </smzh-typography>
                    `}
              </slot>
            </div>
          </div>

          <div class="field" part="field" style=${h??Z}>
            <slot name="field">
              ${a?Z:"summary"===o?W`
                      <div
                        class="summary-value"
                        part="summary-value"
                        aria-label=${this.resolveAriaLabel()??Z}
                      >
                        <span class="summary-value-text">
                          ${this.resolveDisplayValue()}
                        </span>
                        <span class="summary-suffix">
                          ${this.resolveSuffix()}
                        </span>
                      </div>
                    `:W`
                      <smzh-input
                        .value=${this.value??""}
                        placeholder=${this.placeholder??""}
                        aria-label=${this.resolveAriaLabel()??Z}
                        name=${(this.name?.trim()?this.name:void 0)??Z}
                        inputmode=${this.resolveInputMode()??Z}
                        amount-format=${this.resolveAmountFormat()??Z}
                        ?disabled=${this.disabled}
                        ?readonly=${this.readonly}
                        variant=${this.resolveInputVariant()}
                        suffix=${this.resolveSuffix()}
                        maxlength=${(this.maxlength?.trim()?this.maxlength:void 0)??Z}
                        ?digits-only=${this.digitsOnly}
                        ?destructive=${this.destructive}
                        @input=${this.handleInput}
                        @change=${this.handleChange}
                      ></smzh-input>
                    `}
            </slot>
          </div>
        </div>

        ${s?W`
              <div class="supporting-text" part="supporting-text">
                <slot name="supporting-text"></slot>
              </div>
            `:Z}
      </div>
    `}});let a0=Math.abs,a1=Math.atan2,a2=Math.cos,a4=Math.max,a3=Math.min,a5=Math.sin,a8=Math.sqrt,a6=Math.PI,a9=a6/2,a7=2*a6;function st(t){return t>=1?a9:t<=-1?-a9:Math.asin(t)}let se=Math.PI,sr=2*se,si=sr-1e-6;function sa(t){this._+=t[0];for(let e=1,r=t.length;e<r;++e)this._+=arguments[e]+t[e]}class ss{constructor(t){this._x0=this._y0=this._x1=this._y1=null,this._="",this._append=null==t?sa:function(t){let e=Math.floor(t);if(!(e>=0))throw Error(`invalid digits: ${t}`);if(e>15)return sa;let r=10**e;return function(t){this._+=t[0];for(let e=1,i=t.length;e<i;++e)this._+=Math.round(arguments[e]*r)/r+t[e]}}(t)}moveTo(t,e){this._append`M${this._x0=this._x1=+t},${this._y0=this._y1=+e}`}closePath(){null!==this._x1&&(this._x1=this._x0,this._y1=this._y0,this._append`Z`)}lineTo(t,e){this._append`L${this._x1=+t},${this._y1=+e}`}quadraticCurveTo(t,e,r,i){this._append`Q${+t},${+e},${this._x1=+r},${this._y1=+i}`}bezierCurveTo(t,e,r,i,a,s){this._append`C${+t},${+e},${+r},${+i},${this._x1=+a},${this._y1=+s}`}arcTo(t,e,r,i,a){if(t*=1,e*=1,r*=1,i*=1,(a*=1)<0)throw Error(`negative radius: ${a}`);let s=this._x1,n=this._y1,o=r-t,l=i-e,h=s-t,c=n-e,d=h*h+c*c;if(null===this._x1)this._append`M${this._x1=t},${this._y1=e}`;else if(d>1e-6)if(Math.abs(c*o-l*h)>1e-6&&a){let p=r-s,u=i-n,m=o*o+l*l,g=Math.sqrt(m),f=Math.sqrt(d),v=a*Math.tan((se-Math.acos((m+d-(p*p+u*u))/(2*g*f)))/2),y=v/f,b=v/g;Math.abs(y-1)>1e-6&&this._append`L${t+y*h},${e+y*c}`,this._append`A${a},${a},0,0,${+(c*p>h*u)},${this._x1=t+b*o},${this._y1=e+b*l}`}else this._append`L${this._x1=t},${this._y1=e}`}arc(t,e,r,i,a,s){if(t*=1,e*=1,r*=1,s=!!s,r<0)throw Error(`negative radius: ${r}`);let n=r*Math.cos(i),o=r*Math.sin(i),l=t+n,h=e+o,c=1^s,d=s?i-a:a-i;null===this._x1?this._append`M${l},${h}`:(Math.abs(this._x1-l)>1e-6||Math.abs(this._y1-h)>1e-6)&&this._append`L${l},${h}`,r&&(d<0&&(d=d%sr+sr),d>si?this._append`A${r},${r},0,1,${c},${t-n},${e-o}A${r},${r},0,1,${c},${this._x1=l},${this._y1=h}`:d>1e-6&&this._append`A${r},${r},0,${+(d>=se)},${c},${this._x1=t+r*Math.cos(a)},${this._y1=e+r*Math.sin(a)}`)}rect(t,e,r,i){this._append`M${this._x0=this._x1=+t},${this._y0=this._y1=+e}h${r*=1}v${+i}h${-r}Z`}toString(){return this._}}function sn(t){return t.innerRadius}function so(t){return t.outerRadius}function sl(t){return t.startAngle}function sh(t){return t.endAngle}function sc(t){return t&&t.padAngle}function sd(t,e,r,i,a,s,n){var o=t-r,l=e-i,h=(n?s:-s)/a8(o*o+l*l),c=h*l,d=-h*o,p=t+c,u=e+d,m=r+c,g=i+d,f=(p+m)/2,v=(u+g)/2,y=m-p,b=g-u,z=y*y+b*b,x=a-s,w=p*g-m*u,$=(b<0?-1:1)*a8(a4(0,x*x*z-w*w)),k=(w*b-y*$)/z,S=(-w*y-b*$)/z,_=(w*b+y*$)/z,A=(-w*y+b*$)/z,M=k-f,C=S-v,E=_-f,T=A-v;return M*M+C*C>E*E+T*T&&(k=_,S=A),{cx:k,cy:S,x01:-c,y01:-d,x11:k*(a/x-1),y11:S*(a/x-1)}}function sp(){let t;var e=sn,r=so,i=aQ(0),a=null,s=sl,n=sh,o=sc,l=null,h=(t=3,c.digits=function(e){if(!arguments.length)return t;if(null==e)t=null;else{let r=Math.floor(e);if(!(r>=0))throw RangeError(`invalid digits: ${e}`);t=r}return c},()=>new ss(t));function c(){var t,c,d=+e.apply(this,arguments),p=+r.apply(this,arguments),u=s.apply(this,arguments)-a9,m=n.apply(this,arguments)-a9,g=a0(m-u),f=m>u;if(l||(l=t=h()),p<d&&(c=p,p=d,d=c),p>1e-12)if(g>a7-1e-12)l.moveTo(p*a2(u),p*a5(u)),l.arc(0,0,p,u,m,!f),d>1e-12&&(l.moveTo(d*a2(m),d*a5(m)),l.arc(0,0,d,m,u,f));else{var v,y,b=u,z=m,x=u,w=m,$=g,k=g,S=o.apply(this,arguments)/2,_=S>1e-12&&(a?+a.apply(this,arguments):a8(d*d+p*p)),A=a3(a0(p-d)/2,+i.apply(this,arguments)),M=A,C=A;if(_>1e-12){var E=st(_/d*a5(S)),T=st(_/p*a5(S));($-=2*E)>1e-12?(E*=f?1:-1,x+=E,w-=E):($=0,x=w=(u+m)/2),(k-=2*T)>1e-12?(T*=f?1:-1,b+=T,z-=T):(k=0,b=z=(u+m)/2)}var N=p*a2(b),I=p*a5(b),P=d*a2(w),L=d*a5(w);if(A>1e-12){var R,D=p*a2(z),F=p*a5(z),j=d*a2(x),H=d*a5(x);if(g<a6)if(R=function(t,e,r,i,a,s,n,o){var l=r-t,h=i-e,c=n-a,d=o-s,p=d*l-c*h;if(!(p*p<1e-12))return p=(c*(e-s)-d*(t-a))/p,[t+p*l,e+p*h]}(N,I,j,H,D,F,P,L)){var O,B=N-R[0],q=I-R[1],U=D-R[0],V=F-R[1],W=1/a5(((O=(B*U+q*V)/(a8(B*B+q*q)*a8(U*U+V*V)))>1?0:O<-1?a6:Math.acos(O))/2),G=a8(R[0]*R[0]+R[1]*R[1]);M=a3(A,(d-G)/(W-1)),C=a3(A,(p-G)/(W+1))}else M=C=0}k>1e-12?C>1e-12?(v=sd(j,H,N,I,p,C,f),y=sd(D,F,P,L,p,C,f),l.moveTo(v.cx+v.x01,v.cy+v.y01),C<A?l.arc(v.cx,v.cy,C,a1(v.y01,v.x01),a1(y.y01,y.x01),!f):(l.arc(v.cx,v.cy,C,a1(v.y01,v.x01),a1(v.y11,v.x11),!f),l.arc(0,0,p,a1(v.cy+v.y11,v.cx+v.x11),a1(y.cy+y.y11,y.cx+y.x11),!f),l.arc(y.cx,y.cy,C,a1(y.y11,y.x11),a1(y.y01,y.x01),!f))):(l.moveTo(N,I),l.arc(0,0,p,b,z,!f)):l.moveTo(N,I),d>1e-12&&$>1e-12?M>1e-12?(v=sd(P,L,D,F,d,-M,f),y=sd(N,I,j,H,d,-M,f),l.lineTo(v.cx+v.x01,v.cy+v.y01),M<A?l.arc(v.cx,v.cy,M,a1(v.y01,v.x01),a1(y.y01,y.x01),!f):(l.arc(v.cx,v.cy,M,a1(v.y01,v.x01),a1(v.y11,v.x11),!f),l.arc(0,0,d,a1(v.cy+v.y11,v.cx+v.x11),a1(y.cy+y.y11,y.cx+y.x11),f),l.arc(y.cx,y.cy,M,a1(y.y11,y.x11),a1(y.y01,y.x01),!f))):l.arc(0,0,d,w,x,f):l.lineTo(P,L)}else l.moveTo(0,0);if(l.closePath(),t)return l=null,t+""||null}return c.centroid=function(){var t=(+e.apply(this,arguments)+ +r.apply(this,arguments))/2,i=(+s.apply(this,arguments)+ +n.apply(this,arguments))/2-a6/2;return[a2(i)*t,a5(i)*t]},c.innerRadius=function(t){return arguments.length?(e="function"==typeof t?t:aQ(+t),c):e},c.outerRadius=function(t){return arguments.length?(r="function"==typeof t?t:aQ(+t),c):r},c.cornerRadius=function(t){return arguments.length?(i="function"==typeof t?t:aQ(+t),c):i},c.padRadius=function(t){return arguments.length?(a=null==t?null:"function"==typeof t?t:aQ(+t),c):a},c.startAngle=function(t){return arguments.length?(s="function"==typeof t?t:aQ(+t),c):s},c.endAngle=function(t){return arguments.length?(n="function"==typeof t?t:aQ(+t),c):n},c.padAngle=function(t){return arguments.length?(o="function"==typeof t?t:aQ(+t),c):o},c.context=function(t){return arguments.length?(l=null==t?null:t,c):l},c}function su(t,e){return e<t?-1:e>t?1:e>=t?0:NaN}function sm(t){return t}ss.prototype,Array.prototype.slice;let sg=l`
  :host {
    display: block;
    width: 100%;
  }

  .chart-wrap {
    --smzh-budget-chart-inner-ratio: 0.68;
    aspect-ratio: 1;
    background: var(--smzh-color-chart-budget-background);
    border-radius: 50%;
    display: grid;
    margin: 0 auto;
    max-width: var(--smzh-budget-chart-max-size, 320px);
    place-items: center;
    position: relative;
    width: 100%;
  }

  .center-disc {
    background: var(--smzh-color-chart-budget-center);
    border-radius: 50%;
    box-shadow: var(--smzh-color-chart-budget-center-shadow);
    height: calc(var(--smzh-budget-chart-inner-ratio, 0.68) * 100%);
    pointer-events: none;
    position: absolute;
    width: calc(var(--smzh-budget-chart-inner-ratio, 0.68) * 100%);
    z-index: 0;
  }

  .chart-svg {
    block-size: 100%;
    inline-size: 100%;
    position: relative;
    z-index: 1;
  }

  .chart-svg .segment {
    cursor: pointer;
    stroke: var(--smzh-color-chart-budget-segment-border);
    stroke-linejoin: round;
  }

  .chart-svg .track {
    cursor: default;
    stroke: var(--smzh-color-chart-budget-segment-border);
    stroke-linejoin: round;
  }

  .center {
    display: flex;
    flex-direction: column;
    gap: var(--smzh-spacing-xxx-sm);
    inset: 0;
    justify-content: center;
    opacity: 1;
    pointer-events: none;
    position: absolute;
    text-align: center;
    transition: opacity 400ms ease 180ms;
    z-index: 2;
  }

  .chart-wrap[data-entering] .center {
    opacity: 0;
  }

  .amount {
    color: var(--smzh-color-chart-budget-amount);
    font-size: var(--smzh-budget-chart-amount-size, 1.5rem);
    font-weight: 600;
    line-height: 1.2;
    margin: 0;
  }

  .subtitle {
    color: var(--smzh-color-chart-budget-subtitle);
    font-size: var(--smzh-budget-chart-subtitle-size, 0.875rem);
    font-weight: 400;
    line-height: 1.3;
    margin: 0;
  }
`,sf="var(--smzh-color-chart-budget-track)",sv="var(--smzh-color-chart-budget-segment-border)",sy=0,sb=0;class sz extends tp{static styles=sg;static properties={subtitle:{type:String},currency:{type:String},locale:{type:String},segmentsData:{type:String,attribute:"segments-data"},segments:{attribute:!1},animateEntrance:{type:Boolean,attribute:"animate-entrance"}};resizeObserver=null;chartSize=200;hasRenderedData=!1;centerEntranceActive=!1;hoveredSegmentIndex=-1;chartInnerRadius=0;chartOuterRadius=0;lastActiveSegments=[];lastTotal=0;ringShadowFilterId=`smzh-budget-ring-shadow-${++sy}`;revealClipId=`smzh-budget-reveal-clip-${++sb}`;constructor(){super(),this.subtitle="Total Expenditure",this.currency="CHF",this.locale="de-CH",this.segmentsData="",this.segments=[],this.animateEntrance=!0}connectedCallback(){super.connectedCallback(),this.resizeObserver=new ResizeObserver(t=>{let[e]=t;if(!e)return;let r=Math.max(200,Math.floor(Math.min(e.contentRect.width,e.contentRect.height)));r!==this.chartSize&&(this.chartSize=r,this.requestUpdate())})}firstUpdated(){let t=this.renderRoot.querySelector(".chart-wrap");if(t instanceof HTMLElement){this.resizeObserver?.observe(t),t.addEventListener("mouseleave",()=>{this.setHoveredIndex(-1)});let e=Math.max(1,Math.floor(t.clientWidth)),r=Math.max(1,Math.floor(t.clientHeight));this.chartSize=Math.max(200,Math.floor(Math.min(e,r)))}this.renderD3Chart({animate:!1})}disconnectedCallback(){this.resizeObserver?.disconnect(),this.resizeObserver=null,super.disconnectedCallback()}willUpdate(t){let e=this.getTotal(this.getResolvedSegments())>0;if(!e){this.centerEntranceActive=!1;return}if(this.shouldAnimate(t,e)){this.centerEntranceActive=!0;return}e&&(this.centerEntranceActive=!1)}updated(t){try{super.updated(t)}catch{}let e=t.has("segments")||t.has("segmentsData")||t.has("currency")||t.has("locale"),r=this.getTotal(this.getResolvedSegments())>0,i=this.shouldAnimate(t,r);e&&(this.hoveredSegmentIndex=-1),e&&r&&!i&&(this.centerEntranceActive=!1),this.syncChartVisualization({animate:i}),r?this.hasRenderedData=!0:this.hasRenderedData=!1}refreshChart(t={}){if(!(this.renderRoot.querySelector("svg.chart-svg")instanceof SVGSVGElement)){this.requestUpdate(),this.updateComplete.then(()=>{this.syncChartVisualization({animate:t.animate??!1})});return}this.syncChartVisualization({animate:t.animate??!1})}syncChartVisualization(t={}){this.renderD3Chart({animate:t.animate??!1})}shouldAnimate(t,e){return!(!this.animateEntrance||!e||this.prefersReducedMotion())&&!this.hasRenderedData&&(t.has("segments")||t.has("segmentsData"))}prefersReducedMotion(){return"u">typeof window&&window.matchMedia("(prefers-reduced-motion: reduce)").matches}getHoverTransitionMs(){return 150*!this.prefersReducedMotion()}isValidSegment(t){return"object"==typeof t&&null!==t&&"number"==typeof t.value&&Number.isFinite(t.value)&&t.value>=0&&"string"==typeof t.color&&t.color.trim().length>0&&(void 0===t.label||"string"==typeof t.label)}getHoveredSegment(t){return this.hoveredSegmentIndex<0||this.hoveredSegmentIndex>=t.length?null:t[this.hoveredSegmentIndex]??null}formatValue(t){let e=Math.round(t).toLocaleString(this.locale);return`${this.currency} ${e}`}parseSegmentsDataAttribute(t){let e=t.trim();if(0===e.length)return[];try{let t=JSON.parse(e);if(!Array.isArray(t))return[];return t.filter(t=>this.isValidSegment(t))}catch{return[]}}getResolvedSegments(){let t=Array.isArray(this.segments)&&this.segments.length>0?this.segments.filter(t=>this.isValidSegment(t)):[],e=this.parseSegmentsDataAttribute(this.segmentsData);return 0===t.length?e:0===e.length?t:this.getTotal(e)>=this.getTotal(t)?e:t}getActiveSegments(t){return t.filter(t=>t.value>0)}getTotal(t){return this.getActiveSegments(t).reduce((t,e)=>t+e.value,0)}formatTotal(t){return this.formatValue(t)}createArcGenerator(t,e,r){return sp().innerRadius(t).outerRadius(r?1.015*e:e)}clockRevealClipTween(t,e){let r=sp().innerRadius(t).outerRadius(e);return t=>r({startAngle:0,endAngle:0+2*Math.PI*t})??""}easeOutQuad(t){return t*(2-t)}finishCenterEntrance(){this.revealCenterDisplay()}revealCenterDisplay(){this.centerEntranceActive=!1;let t=this.renderRoot.querySelector(".chart-wrap");t instanceof HTMLElement&&t.removeAttribute("data-entering");let e=this.renderRoot.querySelector(".center");e instanceof HTMLElement&&(e.style.opacity="1")}setHoveredIndex(t,e=null){this.hoveredSegmentIndex!==t&&(this.hoveredSegmentIndex=t,e instanceof SVGPathElement&&eW(e).raise(),this.applyHoverVisuals(),this.updateCenterDisplay())}updateCenterDisplay(){let t=this.getHoveredSegment(this.lastActiveSegments),e=this.renderRoot.querySelector(".amount"),r=this.renderRoot.querySelector(".subtitle"),i=this.renderRoot.querySelector(".chart-wrap"),a=t?this.formatValue(t.value):this.formatTotal(this.lastTotal),s=t?.label?.trim()?t.label:this.subtitle;e&&(e.textContent=a),r&&(r.textContent=s),i instanceof HTMLElement&&(t?(i.setAttribute("data-hovered",""),i.setAttribute("aria-label",`${a}, ${s}`)):(i.removeAttribute("data-hovered"),i.setAttribute("aria-label",`${a}, ${this.subtitle}`)))}applyHoverVisuals(){if(this.chartOuterRadius<=0)return;let t=this.getHoverTransitionMs(),e=this.hoveredSegmentIndex;this.getSvgSelection().select("g.chart-layer").selectAll("path.segment").interrupt().transition().duration(t).attr("opacity",t=>e>=0&&t.index!==e?.88:1).attr("d",t=>{let r=t.index===e;return this.createArcGenerator(this.chartInnerRadius,this.chartOuterRadius,r)(t)??""})}bindSegmentInteractions(t){t.on("mouseenter",(t,e)=>{this.setHoveredIndex(e.index,t.currentTarget)}).on("focus",(t,e)=>{this.setHoveredIndex(e.index,t.currentTarget)}).on("blur",()=>{this.setHoveredIndex(-1)})}getSvgSelection(){let t=this.renderRoot.querySelector("svg.chart-svg");if(!(t instanceof SVGSVGElement))throw Error("[smzh-budget-chart] Missing SVG element in shadow root.");return eW(t)}getRadii(t){let e=t/2;return{innerRadius:.68*e,outerRadius:.95*e}}ensureRingShadowFilter(t){let e=this.ringShadowFilterId,r=t.selectAll("defs").data([0]).join("defs"),i=r.select(`filter#${e}`);i.empty()&&(i=r.append("filter").attr("id",e)),i.attr("x","-40%").attr("y","-40%").attr("width","180%").attr("height","180%").attr("filterUnits","objectBoundingBox"),i.selectAll("*").remove(),i.append("feDropShadow").attr("dx",0).attr("dy",2).attr("stdDeviation",3).attr("flood-color","#101828").attr("flood-opacity",.06)}ensureRevealClipPath(t){let e=this.revealClipId,r=t.select("defs");if(r.empty())return;let i=r.select(`clipPath#${e}`);i.empty()&&(i=r.append("clipPath").attr("id",e)),i.selectAll("path.reveal-clip").data([0]).join("path").attr("class","reveal-clip")}renderD3Chart(t={}){let e=t.animate??!1,r=Math.max(200,this.chartSize),i=r/2,{innerRadius:a,outerRadius:s}=this.getRadii(r);this.chartInnerRadius=a,this.chartOuterRadius=s;let n=this.getResolvedSegments(),o=this.getActiveSegments(n),l=this.getTotal(n);this.lastActiveSegments=o,this.lastTotal=l;let h=this.getSvgSelection().attr("viewBox",`0 0 ${r} ${r}`);this.ensureRingShadowFilter(h),this.ensureRevealClipPath(h);let c=h.selectAll("g.chart-layer").data([0]).join("g").attr("class","chart-layer").attr("transform",`translate(${i},${i})`).attr("filter",`url(#${this.ringShadowFilterId})`),d=sp().innerRadius(a).outerRadius(s).startAngle(t=>t.startAngle).endAngle(t=>t.endAngle),p=(function(){var t=sm,e=su,r=null,i=aQ(0),a=aQ(a7),s=aQ(0);function n(n){var o,l,h,c,d,p,u=(n="object"==typeof(o=n)&&"length"in o?o:Array.from(o)).length,m=0,g=Array(u),f=Array(u),v=+i.apply(this,arguments),y=Math.min(a7,Math.max(-a7,a.apply(this,arguments)-v)),b=Math.min(Math.abs(y)/u,s.apply(this,arguments)),z=b*(y<0?-1:1);for(l=0;l<u;++l)(p=f[g[l]=l]=+t(n[l],l,n))>0&&(m+=p);for(null!=e?g.sort(function(t,r){return e(f[t],f[r])}):null!=r&&g.sort(function(t,e){return r(n[t],n[e])}),l=0,c=m?(y-u*z)/m:0;l<u;++l,v=d)d=v+((p=f[h=g[l]])>0?p*c:0)+z,f[h]={data:n[h],index:l,value:p,startAngle:v,endAngle:d,padAngle:b};return f}return n.value=function(e){return arguments.length?(t="function"==typeof e?e:aQ(+e),n):t},n.sortValues=function(t){return arguments.length?(e=t,r=null,n):e},n.sort=function(t){return arguments.length?(r=t,e=null,n):r},n.startAngle=function(t){return arguments.length?(i="function"==typeof t?t:aQ(+t),n):i},n.endAngle=function(t){return arguments.length?(a="function"==typeof t?t:aQ(+t),n):a},n.padAngle=function(t){return arguments.length?(s="function"==typeof t?t:aQ(+t),n):s},n})().value(t=>t.value).sort(null),u={startAngle:0,endAngle:2*Math.PI};if(l<=0){this.hoveredSegmentIndex=-1,c.selectAll("path.segment").data([]).join("path").remove(),c.selectAll("path.track").data([u]).join("path").attr("class","track").attr("fill",sf).attr("stroke",sv).attr("stroke-width",2).transition().duration(320).attr("d",t=>d(t)??""),this.updateCenterDisplay();return}let m=p(o);this.hoveredSegmentIndex>=0&&this.hoveredSegmentIndex>=m.length&&(this.hoveredSegmentIndex=-1),c.selectAll("path.track").data([u]).join("path").attr("class","track").attr("fill",sf).attr("stroke",sv).attr("stroke-width",2).attr("d",t=>d(t)??"");let g=c.selectAll("g.segments-clip").data([0]).join("g").attr("class","segments-clip").attr("clip-path",`url(#${this.revealClipId})`).selectAll("path.segment").data(m,t=>String(t.index)).join(t=>t.append("path").attr("class","segment").attr("fill",t=>t.data.color).attr("stroke",sv).attr("stroke-width",2).attr("opacity",1).attr("tabindex",0).attr("role","graphics-symbol").attr("aria-label",t=>`${t.data.label??"Category"}: ${this.formatValue(t.data.value)}`),t=>t,t=>t.remove());this.bindSegmentInteractions(g);let f=t=>{let e=t.index===this.hoveredSegmentIndex;return this.createArcGenerator(a,s,e)(t)??""};g.attr("fill",t=>t.data.color).attr("stroke",sv).attr("stroke-width",2).attr("opacity",1).attr("d",f);let v=sp().innerRadius(a).outerRadius(s),y=h.select(`clipPath#${this.revealClipId} path.reveal-clip`),b=v({startAngle:0,endAngle:0+2*Math.PI})??"";e?y.interrupt().attr("d",v({startAngle:0,endAngle:0})??"").transition().duration(720).ease(t=>this.easeOutQuad(t)).attrTween("d",()=>this.clockRevealClipTween(a,s)).on("end",()=>{y.attr("d",b),this.finishCenterEntrance()}).on("interrupt",()=>{y.attr("d",b),this.finishCenterEntrance()}):(y.interrupt().attr("d",b),this.finishCenterEntrance()),this.applyHoverVisuals(),this.updateCenterDisplay(),(!e||l<=0)&&this.revealCenterDisplay()}render(){let t=this.getTotal(this.getResolvedSegments()),e=this.formatTotal(t);return W`
      <div
        class="chart-wrap"
        aria-label=${`${e}, ${this.subtitle}`}
        data-entering=${this.centerEntranceActive?"":Z}
      >
        <div class="center-disc" aria-hidden="true"></div>
        <svg class="chart-svg" role="img" aria-hidden="true"></svg>
        <div class="center">
          <p class="amount">${e}</p>
          <p class="subtitle">${this.subtitle}</p>
        </div>
      </div>
    `}}"u">typeof window&&!customElements.get("smzh-budget-chart")&&customElements.define("smzh-budget-chart",sz),t.s(["default",0,function(){return null}],939919)}]);

//# sourceMappingURL=0o6emi165z2g_.js.map