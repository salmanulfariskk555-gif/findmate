import React from "react";
import {
  Heart, ShieldCheck, Sparkles, MessageCircle, ArrowRight, Menu,
  Check, LockKeyhole, Users, Compass, ChevronDown, Star, Leaf
} from "lucide-react";

const values = [
  { icon: ShieldCheck, title: "Safety before everything", text: "Privacy-first profiles, reporting tools and a community built around respect." },
  { icon: Sparkles, title: "Compatibility with intention", text: "Look beyond quick swipes. Focus on values, interests and the future you want." },
  { icon: MessageCircle, title: "Conversations that matter", text: "A mutual connection comes first. Private messaging will follow in a later release." }
];

const questions = [
  ["Who is FindMate for?", "FindMate is being designed for adults aged 18 and above who are interested in serious relationships and marriage."],
  ["Can I create an account now?", "Not yet. This is the public design preview. Registration will open only after verification, privacy and moderation features are ready."],
  ["Will my profile be public?", "Profiles are designed to stay hidden by default until the member chooses visibility and the profile passes the planned review process."],
  ["Is the mobile app ready?", "The Android app is in development. This website preview is the first visual step."],
];

function Brand() {
  return <a className="brand" href="#home" aria-label="FindMate home"><span className="brand-mark"><Heart size={18} fill="currentColor" /></span><span>findmate<span className="brand-period">.</span></span></a>;
}

function SampleProfile({ name, age, city, initials, tone, tags }) {
  return <article className="sample-card">
    <div className={`sample-avatar ${tone}`}><span>{initials}</span><i><Check size={12}/></i></div>
    <div className="sample-info"><div className="sample-name">{name}, {age}</div><div className="sample-city">{city}</div><div className="sample-tags">{tags.map(tag => <span key={tag}>{tag}</span>)}</div></div>
    <div className="sample-heart"><Heart size={17}/></div>
  </article>;
}

export default function App() {
  return <main id="home">
    <div className="announcement"><span className="announcement-dot"/> FindMate is taking shape — explore our first website preview <a href="#preview">See the vision <ArrowRight size={13}/></a></div>
    <header className="site-header wrap">
      <Brand />
      <nav className="desktop-nav" aria-label="Main navigation">
        <a href="#why">Why FindMate</a><a href="#how">How it works</a><a href="#safety">Safety</a><a href="#faq">FAQs</a>
      </nav>
      <a className="header-cta" href="#preview">Explore preview <ArrowRight size={15}/></a>
      <a className="mobile-menu" href="#mobile-nav" aria-label="Jump to navigation"><Menu size={22}/></a>
    </header>
    <nav id="mobile-nav" className="mobile-nav wrap"><a href="#why">Why FindMate</a><a href="#how">How it works</a><a href="#safety">Safety</a><a href="#faq">FAQs</a></nav>

    <section className="hero wrap">
      <div className="hero-copy">
        <div className="eyebrow"><span className="eyebrow-line"/> MADE FOR MEANINGFUL CONNECTIONS</div>
        <h1>Find someone<br/>to build <em>a life with.</em></h1>
        <p className="hero-description">Not just another match. A thoughtful place for adults who are ready for a genuine relationship, shared values and a future together.</p>
        <div className="hero-buttons"><a className="primary-button" href="#how">Discover FindMate <ArrowRight size={17}/></a><a className="secondary-button" href="#why">Why we're different</a></div>
        <div className="hero-trust"><span><ShieldCheck size={16}/> Privacy-minded</span><span><Users size={16}/> Adults 18+</span><span><Heart size={16}/> Serious intentions</span></div>
      </div>
      <div className="hero-visual" aria-label="Illustration of two profile cards and a heart">
        <div className="visual-halo halo-a"/><div className="visual-halo halo-b"/>
        <div className="floating-label label-top"><Sparkles size={15}/> Shared values matter</div>
        <div className="profile-art art-back"><div className="art-photo art-photo-two"><span className="art-sun"/></div><div className="art-lines"><b/><i/></div></div>
        <div className="profile-art art-front"><div className="art-photo art-photo-one"><span className="art-flower">✳</span><span className="art-figure"/></div><div className="art-caption"><div><b>A meaningful beginning</b><small>Connection starts with conversation</small></div><span className="art-heart"><Heart size={18} fill="currentColor"/></span></div></div>
        <div className="floating-label label-bottom"><span className="label-check"><Check size={12}/></span> A little more intentional</div>
        <div className="visual-spark spark-one">✦</div><div className="visual-spark spark-two">✧</div>
      </div>
    </section>

    <section className="marquee-strip"><div className="wrap strip-inner"><span>HONESTY</span><i>✦</i><span>COMPATIBILITY</span><i>✦</i><span>RESPECT</span><i>✦</i><span>COMMITMENT</span><i>✦</i><span>MEANINGFUL CONNECTIONS</span></div></section>

    <section className="intro-section" id="why"><div className="wrap intro-grid">
      <div><div className="eyebrow"><span className="eyebrow-line"/> A BETTER WAY TO BEGIN</div><h2>Because your<br/>future deserves<br/><em>more than a swipe.</em></h2></div>
      <div className="intro-copy"><p>Finding the right person is about more than a profile picture. It is about shared values, trust, kindness and the things that make a relationship last.</p><p>FindMate is being created with one clear purpose: help people meet with sincerity and move towards meaningful relationships.</p><a className="underlined-link" href="#how">See how it will work <ArrowRight size={15}/></a></div>
    </div></section>

    <section className="features-section wrap" id="how">
      <div className="section-heading"><div><div className="eyebrow"><span className="eyebrow-line"/> SIMPLE. THOUGHTFUL. INTENTIONAL.</div><h2>Connection, with <em>purpose.</em></h2></div><p>A clearer path from discovering someone to building a genuine connection.</p></div>
      <div className="feature-grid">{values.map(({icon:Icon,title,text},index)=><article className="feature-card" key={title}><div className="feature-top"><span className="feature-icon"><Icon size={22}/></span><span className="feature-index">0{index+1}</span></div><h3>{title}</h3><p>{text}</p></article>)}</div>
    </section>

    <section className="preview-section" id="preview"><div className="wrap preview-grid">
      <div className="preview-copy"><div className="eyebrow"><span className="eyebrow-line"/> A GLIMPSE OF WHAT'S AHEAD</div><h2>Meet beyond<br/>the <em>profile.</em></h2><p>Our future discovery experience is being designed to make the important things easier to notice — values, interests, intentions and compatibility.</p><div className="preview-points"><span><Check size={15}/> Profiles with personality</span><span><Check size={15}/> Shared interests and values</span><span><Check size={15}/> Member-controlled visibility</span></div><small>Illustrative sample cards only — not real members.</small></div>
      <div className="sample-stack"><div className="sample-topline"><span><Compass size={15}/> DISCOVERY PREVIEW</span><span className="preview-pill">Concept design</span></div><SampleProfile name="Aarav" age="28" city="Kochi · Kerala" initials="A" tone="tone-one" tags={["Family values","Travel"]}/><SampleProfile name="Mira" age="26" city="Calicut · Kerala" initials="M" tone="tone-two" tags={["Books","Nature"]}/><SampleProfile name="Ishaan" age="30" city="Thrissur · Kerala" initials="I" tone="tone-three" tags={["Faith","Growth"]}/><div className="sample-foot"><LockKeyhole size={14}/> Your privacy stays in your hands.</div></div>
    </div></section>

    <section className="safety-section wrap" id="safety"><div className="safety-art"><div className="safety-ring"><div className="safety-shield"><ShieldCheck size={48}/></div></div><span className="safety-star star-a">✦</span><span className="safety-star star-b">✧</span></div><div className="safety-copy"><div className="eyebrow"><span className="eyebrow-line"/> TRUST IS THE STARTING POINT</div><h2>A meaningful match<br/>begins with <em>feeling safe.</em></h2><p>We believe a serious relationship platform must take privacy and member wellbeing seriously from day one.</p><div className="safety-list"><div><Check size={16}/> Private-by-default profile design</div><div><Check size={16}/> Planned profile review and approval</div><div><Check size={16}/> Block and report tools in the foundation</div></div></div></section>

    <section className="faq-section" id="faq"><div className="wrap faq-grid"><div><div className="eyebrow"><span className="eyebrow-line"/> GOOD TO KNOW</div><h2>A few things<br/>you might <em>wonder.</em></h2><p>We're building carefully, and we'd rather be clear about what's ready and what's still on the way.</p></div><div className="faq-list">{questions.map(([q,a])=><details key={q}><summary>{q}<ChevronDown size={18}/></summary><p>{a}</p></details>)}</div></div></section>

    <section className="closing-section"><div className="wrap closing-inner"><div className="closing-heart"><Heart size={23} fill="currentColor"/></div><div className="eyebrow">THE NEXT CHAPTER STARTS WITH INTENTION</div><h2>Make space for<br/><em>something meaningful.</em></h2><p>FindMate is in development. We're building the experience with care before opening it to members.</p><a className="light-button" href="#home">Back to the beginning <ArrowRight size={16}/></a><div className="closing-note"><LockKeyhole size={13}/> Registration is not open in this preview.</div></div></section>

    <footer className="site-footer wrap"><Brand/><div className="footer-links"><a href="#why">About</a><a href="#safety">Safety</a><a href="#faq">FAQs</a></div><div className="footer-legal">© {new Date().getFullYear()} FindMate · Adults 18+ only</div></footer>
  </main>;
}
