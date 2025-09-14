import React, { useEffect, useRef } from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';
import Lenis from 'lenis';
import './ScrollStack.css';

const ScrollStack = ({ children }) => {
  const containerRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start end", "end start"]
  });

  useEffect(() => {
    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true,
    });

    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }

    requestAnimationFrame(raf);

    return () => {
      lenis.destroy();
    };
  }, []);

  return (
    <div ref={containerRef} className="scroll-stack-container">
      <div className="scroll-stack">
        {children}
      </div>
    </div>
  );
};

const ScrollStackItem = ({ children, index = 0 }) => {
  const itemRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: itemRef,
    offset: ["start end", "end start"]
  });

  // Create staggered transforms for each card
  const y = useTransform(scrollYProgress, [0, 0.5, 1], [100, 0, -100]);
  const scale = useTransform(scrollYProgress, [0, 0.5, 1], [0.8, 1, 0.8]);
  const opacity = useTransform(scrollYProgress, [0, 0.2, 0.8, 1], [0, 1, 1, 0]);
  const rotate = useTransform(scrollYProgress, [0, 0.5, 1], [-5, 0, 5]);

  return (
    <motion.div
      ref={itemRef}
      className="scroll-stack-item"
      style={{
        y,
        scale,
        opacity,
        rotate,
        zIndex: 10 - index,
      }}
      initial={{ opacity: 0, y: 50 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ 
        duration: 0.8, 
        delay: index * 0.2,
        ease: "easeOut" 
      }}
      viewport={{ once: true, amount: 0.3 }}
    >
      {children}
    </motion.div>
  );
};

export default ScrollStack;
export { ScrollStackItem };
