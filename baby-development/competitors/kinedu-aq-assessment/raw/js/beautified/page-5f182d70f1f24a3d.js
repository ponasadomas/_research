(self.webpackChunk_N_E = self.webpackChunk_N_E || []).push([
  [595], {
    1976: function(e, t, a) {
      Promise.resolve().then(a.bind(a, 178))
    },
    178: function(e, t, a) {
      "use strict";
      a.d(t, {
        default: function() {
          return X
        }
      });
      var s = a(7437),
        l = a(2265),
        n = a(6125),
        r = a(9845);
      let o = {
          Physical: "#3B82F6",
          Cognitive: "#22C55E",
          Language: "#F97316",
          "Social-Emotional": "#EC4899"
        },
        i = {
          Physical: "\uD83D\uDC63",
          Cognitive: "\uD83E\uDDE9",
          Language: "\uD83D\uDCAC",
          "Social-Emotional": "\uD83D\uDE42"
        },
        d = {
          blue: "#087BF3",
          navy: "#081B46",
          text: "#132351",
          sub: "#52607A",
          line: "#EBE6DF",
          bg: "#FFFDF9",
          green: "#32C99A"
        },
        c = n.FB;

      function u(e, t) {
        var a, s, l;
        let n = null !== (l = null === (a = c[e]) || void 0 === a ? void 0 : a[t]) && void 0 !== l ? l : null === (s = c.en) || void 0 === s ? void 0 : s[t];
        return "string" == typeof n ? n : ""
      }

      function m(e, t) {
        return e.replace(/\{(\w+)\}/g, (e, a) => {
          var s;
          return String(null !== (s = t[a]) && void 0 !== s ? s : "")
        })
      }

      function x(e) {
        let t = e.split(/\*\*(.+?)\*\*/g);
        return (0, s.jsx)(s.Fragment, {
          children: t.map((e, t) => t % 2 ? (0, s.jsx)("strong", {
            children: e
          }, t) : (0, s.jsx)("span", {
            children: e
          }, t))
        })
      }

      function p(e) {
        e("quiz_answer", "paywall_handoff"), (0, r.iA)("InitiateCheckout", {
          content_category: "acquisition",
          content_name: "assessment"
        }), location.href = function() {
          let e;
          try {
            e = new URLSearchParams(location.search)
          } catch (t) {
            e = new URLSearchParams
          }
          let t = (e.get("paywall") || "").trim();
          /^[a-z0-9][a-z0-9-]{0,31}$/.test(t) || (t = "trial3"), e.set("from", "assessment");
          let a = e.toString();
          return "/aq-paywall-".concat(t, "/index.html").concat(a ? "?".concat(a) : "")
        }()
      }

      function h(e) {
        let {
          children: t
        } = e;
        return (0, s.jsxs)("div", {
          className: "min-h-screen",
          style: {
            background: d.bg,
            color: d.text,
            fontFamily: "'DM Sans', -apple-system, sans-serif"
          },
          children: [(0, s.jsx)("link", {
            href: "https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700;9..40,800&display=swap",
            rel: "stylesheet"
          }), (0, s.jsx)("div", {
            className: "mx-auto flex min-h-screen w-full max-w-md flex-col px-5 pb-10 pt-6",
            children: t
          })]
        })
      }

      function b() {
        return (0, s.jsx)("img", {
          src: "/promo-flash/Kinedu_Logo_Color.png",
          alt: "Kinedu",
          className: "mx-auto mb-4 h-7 w-auto"
        })
      }

      function g(e) {
        let {
          onClick: t,
          children: a,
          color: l = d.blue,
          disabled: n
        } = e;
        return (0, s.jsx)("button", {
          onClick: t,
          disabled: n,
          className: "mt-6 w-full rounded-2xl px-6 py-4 text-[17px] font-bold text-white transition-transform active:scale-[0.98] disabled:opacity-40",
          style: {
            background: l
          },
          children: a
        })
      }

      function y(e) {
        let {
          children: t
        } = e;
        return (0, s.jsx)("h1", {
          className: "text-[26px] font-extrabold leading-tight",
          style: {
            letterSpacing: "-0.045em"
          },
          children: t
        })
      }

      function f(e) {
        let {
          s: t,
          color: a,
          age: l
        } = e, n = {
          l: 30,
          r: 10,
          t: 8,
          b: 18
        }, r = t.curve;
        if (r.length < 2) return null;
        let o = r[0].age,
          i = r[r.length - 1].age,
          c = e => n.l + (e - o) / Math.max(i - o, 1) * (320 - n.l - n.r),
          u = e => n.t + (1 - e) * (130 - n.t - n.b),
          m = r.map(e => "".concat(c(e.age), ",").concat(u(e.pct))).join(" "),
          x = [...r.map(e => "".concat(c(e.age), ",").concat(u(e.hi))), ...[...r].reverse().map(e => "".concat(c(e.age), ",").concat(u(e.lo)))].join(" "),
          p = c(Math.min(Math.max(l, o), i)),
          h = u(Math.min(Math.max(t.childPct, 0), 1));
        return (0, s.jsxs)("svg", {
          viewBox: "0 0 ".concat(320, " ").concat(130),
          className: "w-full",
          role: "img",
          "aria-label": "How ".concat(t.skill, " typically develops, with your child's position"),
          children: [
            [0, .5, 1].map(e => (0, s.jsxs)("g", {
              children: [(0, s.jsx)("line", {
                x1: n.l,
                x2: 320 - n.r,
                y1: u(e),
                y2: u(e),
                stroke: d.line,
                strokeWidth: "1"
              }), (0, s.jsxs)("text", {
                x: n.l - 4,
                y: u(e) + 3,
                textAnchor: "end",
                fontSize: "8",
                fill: d.sub,
                children: [100 * e, "%"]
              })]
            }, e)), (0, s.jsx)("polygon", {
              points: x,
              fill: a,
              opacity: "0.15"
            }), (0, s.jsx)("polyline", {
              points: m,
              fill: "none",
              stroke: a,
              strokeWidth: "2",
              strokeLinejoin: "round"
            }), (0, s.jsx)("circle", {
              cx: p,
              cy: h,
              r: "4.5",
              fill: a,
              stroke: "#fff",
              strokeWidth: "2"
            }), (0, s.jsxs)("text", {
              x: n.l,
              y: 125,
              fontSize: "8",
              fill: d.sub,
              children: [o, " mo"]
            }), (0, s.jsxs)("text", {
              x: 320 - n.r,
              y: 125,
              textAnchor: "end",
              fontSize: "8",
              fill: d.sub,
              children: [i, " mo"]
            })
          ]
        })
      }

      function _() {
        let {
          track: e,
          lead: t
        } = function() {
          let e = (0, l.useRef)({});
          return (0, l.useEffect)(() => {
            var t, a, s, l, n, r;
            let o = new URLSearchParams(location.search),
              i = "";
            try {
              (i = localStorage.getItem("kinedu_session_id") || "") || (i = null !== (s = null === (t = (a = crypto).randomUUID) || void 0 === t ? void 0 : t.call(a)) && void 0 !== s ? s : String(Math.random()).slice(2), localStorage.setItem("kinedu_session_id", i))
            } catch (e) {
              i = null !== (r = null === (l = (n = crypto).randomUUID) || void 0 === l ? void 0 : l.call(n)) && void 0 !== r ? r : "s-".concat(Date.now(), "-").concat(Math.random().toString(36).slice(2))
            }
            let d = "qa" === o.get("env") || "webpromo.kinedu.com" !== location.hostname ? "qa" : "prod";
            e.current = {
              session_id: i,
              environment: d,
              test_id: (o.get("test_id") || "aq-assessment").slice(0, 80),
              variant: (o.get("v") || o.get("ui") || "assessment").slice(0, 20),
              utm_source: o.get("utm_source"),
              utm_medium: o.get("utm_medium"),
              utm_campaign: o.get("utm_campaign"),
              utm_content: o.get("utm_content"),
              utm_term: o.get("utm_term"),
              fbclid: o.get("fbclid"),
              gclid: o.get("gclid"),
              ttclid: o.get("ttclid"),
              landing_url: location.href,
              referrer: document.referrer || null
            }
          }, []), {
            track: (0, l.useCallback)((t, a) => {
              let s = e.current;
              s.session_id && fetch("/api/track", {
                method: "POST",
                keepalive: !0,
                headers: {
                  "Content-Type": "application/json"
                },
                body: JSON.stringify({
                  event_name: t,
                  screen: null != a ? a : null,
                  environment: s.environment,
                  language: "en",
                  test_id: s.test_id,
                  variant: s.variant,
                  session_id: s.session_id,
                  utm_source: s.utm_source,
                  utm_medium: s.utm_medium,
                  utm_campaign: s.utm_campaign,
                  utm_content: s.utm_content,
                  utm_term: s.utm_term,
                  fbclid: s.fbclid,
                  gclid: s.gclid,
                  ttclid: s.ttclid,
                  landing_url: s.landing_url,
                  referrer: s.referrer,
                  user_agent: navigator.userAgent
                })
              }).catch(() => {})
            }, []),
            lead: (0, l.useCallback)((t, a) => {
              let s = e.current;
              return fetch("/api/lead", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json"
                },
                body: JSON.stringify({
                  email: t,
                  name: a,
                  environment: s.environment,
                  language: "en",
                  test_id: s.test_id,
                  variant: s.variant,
                  session_id: s.session_id,
                  utm_source: s.utm_source,
                  utm_medium: s.utm_medium,
                  utm_campaign: s.utm_campaign,
                  landing_url: s.landing_url
                })
              })
            }, [])
          }
        }(), [a, n] = (0, l.useState)({
          s: "hero"
        }), [_, v] = (0, l.useState)("steps"), [j, w] = (0, l.useState)(!1);
        (0, l.useEffect)(() => {
          try {
            let e = new URLSearchParams(location.search),
              t = e.get("ui") || e.get("v");
            "list" === t && v("list"), "skills" === t && v("skills"), "0" === e.get("capture") && w(!0)
          } catch (e) {}
        }, []);
        let [, N] = (0, l.useState)(0), [k, C] = (0, l.useState)(""), [S, D] = (0, l.useState)(""), [F, A] = (0, l.useState)(!1), [E, q] = (0, l.useState)(34), [P, T] = (0, l.useState)(null), [M, z] = (0, l.useState)(!1), [L, O] = (0, l.useState)([]), [B, U] = (0, l.useState)([]), [W, K] = (0, l.useState)([]), R = (0, l.useRef)(new Map), [J, I] = (0, l.useState)(null), [Y, V] = (0, l.useState)([]), [G, H] = (0, l.useState)(null), [Q, $] = (0, l.useState)("all"), X = (0, l.useRef)(null), [Z, ee] = (0, l.useState)(!1), [et, ea] = (0, l.useState)(""), [es, el] = (0, l.useState)("");
        (0, l.useEffect)(() => {
          e("funnel_started", "assessment")
        }, []);
        let en = k.trim() || "your baby",
          er = (0, l.useMemo)(() => L.map((e, t) => {
            let a = [];
            return e.anchor && a.push(e.anchor), a.push(...e.items), t < B.length && a.push(B[t]), a
          }), [L, B]),
          eo = async () => {
            ee(!0), ea("");
            try {
              var t, a;
              let s = await fetch("/api/assessment", {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json"
                  },
                  body: JSON.stringify({
                    action: "start",
                    birthdate: S,
                    gestationalWeeks: F ? E : null
                  })
                }),
                l = await s.json();
              if (422 === s.status && (null == l ? void 0 : l.error) === "age_range") {
                n({
                  s: "age_range",
                  months: null !== (t = l.ageMonths) && void 0 !== t ? t : 49
                });
                return
              }
              if (!s.ok) {
                ea("Please check the birthdate.");
                return
              }
              T(l.ageMonths), z(l.corrected), O(l.sections), U(null !== (a = l.calibration) && void 0 !== a ? a : []), e("quiz_started", "child"), n({
                s: "area",
                idx: 0,
                q: 0
              })
            } catch (e) {
              ea("Connection hiccup — try again.")
            } finally {
              ee(!1)
            }
          }, ei = async t => {
            ee(!0);
            try {
              var a;
              let s = await fetch("/api/assessment", {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json"
                  },
                  body: JSON.stringify({
                    action: "result",
                    ageMonths: P,
                    extended: t,
                    answers: [...R.current.entries()].map(e => {
                      let [t, a] = e;
                      return {
                        id: t,
                        y: a
                      }
                    })
                  })
                }),
                l = await s.json();
              if ("extension" === l.stage && !t) {
                K(l.items), e("extension_started", "extension"), n({
                  s: "extension",
                  q: 0
                });
                return
              }
              I(l.basic), V(null !== (a = l.skills) && void 0 !== a ? a : []), e("funnel_completed", "celebrate"), n({
                s: "celebrate"
              })
            } catch (e) {
              ea("Connection hiccup — try again.")
            } finally {
              ee(!1)
            }
          }, ed = (0, l.useCallback)(() => {
            X.current && clearTimeout(X.current), X.current = setTimeout(async () => {
              try {
                let t = await fetch("/api/assessment", {
                    method: "POST",
                    headers: {
                      "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                      action: "result",
                      ageMonths: P,
                      extended: !0,
                      answers: [...R.current.entries()].map(e => {
                        let [t, a] = e;
                        return {
                          id: t,
                          y: a
                        }
                      })
                    })
                  }),
                  a = await t.json();
                if ("complete" === a.stage) {
                  var e;
                  I(a.basic), V(null !== (e = a.skills) && void 0 !== e ? e : [])
                }
              } catch (e) {}
            }, 800)
          }, [P]), ec = (e, t, a) => {
            R.current.set(e.id, t), a()
          };
        if ("hero" === a.s) return (0, s.jsxs)(h, {
          children: [(0, s.jsx)(b, {}), (0, s.jsxs)("div", {
            className: "my-auto text-center",
            children: [(0, s.jsx)("p", {
              className: "mb-3 text-sm font-bold uppercase tracking-wide",
              style: {
                color: d.blue
              },
              children: "Kinedu Assessment"
            }), (0, s.jsx)(y, {
              children: "See what your baby is building right now"
            }), (0, s.jsx)("p", {
              className: "mt-3 text-[15px] leading-relaxed",
              style: {
                color: d.sub
              },
              children: "Answer real questions from Kinedu’s developmental assessment — created and psychometrically evaluated by Kinedu with 2,135 caregivers — and see your baby’s developmental picture today."
            }), (0, s.jsxs)("div", {
              className: "mt-5 flex items-center justify-center gap-3 text-[13px]",
              style: {
                color: d.sub
              },
              children: [(0, s.jsx)("span", {
                children: "⏱ 5–10 min"
              }), (0, s.jsx)("span", {
                children: "\xb7"
              }), (0, s.jsx)("span", {
                children: "0–48 months"
              }), (0, s.jsx)("span", {
                children: "\xb7"
              }), (0, s.jsx)("span", {
                children: "Free reading"
              })]
            }), (0, s.jsxs)(g, {
              onClick: () => {
                e("quiz_answer", "hero"), n({
                  s: "primer",
                  n: 1
                })
              },
              children: ["Start ", k ? "for ".concat(k) : "", " →"]
            }), (0, s.jsx)("p", {
              className: "mt-4 text-xs",
              style: {
                color: d.sub
              },
              children: "Development surveillance, not diagnosis."
            })]
          })]
        });
        if ("primer" === a.s) {
          let e = a.n,
            t = e => m(e.replace("at {n} months", "at their exact age"), {
              name: "your baby"
            }),
            l = t(u("en", "primer".concat(e, "_title"))),
            r = t(u("en", "primer".concat(e, "_body")));
          return (0, s.jsxs)(h, {
            children: [(0, s.jsx)(b, {}), (0, s.jsxs)("div", {
              className: "my-auto",
              children: [(0, s.jsxs)("p", {
                className: "mb-2 text-xs font-bold",
                style: {
                  color: d.sub
                },
                children: [e, " / 3"]
              }), (0, s.jsx)(y, {
                children: l
              }), (0, s.jsx)("p", {
                className: "mt-3 text-[15px] leading-relaxed",
                style: {
                  color: d.sub
                },
                children: x(r)
              }), 1 === e && (0, s.jsx)("div", {
                className: "mt-4 space-y-3",
                children: ["primer1_yes", "primer1_not", "primer1_none"].map(e => (0, s.jsx)("div", {
                  className: "rounded-xl border p-3 text-[14px] leading-relaxed",
                  style: {
                    borderColor: d.line
                  },
                  children: x(u("en", e))
                }, e))
              }), 2 === e && (0, s.jsxs)("div", {
                className: "mt-4 space-y-3",
                children: [(0, s.jsx)("div", {
                  className: "rounded-xl border p-3 text-[14px] leading-relaxed",
                  style: {
                    borderColor: d.line
                  },
                  children: x(u("en", "primer2_half"))
                }), (0, s.jsx)("div", {
                  className: "rounded-xl border p-3 text-[14px] leading-relaxed",
                  style: {
                    borderColor: d.line
                  },
                  children: x(u("en", "primer2_older"))
                })]
              }), 3 === e && (0, s.jsx)("div", {
                className: "mt-4 rounded-xl border p-3 text-[14px] leading-relaxed",
                style: {
                  borderColor: d.line
                },
                children: x(u("en", "primer3_pace").replace(" You can save and come back.", ""))
              }), (0, s.jsx)(g, {
                onClick: () => e < 3 ? n({
                  s: "primer",
                  n: e + 1
                }) : n({
                  s: "child"
                }),
                children: e < 3 ? u("en", "primer_next") || "Next" : u("en", "primer_start") || "Start"
              })]
            })]
          })
        }
        if ("child" === a.s) {
          let e = new Date().toISOString().slice(0, 10);
          return (0, s.jsxs)(h, {
            children: [(0, s.jsx)(b, {}), (0, s.jsxs)("div", {
              className: "my-auto",
              children: [(0, s.jsx)(y, {
                children: "Tell us about your baby"
              }), (0, s.jsxs)("label", {
                className: "mt-5 block",
                children: [(0, s.jsx)("span", {
                  className: "text-[13px] font-bold",
                  style: {
                    color: d.sub
                  },
                  children: "Name"
                }), (0, s.jsx)("input", {
                  type: "text",
                  value: k,
                  onChange: e => C(e.target.value),
                  placeholder: "Mar\xeda",
                  className: "mt-1 w-full rounded-xl border bg-white px-4 py-3 text-[16px]",
                  style: {
                    borderColor: d.line
                  }
                })]
              }), (0, s.jsxs)("label", {
                className: "mt-4 block",
                children: [(0, s.jsx)("span", {
                  className: "text-[13px] font-bold",
                  style: {
                    color: d.sub
                  },
                  children: "Date of birth"
                }), (0, s.jsx)("input", {
                  type: "date",
                  value: S,
                  max: e,
                  onChange: e => D(e.target.value),
                  className: "mt-1 w-full rounded-xl border bg-white px-4 py-3 text-[16px]",
                  style: {
                    borderColor: d.line
                  }
                })]
              }), (0, s.jsxs)("label", {
                className: "mt-4 flex cursor-pointer items-center gap-2",
                children: [(0, s.jsx)("input", {
                  type: "checkbox",
                  checked: F,
                  onChange: e => A(e.target.checked),
                  className: "h-4 w-4"
                }), (0, s.jsx)("span", {
                  className: "text-[14px]",
                  style: {
                    color: d.sub
                  },
                  children: "Born before 37 weeks?"
                })]
              }), F && (0, s.jsxs)("label", {
                className: "mt-3 block",
                children: [(0, s.jsxs)("span", {
                  className: "text-[13px] font-bold",
                  style: {
                    color: d.sub
                  },
                  children: ["Weeks of gestation at birth: ", E]
                }), (0, s.jsx)("input", {
                  type: "range",
                  min: 24,
                  max: 36,
                  value: E,
                  onChange: e => q(Number(e.target.value)),
                  className: "mt-1 w-full"
                }), (0, s.jsx)("span", {
                  className: "text-xs",
                  style: {
                    color: d.sub
                  },
                  children: "We adjust the questions to corrected age (AAP), and we’ll say so."
                })]
              }), et && (0, s.jsx)("p", {
                className: "mt-3 text-sm font-semibold text-red-600",
                children: et
              }), (0, s.jsx)(g, {
                onClick: eo,
                disabled: Z || !S,
                children: Z ? "Preparing…" : "See ".concat(en, "’s questions →")
              })]
            })]
          })
        }
        if ("age_range" === a.s) return (0, s.jsxs)(h, {
          children: [(0, s.jsx)(b, {}), (0, s.jsxs)("div", {
            className: "my-auto text-center",
            children: [(0, s.jsx)("div", {
              className: "text-4xl",
              children: "\uD83C\uDF31"
            }), (0, s.jsx)(y, {
              children: "What a big kid!"
            }), (0, s.jsxs)("p", {
              className: "mt-3 text-[15px] leading-relaxed",
              style: {
                color: d.sub
              },
              children: ["This assessment is built and validated for ages 0 to 48 months, so we can’t give", " ", en, " a fair reading here. Kinedu still has classes and activities for the whole family."]
            }), (0, s.jsx)(g, {
              onClick: () => p(e),
              children: "Explore Kinedu →"
            })]
          })]
        });
        if ("area" === a.s || "extension" === a.s) {
          var eu, em, ex, ep, eh, eb, eg, ey, ef, e_;
          let t = "extension" === a.s,
            l = t ? W : null !== (em = er[a.idx]) && void 0 !== em ? em : [];
          if ("list" === _) {
            let r = t ? L.length : a.idx,
              c = t ? u("en", "deep_title") || "Deep dive" : null !== (eh = null === (ex = L[r]) || void 0 === ex ? void 0 : ex.area) && void 0 !== eh ? eh : "",
              m = null !== (eg = o[t ? null !== (eb = null === (ep = l[0]) || void 0 === ep ? void 0 : ep.area) && void 0 !== eb ? eb : "" : c]) && void 0 !== eg ? eg : d.blue,
              x = l.filter(e => R.current.has(e.id)).length,
              p = x === l.length && l.length > 0,
              b = !t && r + 1 < L.length ? L[r + 1].area : null;
            return (0, s.jsxs)(h, {
              children: [(0, s.jsx)("div", {
                className: "flex items-center justify-between",
                children: (0, s.jsxs)("span", {
                  className: "text-[15px] font-extrabold",
                  style: {
                    letterSpacing: "-0.02em"
                  },
                  children: ["Assessment ", k.trim() ? "for ".concat(k.trim()) : ""]
                })
              }), (0, s.jsx)("div", {
                className: "mt-3 flex gap-2",
                children: Array.from({
                  length: t ? L.length + 1 : L.length
                }).map((e, t) => (0, s.jsx)("div", {
                  className: "h-1.5 flex-1 overflow-hidden rounded-full",
                  style: {
                    background: d.line
                  },
                  children: (0, s.jsx)("div", {
                    className: "h-full rounded-full transition-all",
                    style: {
                      background: d.blue,
                      width: t < r ? "100%" : t === r ? "".concat(x / Math.max(l.length, 1) * 100, "%") : "0%"
                    }
                  })
                }, t))
              }), (0, s.jsxs)("div", {
                className: "mt-4 overflow-hidden rounded-2xl bg-white shadow-sm",
                style: {
                  borderTop: "4px solid ".concat(m)
                },
                children: [(0, s.jsxs)("div", {
                  className: "flex items-start justify-between px-4 pb-3 pt-4",
                  children: [(0, s.jsxs)("div", {
                    children: [(0, s.jsxs)("p", {
                      className: "text-[12px] font-bold uppercase tracking-wide",
                      style: {
                        color: m
                      },
                      children: [null !== (ey = i[c]) && void 0 !== ey ? ey : "✨", " ", t ? "Deep dive" : "Area ".concat(r + 1, " of ").concat(L.length)]
                    }), (0, s.jsx)("h2", {
                      className: "mt-0.5 text-[24px] font-extrabold",
                      style: {
                        letterSpacing: "-0.04em"
                      },
                      children: c
                    })]
                  }), (0, s.jsxs)("span", {
                    className: "text-[20px] font-extrabold tabular-nums",
                    style: {
                      color: m
                    },
                    children: [x, "/", l.length]
                  })]
                }), (0, s.jsx)("div", {
                  className: "divide-y",
                  style: {
                    borderColor: d.line
                  },
                  children: l.map(e => {
                    let t = R.current.get(e.id);
                    return (0, s.jsxs)("div", {
                      className: "flex items-center justify-between gap-3 px-4 py-3.5",
                      children: [(0, s.jsx)("p", {
                        className: "text-[15px] leading-snug",
                        children: e.title
                      }), (0, s.jsxs)("div", {
                        className: "flex shrink-0 gap-2",
                        children: [(0, s.jsx)("button", {
                          onClick: () => {
                            R.current.set(e.id, 0), N(e => e + 1)
                          },
                          className: "rounded-full border px-4 py-2 text-[13px] font-bold transition-colors",
                          style: 0 === t ? {
                            background: d.navy,
                            borderColor: d.navy,
                            color: "#fff"
                          } : {
                            background: "#fff",
                            borderColor: d.line,
                            color: d.text
                          },
                          children: u("en", "chip_not_yet") || "Not yet"
                        }), (0, s.jsx)("button", {
                          onClick: () => {
                            R.current.set(e.id, 1), N(e => e + 1)
                          },
                          className: "rounded-full border px-4 py-2 text-[13px] font-bold transition-colors",
                          style: 1 === t ? {
                            background: m,
                            borderColor: m,
                            color: "#fff"
                          } : {
                            background: "#fff",
                            borderColor: d.line,
                            color: d.text
                          },
                          children: u("en", "chip_yes") || "Yes"
                        })]
                      })]
                    }, e.id)
                  })
                }), (0, s.jsx)("div", {
                  className: "flex justify-end px-4 py-4",
                  children: (0, s.jsx)("button", {
                    onClick: () => {
                      if (p && !Z) {
                        if (t) {
                          ei(!0);
                          return
                        }
                        e("quiz_answer", "area_".concat(c)), b ? n({
                          s: "area",
                          idx: r + 1,
                          q: 0
                        }) : ei(!1)
                      }
                    },
                    disabled: !p || Z,
                    className: "rounded-2xl px-6 py-3.5 text-[16px] font-bold text-white transition-transform active:scale-[0.98] disabled:opacity-40",
                    style: {
                      background: d.green
                    },
                    children: Z ? "One sec…" : t || !b ? "See the results ›" : "Next: ".concat(b, " ›")
                  })
                })]
              }), (0, s.jsxs)("p", {
                className: "mt-3 text-center text-[12px]",
                style: {
                  color: d.sub
                },
                children: ["A “Not yet” is as useful as a “Yes.” Both tell us where ", en, " is."]
              })]
            })
          }
          let r = a.q,
            c = l[r];
          if (!c) return null;
          let m = t ? c.area : null !== (ef = null === (eu = L[a.idx]) || void 0 === eu ? void 0 : eu.area) && void 0 !== ef ? ef : c.area,
            x = null !== (e_ = o[m]) && void 0 !== e_ ? e_ : d.blue,
            p = () => {
              if (r + 1 < l.length) {
                n(t ? {
                  s: "extension",
                  q: r + 1
                } : {
                  s: "area",
                  idx: a.idx,
                  q: r + 1
                });
                return
              }
              if (t) {
                ei(!0);
                return
              }
              e("quiz_answer", "area_".concat(m));
              let s = a.idx + 1;
              s < L.length ? n({
                s: "area",
                idx: s,
                q: 0
              }) : ei(!1)
            };
          return (0, s.jsxs)(h, {
            children: [(0, s.jsxs)("div", {
              className: "flex items-center justify-between",
              children: [(0, s.jsxs)("span", {
                className: "text-[13px] font-bold",
                style: {
                  color: x
                },
                children: [i[m], " ", t ? u("en", "deep_title") : m]
              }), (0, s.jsxs)("span", {
                className: "text-[13px] font-bold tabular-nums",
                style: {
                  color: d.sub
                },
                children: [r + 1, "/", l.length]
              })]
            }), (0, s.jsx)("div", {
              className: "mt-2 h-1.5 w-full overflow-hidden rounded-full",
              style: {
                background: d.line
              },
              children: (0, s.jsx)("div", {
                className: "h-full rounded-full transition-all",
                style: {
                  width: "".concat((r + 1) / l.length * 100, "%"),
                  background: x
                }
              })
            }), t && 0 === r && (0, s.jsx)("p", {
              className: "mt-3 rounded-xl border p-3 text-[13px] leading-relaxed",
              style: {
                borderColor: d.line,
                color: d.sub
              },
              children: u("en", "deep_reading_complete")
            }), (0, s.jsxs)("div", {
              className: "my-auto",
              children: [(0, s.jsx)("p", {
                className: "text-[12px] font-bold uppercase tracking-wide",
                style: {
                  color: d.sub
                },
                children: c.skill
              }), (0, s.jsx)("h2", {
                className: "mt-2 text-[22px] font-extrabold leading-snug",
                style: {
                  letterSpacing: "-0.045em"
                },
                children: c.title
              }), (0, s.jsxs)("div", {
                className: "mt-8 grid grid-cols-2 gap-3",
                children: [(0, s.jsx)("button", {
                  onClick: () => ec(c, 0, p),
                  disabled: Z,
                  className: "rounded-2xl border-2 bg-white px-4 py-4 text-[17px] font-bold transition-transform active:scale-[0.97] disabled:opacity-40",
                  style: {
                    borderColor: d.line,
                    color: d.text
                  },
                  children: u("en", "chip_not_yet") || "Not yet"
                }), (0, s.jsx)("button", {
                  onClick: () => ec(c, 1, p),
                  disabled: Z,
                  className: "rounded-2xl px-4 py-4 text-[17px] font-bold text-white transition-transform active:scale-[0.97] disabled:opacity-60",
                  style: {
                    background: x
                  },
                  children: Z ? "One sec…" : u("en", "chip_yes") || "Yes"
                })]
              }), et && !Z && (0, s.jsxs)("div", {
                className: "mt-4 text-center",
                children: [(0, s.jsx)("p", {
                  className: "text-sm font-semibold text-red-600",
                  children: et
                }), (0, s.jsx)("button", {
                  onClick: () => {
                    ea(""), ei(t)
                  },
                  className: "mt-2 rounded-xl border px-4 py-2 text-[14px] font-bold",
                  style: {
                    borderColor: d.line,
                    color: d.text
                  },
                  children: "Try again"
                })]
              }), (0, s.jsxs)("p", {
                className: "mt-4 text-center text-[12px]",
                style: {
                  color: d.sub
                },
                children: ["A “Not yet” is as useful as a “Yes.” Both tell us where ", en, " is."]
              })]
            })]
          })
        }
        if ("celebrate" === a.s) return (0, s.jsxs)(h, {
          children: [(0, s.jsx)(b, {}), (0, s.jsxs)("div", {
            className: "my-auto text-center",
            children: [(0, s.jsx)("div", {
              className: "text-5xl",
              children: "\uD83C\uDF89"
            }), (0, s.jsx)(y, {
              children: u("en", "celebrate_title")
            }), (0, s.jsx)("p", {
              className: "mt-3 text-[15px] leading-relaxed",
              style: {
                color: d.sub
              },
              children: m(u("en", "celebrate_sub"), {
                name: en
              })
            }), (0, s.jsxs)(g, {
              onClick: () => n(j ? {
                s: "portrait"
              } : {
                s: "email"
              }),
              children: [u("en", "see_portrait"), " →"]
            })]
          })]
        });
        if ("email" === a.s) {
          let a = /^\S+@\S+\.\S+$/.test(es.trim());
          return (0, s.jsxs)(h, {
            children: [(0, s.jsx)(b, {}), (0, s.jsxs)("div", {
              className: "my-auto",
              children: [(0, s.jsxs)(y, {
                children: ["Where should we save ", en, "’s portrait?"]
              }), (0, s.jsx)("p", {
                className: "mt-3 text-[15px] leading-relaxed",
                style: {
                  color: d.sub
                },
                children: "We’ll keep the reading linked to your email so you can come back to it — and re-measure later, which is where the real story shows."
              }), (0, s.jsx)("input", {
                type: "email",
                value: es,
                onChange: e => el(e.target.value),
                placeholder: "you@example.com",
                className: "mt-5 w-full rounded-xl border bg-white px-4 py-3 text-[16px]",
                style: {
                  borderColor: d.line
                }
              }), (0, s.jsx)(g, {
                disabled: !a || Z,
                onClick: async () => {
                  ee(!0);
                  try {
                    await t(es.trim(), k.trim())
                  } catch (e) {}
                  try {
                    sessionStorage.setItem("kinedu_email", es.trim())
                  } catch (e) {}(0, r.iA)("Lead", {
                    content_category: "acquisition",
                    content_name: "assessment"
                  }), ee(!1), e("quiz_answer", "email_captured"), n({
                    s: "portrait"
                  })
                },
                children: Z ? "Saving…" : m(u("en", "see_results_btn"), {
                  name: en
                })
              })]
            })]
          })
        }
        if ("portrait" === a.s) {
          if (!J) return null;
          if ("below_floor" === J.state) return (0, s.jsxs)(h, {
            children: [(0, s.jsx)(b, {}), (0, s.jsxs)("div", {
              className: "my-auto",
              children: [(0, s.jsx)(y, {
                children: u("en", "floor_title")
              }), (0, s.jsx)("div", {
                className: "mt-4 space-y-3",
                children: (function(e, t) {
                  var a, s, l;
                  let n = null !== (l = null === (a = c.en) || void 0 === a ? void 0 : a[t]) && void 0 !== l ? l : null === (s = c.en) || void 0 === s ? void 0 : s[t];
                  return Array.isArray(n) ? n : []
                })(0, "floor_activities").map((e, t) => (0, s.jsx)("div", {
                  className: "rounded-xl border bg-white p-4 text-[15px] leading-relaxed",
                  style: {
                    borderColor: d.line
                  },
                  children: e
                }, t))
              }), (0, s.jsx)("p", {
                className: "mt-4 rounded-xl p-4 text-[14px] leading-relaxed",
                style: {
                  background: "#FFF6E9",
                  color: d.text
                },
                children: u("en", "floor_note")
              }), (0, s.jsxs)(g, {
                onClick: () => p(e),
                children: ["Get daily activities for ", en, " →"]
              }), (0, s.jsx)("p", {
                className: "mt-4 text-center text-xs",
                style: {
                  color: d.sub
                },
                children: "Development surveillance, not diagnosis."
              })]
            })]
          });
          if ("ok" !== J.state) return (0, s.jsxs)(h, {
            children: [(0, s.jsx)(b, {}), (0, s.jsxs)("div", {
              className: "my-auto text-center",
              children: [(0, s.jsx)(y, {
                children: u("en", "not_enough")
              }), (0, s.jsx)(g, {
                onClick: () => n({
                  s: "area",
                  idx: 0,
                  q: 0
                }),
                children: "Continue answering"
              })]
            })]
          });
          let t = J.devAge,
            a = m(u("en", "dev_detail_name"), {
              age: J.ageMonths,
              name: en,
              D: J.capped ? "".concat(t, "+") : t
            }),
            l = t / Math.max(J.ageMonths, 1);
          return (0, s.jsxs)(h, {
            children: [(0, s.jsx)(b, {}), (0, s.jsxs)("div", {
              className: "my-auto",
              children: [(0, s.jsx)("p", {
                className: "text-[13px] font-bold uppercase tracking-wide",
                style: {
                  color: d.blue
                },
                children: u("en", "picture_title")
              }), (0, s.jsx)(y, {
                children: function(e, t) {
                  var a;
                  let s = c.en._bands,
                    l = {
                      building: "ratio_low",
                      on_pace: "ratio_mid",
                      little_ahead: "ratio_high",
                      well_ahead: "ratio_top"
                    } [t];
                  return null !== (a = null == s ? void 0 : s[null != l ? l : ""]) && void 0 !== a ? a : ""
                }(0, J.band) || a
              }), (0, s.jsx)("p", {
                className: "mt-2 text-[15px] leading-relaxed",
                style: {
                  color: d.sub
                },
                children: a
              }), J.capped && (0, s.jsx)("p", {
                className: "mt-2 text-[13px] leading-relaxed",
                style: {
                  color: d.sub
                },
                children: u("en", "ceiling_note")
              }), (0, s.jsxs)("div", {
                className: "mt-6",
                children: [(0, s.jsxs)("div", {
                  className: "relative h-3 w-full rounded-full",
                  style: {
                    background: d.line
                  },
                  children: [(0, s.jsx)("div", {
                    className: "absolute inset-y-0 rounded-full opacity-40",
                    style: {
                      left: "28%",
                      right: "28%",
                      background: d.green
                    }
                  }), (0, s.jsx)("div", {
                    className: "absolute top-1/2 h-5 w-5 -translate-x-1/2 -translate-y-1/2 rounded-full border-4 border-white shadow",
                    style: {
                      left: "".concat(Math.max(6, Math.min(94, (l - .6) / .9 * 100)), "%"),
                      background: d.navy
                    }
                  })]
                }), (0, s.jsxs)("div", {
                  className: "mt-1 flex justify-between text-[11px]",
                  style: {
                    color: d.sub
                  },
                  children: [(0, s.jsx)("span", {
                    children: u("en", "band_axis_slower")
                  }), (0, s.jsx)("span", {
                    children: u("en", "band_axis_note")
                  }), (0, s.jsx)("span", {
                    children: u("en", "band_axis_faster")
                  })]
                })]
              }), "skills" === _ && Y.length > 0 ? (0, s.jsxs)(s.Fragment, {
                children: [(0, s.jsx)("p", {
                  className: "mt-7 text-[13px] font-bold uppercase tracking-wide",
                  style: {
                    color: d.blue
                  },
                  children: "Skills"
                }), (0, s.jsx)("div", {
                  className: "mt-2 flex flex-wrap gap-2",
                  children: ["all", ...Object.keys(o)].map(e => (0, s.jsx)("button", {
                    onClick: () => $(e),
                    className: "rounded-full border px-3 py-1.5 text-[13px] font-bold",
                    style: Q === e ? {
                      borderColor: d.blue,
                      color: d.blue,
                      background: "#EFF6FF"
                    } : {
                      borderColor: d.line,
                      color: d.text,
                      background: "#fff"
                    },
                    children: "all" === e ? "All areas" : e
                  }, e))
                }), (0, s.jsx)("div", {
                  className: "mt-3 space-y-2.5",
                  children: Y.filter(e => "all" === Q || e.area === Q).map(t => {
                    var a;
                    let l = null !== (a = o[t.area]) && void 0 !== a ? a : d.blue;
                    return (0, s.jsxs)("button", {
                      onClick: () => {
                        H(t.skill), e("quiz_answer", "skill_".concat(t.skill))
                      },
                      className: "block w-full rounded-2xl bg-white p-4 text-left shadow-sm transition-transform active:scale-[0.99]",
                      children: [(0, s.jsxs)("div", {
                        className: "flex items-center justify-between gap-2",
                        children: [(0, s.jsx)("span", {
                          className: "text-[16px] font-extrabold",
                          style: {
                            letterSpacing: "-0.03em"
                          },
                          children: t.skill
                        }), (0, s.jsxs)("span", {
                          className: "flex items-center gap-1.5",
                          children: [(0, s.jsxs)("span", {
                            className: "rounded-full px-2.5 py-1 text-[12px] font-bold",
                            style: t.focus ? {
                              background: "#FEF3C7",
                              color: "#92400E"
                            } : {
                              background: "#D1FAE5",
                              color: "#065F46"
                            },
                            children: [t.reached, " of ", t.total, t.focus ? " \xb7 focus" : ""]
                          }), (0, s.jsx)("span", {
                            style: {
                              color: d.sub
                            },
                            children: "›"
                          })]
                        })]
                      }), (0, s.jsx)("div", {
                        className: "mt-2.5 h-2 w-full overflow-hidden rounded-full",
                        style: {
                          background: d.line
                        },
                        children: (0, s.jsx)("div", {
                          className: "h-full rounded-full",
                          style: {
                            width: "".concat(100 * t.childPct, "%"),
                            background: l
                          }
                        })
                      })]
                    }, t.skill)
                  })
                }), G && (() => {
                  var t;
                  let a = Y.find(e => e.skill === G);
                  if (!a) return null;
                  let l = null !== (t = o[a.area]) && void 0 !== t ? t : d.blue;
                  return (0, s.jsx)("div", {
                    className: "fixed inset-0 z-50 flex items-end justify-center bg-black/40",
                    onClick: () => H(null),
                    children: (0, s.jsxs)("div", {
                      className: "max-h-[92vh] w-full max-w-md overflow-y-auto rounded-t-3xl bg-white p-5 pb-8",
                      onClick: e => e.stopPropagation(),
                      children: [(0, s.jsxs)("div", {
                        className: "flex items-start justify-between",
                        children: [(0, s.jsxs)("div", {
                          children: [(0, s.jsx)("h3", {
                            className: "text-[22px] font-extrabold",
                            style: {
                              color: l,
                              letterSpacing: "-0.04em"
                            },
                            children: a.skill
                          }), (0, s.jsxs)("p", {
                            className: "mt-1 text-[13px]",
                            style: {
                              color: d.sub
                            },
                            children: ["Actively building from ", a.from, " to ", a.to, " months", (0, s.jsx)("br", {}), a.reached, " of ", a.total, " reached \xb7 ", a.total, " milestones in the skill"]
                          })]
                        }), (0, s.jsx)("button", {
                          onClick: () => H(null),
                          className: "text-[14px] font-bold",
                          style: {
                            color: d.blue
                          },
                          children: "Close"
                        })]
                      }), (0, s.jsx)("p", {
                        className: "mt-4 text-[12px] font-bold uppercase tracking-wide",
                        style: {
                          color: d.blue
                        },
                        children: "How this skill is going"
                      }), (0, s.jsxs)("p", {
                        className: "mt-0.5 text-[13px]",
                        style: {
                          color: d.sub
                        },
                        children: ["Compared with children ", en, "’s age"]
                      }), (0, s.jsx)("div", {
                        className: "mt-2",
                        children: (0, s.jsx)(f, {
                          s: a,
                          color: l,
                          age: J.ageMonths
                        })
                      }), (0, s.jsxs)("p", {
                        className: "mt-2 text-[13px] leading-relaxed",
                        style: {
                          color: d.sub
                        },
                        children: ["How to read this: the line is the typical child, and the shaded band spans this skill’s milestones — from the earliest to the latest. The dot is ", en, ". Pace matters more than position."]
                      }), (0, s.jsx)("p", {
                        className: "mt-2 text-[13px] leading-relaxed",
                        style: {
                          color: d.sub
                        },
                        children: "Milestones marked “typical at their age” aren’t asked because nearly every child this age already does them — they are not gaps."
                      }), (0, s.jsx)("p", {
                        className: "mt-4 text-[12px] font-bold uppercase tracking-wide",
                        style: {
                          color: d.blue
                        },
                        children: "Milestones"
                      }), (0, s.jsx)("p", {
                        className: "mt-0.5 text-[13px]",
                        style: {
                          color: d.sub
                        },
                        children: "Mark what you already see at home — each answer sharpens the reading."
                      }), (0, s.jsx)("div", {
                        className: "mt-2 divide-y",
                        style: {
                          borderColor: d.line
                        },
                        children: a.items.map(e => {
                          let t = R.current.get(e.id),
                            a = t => {
                              R.current.set(e.id, t), N(e => e + 1), ed()
                            };
                          return (0, s.jsxs)("div", {
                            className: "flex items-center justify-between gap-2 py-3",
                            children: [(0, s.jsxs)("div", {
                              className: "min-w-0",
                              children: [(0, s.jsx)("p", {
                                className: "text-[14px] leading-snug",
                                children: e.title
                              }), "typical" === e.status && void 0 === t && (0, s.jsx)("span", {
                                className: "mt-1 inline-block rounded-full px-2 py-0.5 text-[11px] font-bold",
                                style: {
                                  background: "#D1FAE5",
                                  color: "#065F46"
                                },
                                children: "typical at their age"
                              })]
                            }), (0, s.jsxs)("div", {
                              className: "flex shrink-0 gap-1.5",
                              children: [(0, s.jsx)("button", {
                                onClick: () => a(1),
                                className: "rounded-full border px-3 py-1.5 text-[12px] font-bold",
                                style: 1 === t ? {
                                  background: l,
                                  borderColor: l,
                                  color: "#fff"
                                } : {
                                  background: "#fff",
                                  borderColor: d.line,
                                  color: d.text
                                },
                                children: "Yes"
                              }), (0, s.jsx)("button", {
                                onClick: () => a(0),
                                className: "rounded-full border px-3 py-1.5 text-[12px] font-bold",
                                style: 0 === t ? {
                                  background: d.navy,
                                  borderColor: d.navy,
                                  color: "#fff"
                                } : {
                                  background: "#fff",
                                  borderColor: d.line,
                                  color: d.text
                                },
                                children: "Not yet"
                              })]
                            })]
                          }, e.id)
                        })
                      }), (0, s.jsxs)("button", {
                        onClick: () => p(e),
                        className: "mt-4 w-full rounded-2xl px-6 py-4 text-[16px] font-bold text-white active:scale-[0.98]",
                        style: {
                          background: l
                        },
                        children: ["Activities that build ", a.skill, " →"]
                      }), (0, s.jsxs)("p", {
                        className: "mt-2 text-center text-[12px]",
                        style: {
                          color: d.sub
                        },
                        children: ["Kinedu’s daily plan turns this reading into play — activities picked for", " ", en, ", updated as they grow."]
                      })]
                    })
                  })
                })()]
              }) : (0, s.jsxs)(s.Fragment, {
                children: [(0, s.jsx)("p", {
                  className: "mt-7 text-[13px] font-bold uppercase tracking-wide",
                  style: {
                    color: d.sub
                  },
                  children: u("en", "areas_title")
                }), (0, s.jsx)("div", {
                  className: "mt-2 space-y-2",
                  children: Object.keys(o).map(e => (0, s.jsxs)("div", {
                    className: "flex items-center justify-between rounded-xl border bg-white px-4 py-3",
                    style: {
                      borderColor: d.line
                    },
                    children: [(0, s.jsxs)("span", {
                      className: "text-[15px] font-bold",
                      style: {
                        color: o[e]
                      },
                      children: [i[e], " ", e]
                    }), (0, s.jsx)("span", {
                      className: "select-none text-[15px] font-bold blur-sm",
                      style: {
                        color: d.sub
                      },
                      children: "●● months"
                    })]
                  }, e))
                }), J.teaserArea && (0, s.jsxs)("p", {
                  className: "mt-3 text-[14px] leading-relaxed",
                  style: {
                    color: d.text
                  },
                  children: ["✨ ", m(u("en", "teaser"), {
                    name: J.teaserArea
                  })]
                })]
              }), "skills" === _ ? (0, s.jsxs)("div", {
                className: "mt-7 rounded-2xl p-5",
                style: {
                  background: "#EAF4FF"
                },
                children: [(0, s.jsx)("p", {
                  className: "text-[18px] font-extrabold",
                  style: {
                    letterSpacing: "-0.03em"
                  },
                  children: "Play with purpose \uD83C\uDFAF"
                }), (0, s.jsxs)("p", {
                  className: "mt-1.5 text-[14px] leading-relaxed",
                  style: {
                    color: d.text
                  },
                  children: ["This is where ", en, " is today. Kinedu turns this exact reading into daily activities — picked for ", en, ", skill by skill, and updated as they grow. You’ll know exactly what to do, every day."]
                })]
              }) : (0, s.jsxs)(g, {
                color: d.green,
                onClick: () => p(e),
                children: ["Unlock ", en, "’s full profile →"]
              }), (0, s.jsx)("p", {
                className: "mt-3 text-center text-[13px] leading-relaxed",
                style: {
                  color: d.sub
                },
                children: u("en", "reassure")
              }), (0, s.jsx)("p", {
                className: "mt-4 text-center text-xs",
                style: {
                  color: d.sub
                },
                children: "Development surveillance, not diagnosis."
              }), "skills" === _ && (0, s.jsx)("div", {
                className: "h-24"
              })]
            }), "skills" === _ && !G && (0, s.jsx)("div", {
              className: "fixed inset-x-0 bottom-0 z-40",
              children: (0, s.jsxs)("div", {
                className: "mx-auto w-full max-w-md px-5 pb-4 pt-8",
                style: {
                  background: "linear-gradient(180deg, transparent, #FFFDF9 40%)"
                },
                children: [(0, s.jsxs)("p", {
                  className: "mb-1.5 text-center text-[12px] font-semibold",
                  style: {
                    color: d.sub
                  },
                  children: ["This is ", en, " today — here’s how to help them grow."]
                }), (0, s.jsxs)("button", {
                  onClick: () => p(e),
                  className: "w-full rounded-2xl px-6 py-4 text-[17px] font-bold text-white shadow-lg transition-transform active:scale-[0.98]",
                  style: {
                    background: d.green
                  },
                  children: ["Get ", en, "’s daily plan →"]
                })]
              })
            })]
          })
        }
        return null
      }
      var v = a(5668),
        j = a(7578);
      a(8487), a(1121);
      let w = {
          Physical: "#32AFE0",
          Cognitive: "#3EB646",
          Language: "#F99848",
          "Social-Emotional": "#D1296D"
        },
        N = {
          Physical: {
            bg: "#F1FAFE",
            border: "#BFE4F6"
          },
          Cognitive: {
            bg: "#F2FAF2",
            border: "#C9E9CB"
          },
          Language: {
            bg: "#FFF8EF",
            border: "#FBDFBC"
          },
          "Social-Emotional": {
            bg: "#FDF1F6",
            border: "#F3C6D8"
          }
        },
        k = {
          Physical: "/aq-classic/physical.png",
          Cognitive: "/aq-classic/cognitive.png",
          Language: "/aq-classic/language.png",
          "Social-Emotional": "/aq-classic/social-emotional.png"
        },
        C = {
          brand: "#0086D8",
          paper: "#FAF9F6",
          ink: "#23303E",
          sub: "#5F6B78",
          faint: "#98A1AC",
          line: "#ECE8DF",
          cta: "#75B753",
          zone: "rgba(138, 210, 143, .45)"
        },
        S = n.FB;

      function D() {
        try {
          let e = (new URLSearchParams(location.search).get("lang") || "").toLowerCase();
          if (e.startsWith("es")) return "es";
          if (e.startsWith("pt")) return "pt"
        } catch (e) {}
        return "en"
      }

      function F(e, t) {
        var a, s;
        return "es" === t ? null !== (a = v[String(e.id)]) && void 0 !== a ? a : e.title : "pt" === t && null !== (s = j[String(e.id)]) && void 0 !== s ? s : e.title
      }
      let A = {
          en: {
            Physical: "Physical",
            Cognitive: "Cognitive",
            Language: "Language",
            "Social-Emotional": "Social-Emotional"
          },
          es: {
            Physical: "F\xedsica",
            Cognitive: "Cognitiva",
            Language: "Lenguaje",
            "Social-Emotional": "Socioemocional"
          },
          pt: {
            Physical: "F\xedsica",
            Cognitive: "Cognitiva",
            Language: "Linguagem",
            "Social-Emotional": "Socioemocional"
          }
        },
        E = function(e, t) {
          var a;
          let s = arguments.length > 2 && void 0 !== arguments[2] && arguments[2],
            l = null !== (a = A[t][e]) && void 0 !== a ? a : e;
          return s && "Social-Emotional" === e ? "en" === t ? "Social-Emot." : "Socioemoc." : l
        },
        q = {
          en: {
            hero_h1: "See what your baby is building right now",
            hero_sub: "Answer about what they do today and see which skills are opening up — compared to what’s typical at their exact age.",
            hero_cta: "Start FREE assessment →",
            trust_time: "⏱ 5–10 minutes",
            trust_card: "\uD83D\uDD12 No credit card",
            trust_report: "\uD83D\uDCC4 Free reading included",
            preview_eyebrow: "You’ll get a reading like this",
            preview_line: "“At 6 months, showing the skills of a typical",
            preview_line2: ".”",
            preview_months: "months",
            at_least20: "around 8",
            around16: "around 7",
            around12: "around 6",
            around18: "around 7",
            band_zone: "The green zone is what we usually see at this age.",
            sample_note: "Example — not a real child’s result.",
            honest: "\uD83C\uDF31 **About half the answers will be “Not yet” — and that’s fine.** We ask right at the edge of what your baby is building: that’s what real measurement looks like.",
            science: "Created and psychometrically evaluated by Kinedu with 2,135 caregivers. Michael C. Frank, of Stanford, advised on the early review of the 0–24 month milestones.",
            disclaimer: "Development surveillance, not diagnosis.",
            primer_title: "Before we start",
            primer_sub: "30 seconds that make the measurement better",
            primer_q_title: "Questions picked for their exact age",
            primer_q_body: "A 5-month-old and a 7-month-old don’t see the same list.",
            primer_two: "There are only two answers",
            primer_half_title: "About half will be “Not yet” — and that’s fine",
            primer_cta: "Start the questions →",
            child_title: "Tell us about your baby",
            name_label: "Name",
            optional: "(optional)",
            name_ph: "E.g., Emma",
            dob_label: "Date of birth",
            preterm_q: "Born before 37 weeks?",
            weeks_label: "Weeks of gestation",
            aap_note: "We’ll use their corrected age, as the American Academy of Pediatrics recommends, until age 2 — and we’ll say so.",
            check_date: "Please check the birthdate.",
            conn_error: "Connection hiccup — try again.",
            preparing: "Preparing…",
            see_questions: "See {name}’s questions →",
            over48_title: "What a big kid",
            over48_body: "This assessment is built and validated for ages 0 to 48 months, so we can’t give {name} a fair reading here. Kinedu still has activity plans and expert content for the whole family.",
            over48_cta: "Explore Kinedu →",
            assessment_for: "Assessment for {name}",
            assessment_plain: "Assessment",
            area_of: "Area {i} of {n}",
            going_further: "Going further",
            ext_note: "{name} passed everything we asked. These run a bit ahead of their age, to see just how far along they are.",
            back: "‹ Back",
            next_prefix: "Next:",
            see_reading: "See {name}’s reading →",
            your_baby: "your baby",
            your_baby_cap: "Your baby",
            email_eyebrow: "Their full reading, to your inbox",
            email_title: "Where should we save {name}’s reading?",
            email_sub: "We’ll keep it linked to your email so you can come back — and re-measure later, which is where the real story shows.",
            email_ph: "you@email.com",
            email_btn: "Save it",
            ready: "{name}’s reading is ready!",
            ready_generic: "The reading is ready!",
            is_showing: "is {age} months old, showing the skills of",
            at_least_conn: "at least",
            a_typical: "a typical",
            month_old: "-month-old",
            zone_at: "The green zone is what we usually see at {age} months. The dot is their reading.",
            born_at: "Born at {weeks} weeks, so this reading uses their corrected age (AAP).",
            born_at_flow: "Born at {weeks} weeks, so we use their corrected age (AAP).",
            see_breakdown: "See the area breakdown ▾",
            one_process: "In the first year, areas mostly move as one process.",
            more_needed: "more answers needed",
            few_more: "a few more and we’ll tell you",
            around_lbl: "around",
            at_least_lbl: "at least",
            months_lbl: "months",
            passed_all: "passed everything we asked",
            strongest_today: "their strongest area today",
            activities_eyebrow: "Activities to focus on now",
            get_activities: "Get daily activities for {name} →",
            continue_answering: "Continue answering",
            sticky_cta: "Start {name}’s plan — 7 days free",
            sticky_your: "your baby",
            sticky_note: "No commitment \xb7 the plan turns this into daily activities",
            month: "Month",
            day: "Day",
            year: "Year",
            done_title: "All done!",
            done_sub: "We compared what you told us about {name} against what’s typical at their exact age. Their reading is ready.",
            done_answers: "{n} answers",
            done_areas: "4 areas",
            email_b1: "Come back to their reading anytime",
            email_b2: "We’ll tell you when it’s time to re-measure",
            email_micro: "No spam — just their development.",
            opening_eyebrow: "What’s opening up for {name} right now",
            opening_more: "+{n} more in the full profile",
            locked_hint: "Tap to unlock",
            unlock_cta: "Unlock {name}’s full profile + daily activities →",
            unlock_note: "7 days free \xb7 no commitment",
            retro_note: "Their answers are already saved — it opens instantly.",
            picked_for: "Chosen for {name} at {age} months",
            reading_done: "This reading is already complete — unlocking adds depth by area, it doesn’t change the number.",
            gift_eyebrow: "A free activity for today",
            gift_line: "Chosen at {name}’s level in {area}",
            gift_locked: "The daily plan of 3 + the Top 10 are waiting in the app",
            email_b3: "The Kinedu parents’ guide (PDF), as a gift",
            every_pace: "Every child develops at their own pace. This helps you understand their unique journey — not compare them to others."
          },
          es: {
            hero_h1: "Mira lo que tu beb\xe9 est\xe1 construyendo ahora",
            hero_sub: "Responde sobre lo que hace hoy y descubre las habilidades que se est\xe1n abriendo — comparado con lo t\xedpico a su edad exacta.",
            hero_cta: "Empezar evaluaci\xf3n GRATIS →",
            trust_time: "⏱ 5–10 minutos",
            trust_card: "\uD83D\uDD12 Sin tarjeta",
            trust_report: "\uD83D\uDCC4 Lectura gratis incluida",
            preview_eyebrow: "Recibir\xe1s una lectura como esta",
            preview_line: "“Tiene 6 meses y muestra las habilidades de una ni\xf1a t\xedpica de",
            preview_line2: ".”",
            preview_months: "meses",
            at_least20: "alrededor de 8",
            around16: "alrededor de 7",
            around12: "alrededor de 6",
            around18: "alrededor de 7",
            band_zone: "La zona verde es lo usual a su edad.",
            sample_note: "Ejemplo — no es el resultado de un ni\xf1o real.",
            honest: "\uD83C\uDF31 **La mitad de las respuestas ser\xe1n “A\xfan no” — y est\xe1 bien.** Preguntamos justo al borde de lo que tu beb\xe9 est\xe1 construyendo: as\xed es como se mide de verdad.",
            science: "Creado y evaluado psicom\xe9tricamente por Kinedu con 2,135 cuidadores hispanohablantes. Michael C. Frank, de Stanford, asesor\xf3 en la revisi\xf3n temprana de los hitos de 0 a 24 meses.",
            disclaimer: "Seguimiento del desarrollo, no diagn\xf3stico.",
            primer_title: "Antes de empezar",
            primer_sub: "30 segundos que hacen mejor la medici\xf3n",
            primer_q_title: "Preguntas elegidas para su edad exacta",
            primer_q_body: "Un beb\xe9 de 5 meses y uno de 7 no ven la misma lista.",
            primer_two: "Solo hay dos respuestas",
            primer_half_title: "La mitad ser\xe1n “A\xfan no” — y est\xe1 bien",
            primer_cta: "Empezar las preguntas →",
            child_title: "Cu\xe9ntanos de tu beb\xe9",
            name_label: "Nombre",
            optional: "(opcional)",
            name_ph: "Ej., Emma",
            dob_label: "Fecha de nacimiento",
            preterm_q: "\xbfNaci\xf3 antes de las 37 semanas?",
            weeks_label: "Semanas de gestaci\xf3n",
            aap_note: "Usaremos su edad corregida, como recomienda la Academia Americana de Pediatr\xeda, hasta los 2 a\xf1os — y te lo diremos.",
            check_date: "Revisa la fecha de nacimiento.",
            conn_error: "Fall\xf3 la conexi\xf3n — intenta de nuevo.",
            preparing: "Preparando…",
            see_questions: "Ver las preguntas de {name} →",
            over48_title: "Qu\xe9 grande est\xe1",
            over48_body: "Esta evaluaci\xf3n est\xe1 construida y validada para 0 a 48 meses, as\xed que no podemos darle a {name} una lectura justa aqu\xed. Kinedu tiene planes de actividades y contenido de expertos para toda la familia.",
            over48_cta: "Conocer Kinedu →",
            assessment_for: "Evaluaci\xf3n de {name}",
            assessment_plain: "Evaluaci\xf3n",
            area_of: "\xc1rea {i} de {n}",
            going_further: "Yendo m\xe1s lejos",
            ext_note: "{name} pas\xf3 todo lo que preguntamos. Estas van un poco adelante de su edad, para ver qu\xe9 tan lejos llega.",
            back: "‹ Atr\xe1s",
            next_prefix: "Siguiente:",
            see_reading: "Ver la lectura de {name} →",
            your_baby: "tu beb\xe9",
            your_baby_cap: "Tu beb\xe9",
            email_eyebrow: "Su lectura completa, a tu correo",
            email_title: "\xbfD\xf3nde guardamos la lectura de {name}?",
            email_sub: "La dejamos ligada a tu correo para que puedas volver — y medir de nuevo despu\xe9s, que es donde se ve la historia real.",
            email_ph: "tu@correo.com",
            email_btn: "Guardar",
            ready: "\xa1La lectura de {name} est\xe1 lista!",
            ready_generic: "\xa1La lectura est\xe1 lista!",
            is_showing: "tiene {age} meses y muestra las habilidades de",
            at_least_conn: "al menos",
            a_typical: "un ni\xf1o t\xedpico de",
            month_old: " meses",
            zone_at: "La zona verde es lo que solemos ver a los {age} meses. El punto es su lectura.",
            born_at: "Como naci\xf3 a las {weeks} semanas, esta lectura usa su edad corregida (AAP).",
            born_at_flow: "Como naci\xf3 a las {weeks} semanas, usamos su edad corregida (AAP).",
            see_breakdown: "Ver el desglose por \xe1rea ▾",
            one_process: "En el primer a\xf1o, las \xe1reas se mueven casi como un solo proceso.",
            more_needed: "faltan respuestas",
            few_more: "unas preguntas m\xe1s y te decimos",
            around_lbl: "alrededor de",
            at_least_lbl: "al menos",
            months_lbl: "meses",
            passed_all: "pas\xf3 todo lo que preguntamos",
            strongest_today: "su \xe1rea m\xe1s fuerte hoy",
            activities_eyebrow: "Actividades para enfocarse ahora",
            get_activities: "Actividades diarias para {name} →",
            continue_answering: "Seguir contestando",
            sticky_cta: "Empieza el plan de {name} — 7 d\xedas gratis",
            sticky_your: "tu beb\xe9",
            sticky_note: "Sin compromiso \xb7 el plan convierte esto en actividades diarias",
            month: "Mes",
            day: "D\xeda",
            year: "A\xf1o",
            done_title: "\xa1Terminaste!",
            done_sub: "Comparamos lo que nos contaste de {name} contra lo t\xedpico de su edad exacta. Su lectura est\xe1 lista.",
            done_answers: "{n} respuestas",
            done_areas: "4 \xe1reas",
            email_b1: "Vuelve a su lectura cuando quieras",
            email_b2: "Te avisamos cuando toque medir de nuevo",
            email_micro: "Sin spam — solo su desarrollo.",
            opening_eyebrow: "Lo que se est\xe1 abriendo para {name} ahora",
            opening_more: "+{n} m\xe1s en el perfil completo",
            locked_hint: "Toca para desbloquear",
            unlock_cta: "Desbloquear el perfil completo de {name} + actividades diarias →",
            unlock_note: "7 d\xedas gratis \xb7 sin compromiso",
            retro_note: "Sus respuestas ya est\xe1n guardadas — se abre al instante.",
            picked_for: "Elegidas para los {age} meses de {name}",
            reading_done: "Su lectura ya est\xe1 completa — desbloquear agrega el detalle por \xe1rea, no cambia el n\xfamero.",
            gift_eyebrow: "Una actividad de regalo para hoy",
            gift_line: "Elegida al nivel de {name} en {area}",
            gift_locked: "El plan diario de 3 + el Top 10 te esperan en el app",
            email_b3: "La gu\xeda para padres de Kinedu (PDF), de regalo",
            every_pace: "Cada ni\xf1o se desarrolla a su propio ritmo. Esto te ayuda a entender su camino \xfanico — no a compararlo con otros."
          },
          pt: {
            hero_h1: "Veja o que seu beb\xea est\xe1 construindo agora",
            hero_sub: "Responda sobre o que ele faz hoje e descubra as habilidades que est\xe3o se abrindo — comparado com o t\xedpico na idade exata dele.",
            hero_cta: "Come\xe7ar avalia\xe7\xe3o GR\xc1TIS →",
            trust_time: "⏱ 5–10 minutos",
            trust_card: "\uD83D\uDD12 Sem cart\xe3o",
            trust_report: "\uD83D\uDCC4 Leitura gr\xe1tis inclu\xedda",
            preview_eyebrow: "Voc\xea receber\xe1 uma leitura como esta",
            preview_line: "“Tem 6 meses e mostra as habilidades de uma crian\xe7a t\xedpica de",
            preview_line2: ".”",
            preview_months: "meses",
            at_least20: "cerca de 8",
            around16: "cerca de 7",
            around12: "cerca de 6",
            around18: "cerca de 7",
            band_zone: "A zona verde \xe9 o usual nessa idade.",
            sample_note: "Exemplo — n\xe3o \xe9 o resultado de uma crian\xe7a real.",
            honest: "\uD83C\uDF31 **Metade das respostas ser\xe1 “Ainda n\xe3o” — e est\xe1 tudo bem.** Perguntamos bem na fronteira do que seu beb\xea est\xe1 construindo: \xe9 assim que se mede de verdade.",
            science: "Criado e avaliado psicometricamente pela Kinedu com 2.135 cuidadores hispanofalantes. Michael C. Frank, de Stanford, assessorou a revis\xe3o inicial dos marcos de 0 a 24 meses.",
            disclaimer: "Acompanhamento do desenvolvimento, n\xe3o diagn\xf3stico.",
            primer_title: "Antes de come\xe7ar",
            primer_sub: "30 segundos que melhoram a medi\xe7\xe3o",
            primer_q_title: "Perguntas escolhidas para a idade exata",
            primer_q_body: "Um beb\xea de 5 meses e um de 7 n\xe3o veem a mesma lista.",
            primer_two: "S\xf3 existem duas respostas",
            primer_half_title: "Metade ser\xe1 “Ainda n\xe3o” — e est\xe1 tudo bem",
            primer_cta: "Come\xe7ar as perguntas →",
            child_title: "Conte sobre seu beb\xea",
            name_label: "Nome",
            optional: "(opcional)",
            name_ph: "Ex., Emma",
            dob_label: "Data de nascimento",
            preterm_q: "Nasceu antes das 37 semanas?",
            weeks_label: "Semanas de gesta\xe7\xe3o",
            aap_note: "Usaremos a idade corrigida, como recomenda a Academia Americana de Pediatria, at\xe9 os 2 anos — e avisaremos.",
            check_date: "Confira a data de nascimento.",
            conn_error: "A conex\xe3o falhou — tente de novo.",
            preparing: "Preparando…",
            see_questions: "Ver as perguntas de {name} →",
            over48_title: "Como est\xe1 grande",
            over48_body: "Esta avalia\xe7\xe3o \xe9 constru\xedda e validada para 0 a 48 meses, ent\xe3o n\xe3o podemos dar a {name} uma leitura justa aqui. A Kinedu tem planos de atividades e conte\xfado de especialistas para toda a fam\xedlia.",
            over48_cta: "Conhecer a Kinedu →",
            assessment_for: "Avalia\xe7\xe3o de {name}",
            assessment_plain: "Avalia\xe7\xe3o",
            area_of: "\xc1rea {i} de {n}",
            going_further: "Indo mais longe",
            ext_note: "{name} passou em tudo o que perguntamos. Estas v\xe3o um pouco al\xe9m da idade, para ver at\xe9 onde chega.",
            back: "‹ Voltar",
            next_prefix: "Pr\xf3xima:",
            see_reading: "Ver a leitura de {name} →",
            your_baby: "seu beb\xea",
            your_baby_cap: "Seu beb\xea",
            email_eyebrow: "A leitura completa, no seu e-mail",
            email_title: "Onde guardamos a leitura de {name}?",
            email_sub: "Deixamos ligada ao seu e-mail para voc\xea voltar — e medir de novo depois, que \xe9 onde a hist\xf3ria real aparece.",
            email_ph: "voce@email.com",
            email_btn: "Salvar",
            ready: "A leitura de {name} est\xe1 pronta!",
            ready_generic: "A leitura est\xe1 pronta!",
            is_showing: "tem {age} meses e mostra as habilidades de",
            at_least_conn: "pelo menos",
            a_typical: "uma crian\xe7a t\xedpica de",
            month_old: " meses",
            zone_at: "A zona verde \xe9 o que costumamos ver aos {age} meses. O ponto \xe9 a leitura.",
            born_at: "Como nasceu com {weeks} semanas, esta leitura usa a idade corrigida (AAP).",
            born_at_flow: "Como nasceu com {weeks} semanas, usamos a idade corrigida (AAP).",
            see_breakdown: "Ver o detalhe por \xe1rea ▾",
            one_process: "No primeiro ano, as \xe1reas se movem quase como um \xfanico processo.",
            more_needed: "faltam respostas",
            few_more: "mais algumas e te contamos",
            around_lbl: "cerca de",
            at_least_lbl: "pelo menos",
            months_lbl: "meses",
            passed_all: "passou em tudo o que perguntamos",
            strongest_today: "a \xe1rea mais forte hoje",
            activities_eyebrow: "Atividades para focar agora",
            get_activities: "Atividades di\xe1rias para {name} →",
            continue_answering: "Continuar respondendo",
            sticky_cta: "Comece o plano de {name} — 7 dias gr\xe1tis",
            sticky_your: "seu beb\xea",
            sticky_note: "Sem compromisso \xb7 o plano transforma isto em atividades di\xe1rias",
            month: "M\xeas",
            day: "Dia",
            year: "Ano",
            done_title: "Pronto!",
            done_sub: "Comparamos o que voc\xea nos contou sobre {name} com o t\xedpico na idade exata. A leitura est\xe1 pronta.",
            done_answers: "{n} respostas",
            done_areas: "4 \xe1reas",
            email_b1: "Volte \xe0 leitura quando quiser",
            email_b2: "Avisamos quando for hora de medir de novo",
            email_micro: "Sem spam — s\xf3 o desenvolvimento.",
            opening_eyebrow: "O que est\xe1 se abrindo para {name} agora",
            opening_more: "+{n} mais no perfil completo",
            locked_hint: "Toque para desbloquear",
            unlock_cta: "Desbloquear o perfil completo de {name} + atividades di\xe1rias →",
            unlock_note: "7 dias gr\xe1tis \xb7 sem compromisso",
            retro_note: "As respostas j\xe1 est\xe3o guardadas — abre na hora.",
            picked_for: "Escolhidas para os {age} meses de {name}",
            reading_done: "A leitura j\xe1 est\xe1 completa — desbloquear adiciona o detalhe por \xe1rea, n\xe3o muda o n\xfamero.",
            gift_eyebrow: "Uma atividade de presente para hoje",
            gift_line: "Escolhida no n\xedvel de {name} em {area}",
            gift_locked: "O plano di\xe1rio de 3 + o Top 10 esperam por voc\xea no app",
            email_b3: "O guia para pais da Kinedu (PDF), de presente",
            every_pace: "Cada crian\xe7a se desenvolve no seu pr\xf3prio ritmo. Isto ajuda voc\xea a entender o caminho \xfanico dela — n\xe3o a compar\xe1-la com outras."
          }
        },
        P = {
          en: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
          es: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
          pt: ["Janeiro", "Fevereiro", "Mar\xe7o", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        },
        T = (e, t, a) => {
          var s, l;
          let n = null !== (l = null !== (s = q[e][t]) && void 0 !== s ? s : q.en[t]) && void 0 !== l ? l : "";
          return a ? z(n, a) : n
        };

      function M(e, t) {
        var a, s, l;
        let n = null !== (l = null === (a = S[e]) || void 0 === a ? void 0 : a[t]) && void 0 !== l ? l : null === (s = S.en) || void 0 === s ? void 0 : s[t];
        return "string" == typeof n ? n : ""
      }

      function z(e, t) {
        return e.replace(/\{(\w+)\}/g, (e, a) => {
          var s;
          return String(null !== (s = t[a]) && void 0 !== s ? s : "")
        })
      }

      function L(e) {
        let t = e.split(/\*\*(.+?)\*\*/g);
        return (0, s.jsx)(s.Fragment, {
          children: t.map((e, t) => t % 2 ? (0, s.jsx)("strong", {
            children: e
          }, t) : (0, s.jsx)("span", {
            children: e
          }, t))
        })
      }

      function O(e, t) {
        var a;
        let s = S[e]._bands,
          l = {
            building: "ratio_low",
            on_pace: "ratio_mid",
            little_ahead: "ratio_high",
            well_ahead: "ratio_top"
          } [t];
        return null !== (a = null == s ? void 0 : s[null != l ? l : ""]) && void 0 !== a ? a : ""
      }
      let B = e => Math.max(2, Math.min(98, (e - .7) / .6 * 100));

      function U(e) {
        e("quiz_answer", "paywall_handoff"), (0, r.iA)("InitiateCheckout", {
          content_category: "acquisition",
          content_name: "assessment-classic"
        }), location.href = function() {
          let e;
          try {
            e = new URLSearchParams(location.search)
          } catch (t) {
            e = new URLSearchParams
          }
          let t = (e.get("paywall") || "").trim();
          /^[a-z0-9][a-z0-9-]{0,31}$/.test(t) || (t = "trial3"), e.set("from", "assessment");
          let a = e.toString();
          return "/aq-paywall-".concat(t, "/index.html").concat(a ? "?".concat(a) : "")
        }()
      }

      function W(e) {
        let {
          children: t
        } = e;
        return (0, s.jsxs)("div", {
          className: "min-h-screen",
          style: {
            background: C.paper,
            color: C.ink,
            fontFamily: "'Plus Jakarta Sans', -apple-system, sans-serif"
          },
          children: [(0, s.jsx)("style", {
            children: "html, body { background: ".concat(C.paper, " !important; }")
          }), (0, s.jsx)("link", {
            href: "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap",
            rel: "stylesheet"
          }), (0, s.jsx)("div", {
            className: "mx-auto flex min-h-screen w-full max-w-md flex-col px-4 pb-10 pt-5",
            children: t
          })]
        })
      }

      function K() {
        return (0, s.jsx)("img", {
          src: "/aq-classic/kinedu.png",
          alt: "Kinedu",
          className: "mx-auto mb-3 h-7 w-auto"
        })
      }

      function R(e) {
        let {
          lang: t
        } = e;
        return (0, s.jsx)("p", {
          className: "mt-4 pb-2 text-center text-[11px]",
          style: {
            color: C.faint
          },
          children: T(t, "disclaimer")
        })
      }

      function J(e) {
        let {
          onClick: t,
          children: a,
          disabled: l,
          color: n = C.cta
        } = e;
        return (0, s.jsx)("button", {
          onClick: t,
          disabled: l,
          className: "mt-5 w-full rounded-full px-6 py-4 text-[16px] font-extrabold text-white transition-transform active:scale-[0.98] disabled:opacity-40",
          style: {
            background: "linear-gradient(100deg, ".concat(n === C.cta ? "#83C580" : n, ", ").concat(n, ")"),
            boxShadow: "0 6px 18px rgba(117,183,83,.30)"
          },
          children: a
        })
      }

      function I(e) {
        let {
          children: t,
          style: a
        } = e;
        return (0, s.jsx)("div", {
          className: "mb-3 rounded-2xl border bg-white p-4",
          style: {
            borderColor: C.line,
            boxShadow: "0 1px 3px rgba(30,42,56,.05)",
            ...a
          },
          children: t
        })
      }

      function Y(e) {
        let {
          children: t
        } = e;
        return (0, s.jsx)("p", {
          className: "mb-1.5 text-[10px] font-bold uppercase tracking-[0.11em]",
          style: {
            color: C.faint
          },
          children: t
        })
      }

      function V(e) {
        let {
          ratio: t,
          mini: a,
          color: l = C.brand
        } = e;
        return (0, s.jsxs)("div", {
          className: "relative w-full rounded-full ".concat(a ? "mt-2 h-2" : "h-2.5"),
          style: {
            background: a ? "#EFECE5" : "#ECE8DF"
          },
          children: [(0, s.jsx)("span", {
            className: "absolute inset-y-0 rounded-full",
            style: {
              left: "38%",
              width: "24%",
              background: C.zone
            }
          }), (0, s.jsx)("span", {
            className: "absolute top-1/2 -translate-x-1/2 -translate-y-1/2 rounded-full border-white shadow ".concat(a ? "h-3.5 w-3.5 border-[2.5px]" : "h-[18px] w-[18px] border-[3px]"),
            style: {
              left: "".concat(B(t), "%"),
              background: l,
              borderStyle: "solid"
            }
          })]
        })
      }
      let G = {
        en: ["S", "M", "T", "W", "T", "F", "S"],
        es: ["D", "L", "M", "M", "J", "V", "S"],
        pt: ["D", "S", "T", "Q", "Q", "S", "S"]
      };

      function H(e) {
        let {
          lang: t,
          y: a,
          m: n,
          d: r,
          onPick: o
        } = e, i = new Date, [d, c] = (0, l.useState)("" !== a ? Number(a) : i.getFullYear()), [u, m] = (0, l.useState)("" !== n ? Number(n) : i.getMonth()), x = new Date(d, u, 1).getDay(), p = new Date(d, u + 1, 0).getDate(), h = Array.from({
          length: 6
        }, (e, t) => i.getFullYear() - t), b = e => new Date(d, u, e) > i, g = e => "" !== a && Number(a) === d && Number(n) === u && Number(r) === e, y = d === i.getFullYear() && u >= i.getMonth();
        return (0, s.jsxs)("div", {
          className: "mt-1 rounded-2xl border-2 bg-white p-3",
          style: {
            borderColor: "#D8E4F0"
          },
          children: [(0, s.jsxs)("div", {
            className: "flex items-center gap-1.5",
            children: [(0, s.jsx)("button", {
              type: "button",
              onClick: () => {
                0 === u ? (m(11), c(d - 1)) : m(u - 1)
              },
              "aria-label": "prev",
              className: "flex h-8 w-8 items-center justify-center rounded-full text-[15px] font-bold",
              style: {
                color: C.brand,
                background: "#EAF3FC"
              },
              children: "‹"
            }), (0, s.jsx)("select", {
              value: u,
              onChange: e => m(Number(e.target.value)),
              className: "min-w-0 flex-1 appearance-none rounded-lg bg-transparent px-2 py-1.5 text-center text-[14.5px] font-extrabold",
              style: {
                color: C.ink
              },
              "aria-label": T(t, "month"),
              children: P[t].map((e, t) => (0, s.jsx)("option", {
                value: t,
                children: e
              }, e))
            }), (0, s.jsx)("select", {
              value: d,
              onChange: e => c(Number(e.target.value)),
              className: "appearance-none rounded-lg bg-transparent px-2 py-1.5 text-center text-[14.5px] font-extrabold",
              style: {
                color: C.ink
              },
              "aria-label": T(t, "year"),
              children: h.map(e => (0, s.jsx)("option", {
                value: e,
                children: e
              }, e))
            }), (0, s.jsx)("button", {
              type: "button",
              onClick: () => {
                11 === u ? (m(0), c(d + 1)) : m(u + 1)
              },
              disabled: y,
              "aria-label": "next",
              className: "flex h-8 w-8 items-center justify-center rounded-full text-[15px] font-bold disabled:opacity-30",
              style: {
                color: C.brand,
                background: "#EAF3FC"
              },
              children: "›"
            })]
          }), (0, s.jsxs)("div", {
            className: "mt-2 grid grid-cols-7 text-center",
            children: [G[t].map((e, t) => (0, s.jsx)("span", {
              className: "py-1 text-[10.5px] font-bold",
              style: {
                color: C.faint
              },
              children: e
            }, t)), Array.from({
              length: x
            }).map((e, t) => (0, s.jsx)("span", {}, "p".concat(t))), Array.from({
              length: p
            }, (e, t) => t + 1).map(e => (0, s.jsx)("button", {
              type: "button",
              disabled: b(e),
              onClick: () => o(d, u, e),
              className: "mx-auto flex h-9 w-9 items-center justify-center rounded-full text-[13.5px] font-semibold transition-colors disabled:opacity-25",
              style: g(e) ? {
                background: C.brand,
                color: "#fff",
                fontWeight: 800
              } : {
                color: C.ink
              },
              children: e
            }, e))]
          })]
        })
      }

      function Q() {
        var e, t, a, n, o, i, d, c, u, m;
        let {
          steps: x = !1
        } = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {}, [p] = (0, l.useState)(D), [h] = (0, l.useState)(() => {
          try {
            return "0" === new URLSearchParams(location.search).get("capture")
          } catch (e) {
            return !1
          }
        }), {
          track: b,
          lead: g
        } = function(e) {
          let t = (0, l.useRef)({});
          return (0, l.useEffect)(() => {
            var e, a, s, l, n, r;
            let o = new URLSearchParams(location.search),
              i = "";
            try {
              (i = localStorage.getItem("kinedu_session_id") || "") || (i = null !== (s = null === (e = (a = crypto).randomUUID) || void 0 === e ? void 0 : e.call(a)) && void 0 !== s ? s : String(Math.random()).slice(2), localStorage.setItem("kinedu_session_id", i))
            } catch (e) {
              i = null !== (r = null === (l = (n = crypto).randomUUID) || void 0 === l ? void 0 : l.call(n)) && void 0 !== r ? r : "s-".concat(Date.now(), "-").concat(Math.random().toString(36).slice(2))
            }
            let d = "qa" === o.get("env") || "webpromo.kinedu.com" !== location.hostname ? "qa" : "prod";
            t.current = {
              session_id: i,
              environment: d,
              test_id: (o.get("test_id") || "aq-assessment").slice(0, 80),
              variant: (o.get("v") || o.get("ui") || "classic").slice(0, 20),
              utm_source: o.get("utm_source"),
              utm_medium: o.get("utm_medium"),
              utm_campaign: o.get("utm_campaign"),
              utm_content: o.get("utm_content"),
              utm_term: o.get("utm_term"),
              fbclid: o.get("fbclid"),
              gclid: o.get("gclid"),
              ttclid: o.get("ttclid"),
              landing_url: location.href,
              referrer: document.referrer || null
            }
          }, []), {
            track: (0, l.useCallback)((a, s) => {
              let l = t.current;
              l.session_id && fetch("/api/track", {
                method: "POST",
                keepalive: !0,
                headers: {
                  "Content-Type": "application/json"
                },
                body: JSON.stringify({
                  event_name: a,
                  screen: null != s ? s : null,
                  environment: l.environment,
                  language: e,
                  test_id: l.test_id,
                  variant: l.variant,
                  session_id: l.session_id,
                  utm_source: l.utm_source,
                  utm_medium: l.utm_medium,
                  utm_campaign: l.utm_campaign,
                  utm_content: l.utm_content,
                  utm_term: l.utm_term,
                  fbclid: l.fbclid,
                  gclid: l.gclid,
                  ttclid: l.ttclid,
                  landing_url: l.landing_url,
                  referrer: l.referrer,
                  user_agent: navigator.userAgent
                })
              }).catch(() => {})
            }, [e]),
            lead: (0, l.useCallback)((a, s) => {
              let l = t.current;
              return fetch("/api/lead", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json"
                },
                body: JSON.stringify({
                  email: a,
                  name: s,
                  environment: l.environment,
                  language: e,
                  test_id: l.test_id,
                  variant: l.variant,
                  session_id: l.session_id,
                  utm_source: l.utm_source,
                  utm_medium: l.utm_medium,
                  utm_campaign: l.utm_campaign,
                  landing_url: l.landing_url
                })
              })
            }, [e])
          }
        }(p), [y, f] = (0, l.useState)({
          s: "hero"
        }), [, _] = (0, l.useState)(0), [v, j] = (0, l.useState)(""), [A, q] = (0, l.useState)(""), [P, B] = (0, l.useState)(""), [G, Q] = (0, l.useState)(""), $ = "" !== A && "" !== P && "" !== G ? "".concat(G, "-").concat(String(Number(A) + 1).padStart(2, "0"), "-").concat(String(P).padStart(2, "0")) : "", [X, Z] = (0, l.useState)(!1), [ee, et] = (0, l.useState)(34), [ea, es] = (0, l.useState)(null), [el, en] = (0, l.useState)(!1), [er, eo] = (0, l.useState)([]), [ei, ed] = (0, l.useState)([]), [ec, eu] = (0, l.useState)([]), em = (0, l.useRef)(new Map), [ex, ep] = (0, l.useState)(null), [eh, eb] = (0, l.useState)(null), [eg, ey] = (0, l.useState)([]), [ef, e_] = (0, l.useState)(null), [ev, ej] = (0, l.useState)([]), [ew, eN] = (0, l.useState)(!1), [ek, eC] = (0, l.useState)(!1), [eS, eD] = (0, l.useState)(!1), [eF, eA] = (0, l.useState)(""), [eE, eq] = (0, l.useState)("");
        (0, l.useEffect)(() => {
          b("funnel_started", "assessment")
        }, []), (0, l.useEffect)(() => {
          "portrait" === y.s && ex && (b("quiz_answer", "portrait_shown"), (0, r.iA)("ViewContent", {
            content_category: "acquisition",
            content_name: x ? "assessment-classic-steps" : "assessment-classic"
          }))
        }, [y.s]);
        let eP = v.trim() || T(p, "your_baby"),
          eT = (0, l.useMemo)(() => er.map((e, t) => {
            let a = [];
            return e.anchor && a.push(e.anchor), a.push(...e.items), t < ei.length && a.push(ei[t]), a
          }), [er, ei]),
          eM = async () => {
            eD(!0), eA("");
            try {
              var e;
              let t = await fetch("/api/assessment", {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json"
                  },
                  body: JSON.stringify({
                    action: "start",
                    birthdate: $,
                    gestationalWeeks: X ? ee : null
                  })
                }),
                a = await t.json();
              if (422 === t.status && (null == a ? void 0 : a.error) === "age_range") {
                b("quiz_answer", "age_range"), f({
                  s: "age_range"
                });
                return
              }
              if (!t.ok) {
                eA(T(p, "check_date"));
                return
              }
              es(a.ageMonths), en(a.corrected), eo(a.sections), ed(null !== (e = a.calibration) && void 0 !== e ? e : []), b("quiz_started", "child"), f({
                s: "area",
                idx: 0,
                q: 0
              })
            } catch (e) {
              eA(T(p, "conn_error"))
            } finally {
              eD(!1)
            }
          }, ez = async e => {
            eD(!0);
            try {
              var t, a, s, l;
              let n = await fetch("/api/assessment", {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json"
                  },
                  body: JSON.stringify({
                    action: "result",
                    ageMonths: ea,
                    extended: e,
                    answers: [...em.current.entries()].map(e => {
                      let [t, a] = e;
                      return {
                        id: t,
                        y: a
                      }
                    })
                  })
                }),
                r = await n.json();
              if ("extension" === r.stage && !e) {
                eu(r.items), b("extension_started", "extension"), f({
                  s: "extension",
                  q: 0
                });
                return
              }
              ep(r.basic), eb(null !== (t = r.detail) && void 0 !== t ? t : null), ey(null !== (a = r.skills) && void 0 !== a ? a : []), e_(null !== (s = r.activity) && void 0 !== s ? s : null), ej(null !== (l = r.floorActivities) && void 0 !== l ? l : []), b("funnel_completed", "celebrate"), f({
                s: "celebrate"
              })
            } catch (e) {
              eA(T(p, "conn_error"))
            } finally {
              eD(!1)
            }
          };
        if ("hero" === y.s) return (0, s.jsxs)(W, {
          children: [(0, s.jsx)(K, {}), (0, s.jsxs)("div", {
            className: "px-1 text-center",
            children: [(0, s.jsx)("h1", {
              className: "mx-auto mt-2 text-[25px] font-extrabold leading-tight",
              style: {
                color: C.brand,
                letterSpacing: "-0.02em"
              },
              children: T(p, "hero_h1")
            }), (0, s.jsx)("p", {
              className: "mt-2 text-[13.5px] leading-relaxed",
              style: {
                color: C.sub
              },
              children: T(p, "hero_sub")
            }), (0, s.jsx)(J, {
              onClick: () => {
                b("quiz_answer", "hero"), f({
                  s: "primer"
                })
              },
              children: T(p, "hero_cta")
            }), (0, s.jsxs)("div", {
              className: "mt-3 flex flex-wrap items-center justify-center gap-x-3 gap-y-1 text-[11.5px] font-semibold",
              style: {
                color: C.sub
              },
              children: [(0, s.jsx)("span", {
                children: T(p, "trust_time")
              }), (0, s.jsx)("span", {
                children: T(p, "trust_report")
              })]
            })]
          }), (0, s.jsxs)(I, {
            style: {
              marginTop: 16
            },
            children: [(0, s.jsx)(Y, {
              children: T(p, "preview_eyebrow")
            }), (0, s.jsxs)("p", {
              className: "text-[12.5px]",
              children: [T(p, "preview_line"), " ", (0, s.jsxs)("b", {
                style: {
                  color: C.brand
                },
                children: ["7", "en" === p ? "-month-old" : " " + T(p, "preview_months")]
              }), T(p, "preview_line2")]
            }), (0, s.jsxs)("div", {
              className: "mt-2 flex items-center gap-2",
              children: [(0, s.jsx)("div", {
                className: "flex-1",
                children: (0, s.jsx)(V, {
                  ratio: 7 / 6
                })
              }), (0, s.jsxs)("span", {
                className: "whitespace-nowrap text-[10.5px]",
                style: {
                  color: C.faint
                },
                children: ["→ ", M(p, "band_axis_faster")]
              })]
            }), (0, s.jsx)("p", {
              className: "mt-1.5 text-[10.5px]",
              style: {
                color: C.faint
              },
              children: T(p, "band_zone")
            }), (0, s.jsx)("div", {
              className: "mt-2.5 grid grid-cols-2 gap-2",
              children: [{
                area: "Physical",
                key: "at_least20",
                pos: 90
              }, {
                area: "Cognitive",
                key: "around16",
                pos: 78
              }, {
                area: "Language",
                key: "around12",
                pos: 50
              }, {
                area: "Social-Emotional",
                key: "around18",
                pos: 78
              }].map(e => (0, s.jsxs)("div", {
                className: "rounded-xl border p-2.5",
                style: {
                  background: N[e.area].bg,
                  borderColor: N[e.area].border
                },
                children: [(0, s.jsxs)("span", {
                  className: "flex items-center gap-1.5 text-[11.5px] font-bold",
                  children: [(0, s.jsx)("img", {
                    src: k[e.area],
                    alt: "",
                    className: "h-[18px] w-[18px]"
                  }), E(e.area, p, !0)]
                }), (0, s.jsxs)("div", {
                  className: "mt-1 text-[13.5px] font-extrabold",
                  style: {
                    color: w[e.area]
                  },
                  children: [T(p, e.key), " ", (0, s.jsx)("span", {
                    className: "text-[10px] font-normal",
                    style: {
                      color: C.faint
                    },
                    children: T(p, "preview_months")
                  })]
                }), (0, s.jsx)(V, {
                  ratio: .7 + e.pos / 100 * .6,
                  mini: !0,
                  color: w[e.area]
                })]
              }, e.area))
            }), (0, s.jsx)("p", {
              className: "mt-2 text-center text-[10px]",
              style: {
                color: C.faint
              },
              children: T(p, "sample_note")
            })]
          }), (0, s.jsx)("div", {
            className: "mb-3 rounded-xl border p-3 text-[12.5px] leading-relaxed",
            style: {
              background: "#F3FAF0",
              borderColor: "#D9EDD2",
              color: "#3F6B4A"
            },
            children: L(T(p, "honest"))
          }), (0, s.jsx)("p", {
            className: "px-1 text-[11px] leading-relaxed",
            style: {
              color: C.faint
            },
            children: T(p, "science")
          }), (0, s.jsx)(R, {
            lang: p
          })]
        });
        if ("primer" === y.s) return (0, s.jsxs)(W, {
          children: [(0, s.jsx)(K, {}), (0, s.jsxs)("div", {
            className: "my-auto",
            children: [(0, s.jsx)("h2", {
              className: "text-center text-[20px] font-extrabold",
              style: {
                color: C.brand,
                letterSpacing: "-0.015em"
              },
              children: T(p, "primer_title")
            }), (0, s.jsx)("p", {
              className: "mb-4 mt-1 text-center text-[13px]",
              style: {
                color: C.sub
              },
              children: T(p, "primer_sub")
            }), (0, s.jsxs)("div", {
              className: "mb-2.5 flex items-start gap-3 rounded-2xl border bg-white p-3.5",
              style: {
                borderColor: C.line
              },
              children: [(0, s.jsx)("span", {
                className: "text-[20px]",
                children: "\uD83C\uDFAF"
              }), (0, s.jsxs)("div", {
                children: [(0, s.jsx)("h5", {
                  className: "text-[13.5px] font-extrabold",
                  children: T(p, "primer_q_title")
                }), (0, s.jsx)("p", {
                  className: "mt-0.5 text-[12px] leading-relaxed",
                  style: {
                    color: C.sub
                  },
                  children: T(p, "primer_q_body")
                })]
              })]
            }), (0, s.jsxs)("div", {
              className: "mb-2.5 flex items-start gap-3 rounded-2xl border bg-white p-3.5",
              style: {
                borderColor: C.line
              },
              children: [(0, s.jsx)("span", {
                className: "text-[20px]",
                children: "✅"
              }), (0, s.jsxs)("div", {
                children: [(0, s.jsx)("h5", {
                  className: "text-[13.5px] font-extrabold",
                  children: T(p, "primer_two")
                }), (0, s.jsx)("p", {
                  className: "mt-1 text-[12px] leading-relaxed",
                  children: L(M(p, "primer1_yes"))
                }), (0, s.jsx)("p", {
                  className: "mt-1 text-[12px] leading-relaxed",
                  children: L(M(p, "primer1_not"))
                }), (0, s.jsx)("p", {
                  className: "mt-1 text-[12px] leading-relaxed",
                  style: {
                    color: "#3F6B4A"
                  },
                  children: L(M(p, "primer1_none"))
                })]
              })]
            }), (0, s.jsxs)("div", {
              className: "flex items-start gap-3 rounded-2xl border bg-white p-3.5",
              style: {
                borderColor: C.line
              },
              children: [(0, s.jsx)("span", {
                className: "text-[20px]",
                children: "\uD83C\uDF31"
              }), (0, s.jsxs)("div", {
                children: [(0, s.jsx)("h5", {
                  className: "text-[13.5px] font-extrabold",
                  children: T(p, "primer_half_title")
                }), (0, s.jsx)("p", {
                  className: "mt-0.5 text-[12px] leading-relaxed",
                  style: {
                    color: C.sub
                  },
                  children: L(M(p, "primer2_half"))
                })]
              })]
            }), (0, s.jsx)(J, {
              onClick: () => f({
                s: "child"
              }),
              children: T(p, "primer_cta")
            }), (0, s.jsx)(R, {
              lang: p
            })]
          })]
        });
        if ("child" === y.s) return (0, s.jsxs)(W, {
          children: [(0, s.jsx)(K, {}), (0, s.jsxs)("div", {
            className: "my-auto",
            children: [(0, s.jsx)("div", {
              className: "mb-4 h-1.5 overflow-hidden rounded-full",
              style: {
                background: "#ECE8DF"
              },
              children: (0, s.jsx)("div", {
                className: "h-full rounded-full",
                style: {
                  width: "15%",
                  background: C.brand
                }
              })
            }), (0, s.jsx)("h2", {
              className: "text-center text-[21px] font-extrabold",
              style: {
                color: C.brand,
                letterSpacing: "-0.015em"
              },
              children: T(p, "child_title")
            }), (0, s.jsxs)("label", {
              className: "mt-5 block",
              children: [(0, s.jsxs)("span", {
                className: "text-[12.5px] font-bold",
                style: {
                  color: C.sub
                },
                children: [T(p, "name_label"), " ", (0, s.jsx)("span", {
                  className: "font-normal",
                  children: T(p, "optional")
                })]
              }), (0, s.jsx)("input", {
                type: "text",
                value: v,
                onChange: e => j(e.target.value),
                placeholder: T(p, "name_ph"),
                className: "mt-1 w-full rounded-2xl border-2 bg-white px-4 py-3 text-center text-[16px]",
                style: {
                  borderColor: "#D8E4F0"
                }
              })]
            }), (0, s.jsxs)("div", {
              className: "mt-4",
              children: [(0, s.jsx)("span", {
                className: "text-[12.5px] font-bold",
                style: {
                  color: C.sub
                },
                children: T(p, "dob_label")
              }), (0, s.jsx)(H, {
                lang: p,
                y: G,
                m: A,
                d: P,
                onPick: (e, t, a) => {
                  Q(String(e)), q(String(t)), B(String(a))
                }
              })]
            }), (0, s.jsxs)("div", {
              className: "mt-4 rounded-xl border p-3.5",
              style: {
                borderColor: "#E4E0D8",
                background: "#FDFCFA"
              },
              children: [(0, s.jsxs)("label", {
                className: "flex cursor-pointer items-center justify-between",
                children: [(0, s.jsx)("span", {
                  className: "text-[13px] font-bold",
                  style: {
                    color: "#4A5560"
                  },
                  children: T(p, "preterm_q")
                }), (0, s.jsx)("input", {
                  type: "checkbox",
                  checked: X,
                  onChange: e => Z(e.target.checked),
                  className: "h-4 w-4"
                })]
              }), X && (0, s.jsxs)("div", {
                className: "mt-2.5",
                children: [(0, s.jsxs)("span", {
                  className: "text-[12.5px] font-bold",
                  style: {
                    color: C.sub
                  },
                  children: [T(p, "weeks_label"), ": ", ee]
                }), (0, s.jsx)("input", {
                  type: "range",
                  min: 24,
                  max: 36,
                  value: ee,
                  onChange: e => et(Number(e.target.value)),
                  className: "mt-1 w-full"
                }), (0, s.jsx)("div", {
                  className: "mt-2 rounded-lg p-2.5 text-[11.5px]",
                  style: {
                    background: "#EAF3FC",
                    color: "#33689E"
                  },
                  children: T(p, "aap_note")
                })]
              })]
            }), eF && (0, s.jsx)("p", {
              className: "mt-3 text-center text-sm font-semibold text-red-600",
              children: eF
            }), (0, s.jsx)(J, {
              onClick: eM,
              disabled: eS || !$,
              children: eS ? T(p, "preparing") : T(p, "see_questions", {
                name: eP
              })
            }), (0, s.jsx)(R, {
              lang: p
            })]
          })]
        });
        if ("age_range" === y.s) return (0, s.jsxs)(W, {
          children: [(0, s.jsx)(K, {}), (0, s.jsxs)("div", {
            className: "my-auto text-center",
            children: [(0, s.jsx)("div", {
              className: "text-4xl",
              children: "\uD83D\uDC99"
            }), (0, s.jsxs)("h2", {
              className: "mt-2 text-[20px] font-extrabold",
              style: {
                color: C.brand
              },
              children: [T(p, "over48_title"), v.trim() ? ", ".concat(v.trim()) : "", "!"]
            }), (0, s.jsx)(I, {
              style: {
                marginTop: 14,
                textAlign: "left"
              },
              children: (0, s.jsx)("p", {
                className: "text-[13px] leading-relaxed",
                style: {
                  color: C.sub
                },
                children: T(p, "over48_body", {
                  name: eP
                })
              })
            }), (0, s.jsx)(J, {
              onClick: () => {
                b("quiz_answer", "over48_cta"), U(b)
              },
              children: T(p, "over48_cta")
            }), (0, s.jsx)(R, {
              lang: p
            })]
          })]
        });
        if ("area" === y.s || "extension" === y.s) {
          let l = "extension" === y.s,
            r = l ? er.length : y.idx,
            u = l ? ec : null !== (t = eT[r]) && void 0 !== t ? t : [],
            m = l ? "" : null !== (a = null === (e = er[r]) || void 0 === e ? void 0 : e.area) && void 0 !== a ? a : "",
            h = l ? C.brand : null !== (n = w[m]) && void 0 !== n ? n : C.brand,
            g = l ? "/aq-classic/kinedu.png" : k[m],
            j = u.filter(e => em.current.has(e.id)).length,
            S = j === u.length && u.length > 0,
            D = !l && r + 1 < er.length ? er[r + 1].area : null;
          return (0, s.jsxs)(W, {
            children: [(0, s.jsxs)("div", {
              className: "sticky top-0 z-20 -mx-4 px-4 pb-2.5 pt-3",
              style: {
                background: "rgba(250,249,246,.94)",
                backdropFilter: "blur(6px)",
                borderBottom: "1px solid #ECE8DF"
              },
              children: [(0, s.jsx)("div", {
                className: "flex items-center justify-between",
                children: (0, s.jsx)("span", {
                  className: "text-[12.5px] font-bold",
                  style: {
                    color: "#4A5560"
                  },
                  children: v.trim() ? T(p, "assessment_for", {
                    name: v.trim()
                  }) : T(p, "assessment_plain")
                })
              }), (0, s.jsx)("div", {
                className: "mt-2 flex gap-1.5",
                children: er.map((e, t) => {
                  var a, n, o;
                  let i = (null !== (a = eT[t]) && void 0 !== a ? a : []).filter(e => em.current.has(e.id)).length,
                    d = (null !== (n = eT[t]) && void 0 !== n ? n : []).length || 1;
                  return (0, s.jsx)("div", {
                    className: "h-1.5 flex-1 overflow-hidden rounded-full",
                    style: {
                      background: "#ECE8DF"
                    },
                    children: (0, s.jsx)("div", {
                      className: "h-full rounded-full transition-all",
                      style: {
                        background: null !== (o = w[e.area]) && void 0 !== o ? o : C.brand,
                        width: !l && t > r ? "0%" : "".concat(i / d * 100, "%")
                      }
                    })
                  }, t)
                })
              }), (0, s.jsxs)("div", {
                className: "mt-2.5 flex items-center gap-2.5",
                children: [(0, s.jsx)("span", {
                  className: "flex h-9 w-9 shrink-0 items-center justify-center rounded-full",
                  style: {
                    background: (null !== (o = N[m]) && void 0 !== o ? o : {
                      bg: "#EAF3FC"
                    }).bg
                  },
                  children: (0, s.jsx)("img", {
                    src: g,
                    alt: "",
                    className: "h-6 w-6"
                  })
                }), (0, s.jsxs)("div", {
                  className: "min-w-0",
                  children: [(0, s.jsx)("p", {
                    className: "text-[9.5px] font-bold uppercase tracking-[0.1em]",
                    style: {
                      color: h
                    },
                    children: l ? T(p, "going_further") : T(p, "area_of", {
                      i: r + 1,
                      n: er.length
                    })
                  }), (0, s.jsx)("h2", {
                    className: "truncate text-[16px] font-extrabold leading-tight",
                    style: {
                      letterSpacing: "-0.01em"
                    },
                    children: l ? M(p, "deep_title") : E(m, p)
                  }), !l && null != ea && (0, s.jsx)("p", {
                    className: "truncate text-[10px]",
                    style: {
                      color: C.faint
                    },
                    children: T(p, "picked_for", {
                      age: ea,
                      name: eP
                    })
                  })]
                }), (0, s.jsx)("span", {
                  className: "ml-auto rounded-full px-2.5 py-1 text-[12px] font-extrabold tabular-nums",
                  style: {
                    color: h,
                    background: (null !== (i = N[m]) && void 0 !== i ? i : {
                      bg: "#EAF3FC"
                    }).bg
                  },
                  children: x ? "".concat(Math.min((null !== (d = y.q) && void 0 !== d ? d : 0) + 1, u.length), "/").concat(u.length) : "".concat(j, "/").concat(u.length)
                })]
              })]
            }), el && (0, s.jsx)("div", {
              className: "mb-3 rounded-lg p-2.5 text-[11.5px]",
              style: {
                background: "#EAF3FC",
                color: "#33689E"
              },
              children: T(p, "born_at_flow", {
                weeks: ee
              })
            }), x ? (() => {
              var e;
              let t = null !== (e = y.q) && void 0 !== e ? e : 0,
                a = u[t];
              if (!a) return null;
              let n = em.current.get(a.id),
                o = () => {
                  if (eC(!1), t + 1 < u.length) {
                    f(l ? {
                      s: "extension",
                      q: t + 1
                    } : {
                      s: "area",
                      idx: r,
                      q: t + 1
                    });
                    return
                  }
                  if (l) {
                    ez(!0);
                    return
                  }
                  b("quiz_answer", "area_".concat(m)), D ? (f({
                    s: "area",
                    idx: r + 1,
                    q: 0
                  }), window.scrollTo(0, 0)) : ez(!1)
                },
                i = e => {
                  eS || (em.current.set(a.id, e), _(e => e + 1), eC(!1), setTimeout(o, 220))
                };
              return (0, s.jsxs)("div", {
                className: "mt-3 overflow-hidden rounded-3xl border bg-white px-5 pb-5 pt-6 text-center",
                style: {
                  border: "2px solid ".concat(h),
                  boxShadow: "0 8px 26px ".concat(h, "22")
                },
                children: [l && 0 === t && (0, s.jsx)("p", {
                  className: "mt-2 text-[12px] leading-relaxed",
                  style: {
                    color: C.sub
                  },
                  children: T(p, "ext_note", {
                    name: eP === T(p, "your_baby") ? T(p, "your_baby_cap") : eP
                  })
                }), (0, s.jsx)("p", {
                  className: "mx-auto mt-4 min-h-[76px] max-w-[30ch] text-[18px] font-bold leading-snug",
                  style: {
                    letterSpacing: "-0.01em"
                  },
                  children: F(a, p)
                }), (0, s.jsxs)("div", {
                  className: "mt-5 flex gap-2.5",
                  children: [(0, s.jsx)("button", {
                    onClick: () => i(0),
                    className: "flex-1 rounded-2xl border-2 py-4 text-[15px] font-extrabold transition-all duration-150 active:scale-95",
                    style: 0 === n ? {
                      background: "#fff",
                      borderColor: h,
                      color: h,
                      boxShadow: "0 2px 10px ".concat(h, "33")
                    } : {
                      background: "#fff",
                      borderColor: "#DFDAD0",
                      color: "#7C8794"
                    },
                    children: M(p, "chip_not_yet")
                  }), (0, s.jsx)("button", {
                    onClick: () => i(1),
                    className: "flex-1 rounded-2xl border-2 py-4 text-[15px] font-extrabold transition-all duration-150 active:scale-95",
                    style: 1 === n ? {
                      background: h,
                      borderColor: h,
                      color: "#fff",
                      boxShadow: "0 3px 12px ".concat(h, "55")
                    } : {
                      background: "#fff",
                      borderColor: "#DFDAD0",
                      color: "#7C8794"
                    },
                    children: M(p, "chip_yes")
                  })]
                }), (0, s.jsxs)("div", {
                  className: "mt-4 flex items-center justify-between",
                  children: [t > 0 || !l && r > 0 ? (0, s.jsx)("button", {
                    className: "text-[12.5px] font-bold",
                    style: {
                      color: C.faint
                    },
                    onClick: () => {
                      var e;
                      if (eC(!0), t > 0) {
                        f(l ? {
                          s: "extension",
                          q: t - 1
                        } : {
                          s: "area",
                          idx: r,
                          q: t - 1
                        });
                        return
                      }!l && r > 0 && f({
                        s: "area",
                        idx: r - 1,
                        q: (null !== (e = eT[r - 1]) && void 0 !== e ? e : []).length - 1
                      })
                    },
                    children: T(p, "back")
                  }) : (0, s.jsx)("span", {}), void 0 !== n && ek && (0, s.jsxs)("button", {
                    className: "text-[12.5px] font-bold",
                    style: {
                      color: h
                    },
                    onClick: o,
                    children: [T(p, "next_prefix"), " ›"]
                  })]
                })]
              })
            })() : (0, s.jsxs)("div", {
              className: "mt-3 overflow-hidden rounded-3xl border bg-white",
              style: {
                border: "2px solid ".concat(h),
                boxShadow: "0 8px 26px ".concat(h, "22")
              },
              children: [l && (0, s.jsx)("p", {
                className: "px-4 pb-1 text-[12px] leading-relaxed",
                style: {
                  color: C.sub
                },
                children: T(p, "ext_note", {
                  name: eP === T(p, "your_baby") ? T(p, "your_baby_cap") : eP
                })
              }), (0, s.jsx)("div", {
                className: "divide-y",
                style: {
                  borderColor: "#F5F2EC"
                },
                children: u.map(e => {
                  var t;
                  let a = em.current.get(e.id),
                    n = (null !== (t = N[l ? "Physical" : m]) && void 0 !== t ? t : {
                      bg: "#F1FAFE"
                    }).bg;
                  return (0, s.jsxs)("div", {
                    className: "flex items-center justify-between gap-3 px-4 py-3.5 transition-colors duration-300",
                    style: void 0 !== a ? {
                      background: n
                    } : {},
                    children: [(0, s.jsx)("p", {
                      className: "text-[13.2px] leading-snug",
                      style: void 0 !== a ? {
                        color: "#4A5560"
                      } : {},
                      children: F(e, p)
                    }), (0, s.jsxs)("div", {
                      className: "flex w-[132px] shrink-0 justify-end gap-1.5",
                      children: [(0, s.jsx)("button", {
                        onClick: () => {
                          em.current.set(e.id, 0), _(e => e + 1)
                        },
                        className: "rounded-full border-[1.5px] px-3 py-2 text-[11px] font-bold transition-all duration-150 active:scale-95",
                        style: 0 === a ? {
                          background: "#fff",
                          borderColor: h,
                          color: h,
                          fontWeight: 800,
                          boxShadow: "0 1px 6px ".concat(h, "33")
                        } : {
                          background: "#fff",
                          borderColor: "#DFDAD0",
                          color: "#7C8794",
                          opacity: 1 === a ? .55 : 1
                        },
                        children: M(p, "chip_not_yet")
                      }), (0, s.jsx)("button", {
                        onClick: () => {
                          em.current.set(e.id, 1), _(e => e + 1)
                        },
                        className: "rounded-full border-[1.5px] px-3.5 py-2 text-[11px] font-bold transition-all duration-150 active:scale-95",
                        style: 1 === a ? {
                          background: h,
                          borderColor: h,
                          color: "#fff",
                          boxShadow: "0 2px 8px ".concat(h, "55")
                        } : {
                          background: "#fff",
                          borderColor: "#DFDAD0",
                          color: "#7C8794",
                          opacity: 0 === a ? .55 : 1
                        },
                        children: M(p, "chip_yes")
                      })]
                    })]
                  }, e.id)
                })
              }), (0, s.jsxs)("div", {
                className: "flex items-center justify-between px-4 py-3.5",
                children: [!l && r > 0 ? (0, s.jsx)("button", {
                  className: "text-[12.5px] font-bold",
                  style: {
                    color: C.faint
                  },
                  onClick: () => {
                    f({
                      s: "area",
                      idx: r - 1,
                      q: 0
                    }), window.scrollTo(0, 0)
                  },
                  children: T(p, "back")
                }) : (0, s.jsx)("span", {}), (0, s.jsx)("button", {
                  onClick: () => {
                    if (S && !eS) {
                      if (l) {
                        ez(!0);
                        return
                      }
                      b("quiz_answer", "area_".concat(m)), D ? (f({
                        s: "area",
                        idx: r + 1,
                        q: 0
                      }), window.scrollTo(0, 0)) : ez(!1)
                    }
                  },
                  disabled: !S || eS,
                  className: "rounded-full px-5 py-2.5 text-[13px] font-extrabold text-white transition-transform active:scale-[0.98] disabled:opacity-40",
                  style: {
                    background: l || !D ? h : null !== (c = w[D]) && void 0 !== c ? c : C.brand
                  },
                  children: eS ? "…" : l || !D ? T(p, "see_reading", {
                    name: eP
                  }) : "".concat(T(p, "next_prefix"), " ").concat(E(D, p), " ›")
                })]
              })]
            }), (0, s.jsx)(R, {
              lang: p
            })]
          })
        }
        if ("celebrate" === y.s) {
          let e = em.current.size;
          return (0, s.jsxs)(W, {
            children: [(0, s.jsx)(K, {}), (0, s.jsxs)("div", {
              className: "my-auto text-center",
              children: [(0, s.jsx)("div", {
                className: "text-6xl",
                children: "\uD83C\uDF89"
              }), (0, s.jsx)("h2", {
                className: "mt-3 text-[24px] font-extrabold",
                style: {
                  color: C.brand,
                  letterSpacing: "-0.015em"
                },
                children: T(p, "done_title")
              }), (0, s.jsx)("p", {
                className: "mx-auto mt-2 max-w-[34ch] text-[14px] leading-relaxed",
                style: {
                  color: C.sub
                },
                children: T(p, "done_sub", {
                  name: eP
                })
              }), (0, s.jsxs)("div", {
                className: "mt-4 flex items-center justify-center gap-2",
                children: [(0, s.jsxs)("span", {
                  className: "rounded-full border bg-white px-3.5 py-1.5 text-[12px] font-bold",
                  style: {
                    borderColor: C.line,
                    color: C.sub
                  },
                  children: ["✅ ", T(p, "done_answers", {
                    n: e
                  })]
                }), (0, s.jsxs)("span", {
                  className: "rounded-full border bg-white px-3.5 py-1.5 text-[12px] font-bold",
                  style: {
                    borderColor: C.line,
                    color: C.sub
                  },
                  children: [(0, s.jsxs)("span", {
                    className: "mr-1 inline-flex items-center gap-0.5",
                    children: [(0, s.jsx)("img", {
                      src: k.Physical,
                      alt: "",
                      className: "h-3.5 w-3.5"
                    }), (0, s.jsx)("img", {
                      src: k.Cognitive,
                      alt: "",
                      className: "h-3.5 w-3.5"
                    }), (0, s.jsx)("img", {
                      src: k.Language,
                      alt: "",
                      className: "h-3.5 w-3.5"
                    }), (0, s.jsx)("img", {
                      src: k["Social-Emotional"],
                      alt: "",
                      className: "h-3.5 w-3.5"
                    })]
                  }), T(p, "done_areas")]
                })]
              }), (0, s.jsx)(J, {
                onClick: () => f(h ? {
                  s: "portrait"
                } : {
                  s: "email"
                }),
                children: T(p, "see_reading", {
                  name: eP
                })
              })]
            })]
          })
        }
        if ("email" === y.s) {
          let e = /^\S+@\S+\.\S+$/.test(eE.trim()),
            t = async () => {
              if (e && !eS) {
                eD(!0);
                try {
                  await g(eE.trim(), v.trim())
                } catch (e) {}
                try {
                  sessionStorage.setItem("kinedu_email", eE.trim())
                } catch (e) {}
                if ((0, r.iA)("Lead", {
                    content_category: "acquisition",
                    content_name: "assessment-classic"
                  }), ex && "ok" === ex.state) {
                  let e = [];
                  for (let t of ["Physical", "Cognitive", "Language", "Social-Emotional"]) {
                    let a = eg.find(e => e.area === t && e.items.some(e => "open" === e.status)),
                      s = null == a ? void 0 : a.items.find(e => "open" === e.status);
                    a && s && e.push(F({
                      id: s.id,
                      area: t,
                      skill: a.skill,
                      title: s.title
                    }, p))
                  }
                  fetch("/api/send-reading", {
                    method: "POST",
                    headers: {
                      "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                      email: eE.trim(),
                      name: v.trim(),
                      lang: p,
                      ageMonths: ex.ageMonths,
                      devAge: ex.devAge,
                      capped: ex.capped,
                      bandLine: "well_ahead" === ex.band || "little_ahead" === ex.band ? O(p, ex.band) : void 0,
                      opening: e[0],
                      openingCount: Math.max(e.length - 1, 0),
                      activityTitle: ef ? ef.title[p] || ef.title.en : void 0
                    }),
                    keepalive: !0
                  }).then(e => e.json()).then(e => {
                    e && e.ok && b("quiz_answer", "reading_email_sent")
                  }).catch(() => {})
                }
                eD(!1), b("quiz_answer", "email_captured"), f({
                  s: "portrait"
                })
              }
            };
          return (0, s.jsxs)(W, {
            children: [(0, s.jsx)(K, {}), (0, s.jsxs)("div", {
              className: "my-auto",
              children: [(0, s.jsx)("div", {
                className: "text-center text-5xl",
                children: "\uD83D\uDC8C"
              }), (0, s.jsx)("h2", {
                className: "mt-3 text-center text-[21px] font-extrabold leading-snug",
                style: {
                  color: C.brand,
                  letterSpacing: "-0.015em"
                },
                children: T(p, "email_title", {
                  name: eP
                })
              }), (0, s.jsxs)("div", {
                className: "mx-auto mt-4 max-w-[40ch]",
                children: [(0, s.jsxs)("p", {
                  className: "flex items-start gap-2 text-[13.5px] leading-relaxed",
                  style: {
                    color: C.sub
                  },
                  children: [(0, s.jsx)("span", {
                    className: "mt-px font-extrabold",
                    style: {
                      color: C.cta
                    },
                    children: "✓"
                  }), T(p, "email_b1")]
                }), (0, s.jsxs)("p", {
                  className: "mt-1.5 flex items-start gap-2 text-[13.5px] leading-relaxed",
                  style: {
                    color: C.sub
                  },
                  children: [(0, s.jsx)("span", {
                    className: "mt-px font-extrabold",
                    style: {
                      color: C.cta
                    },
                    children: "✓"
                  }), T(p, "email_b2")]
                }), (0, s.jsxs)("p", {
                  className: "mt-1.5 flex items-start gap-2 text-[13.5px] leading-relaxed",
                  style: {
                    color: C.sub
                  },
                  children: [(0, s.jsx)("span", {
                    className: "mt-px font-extrabold",
                    style: {
                      color: C.cta
                    },
                    children: "✓"
                  }), T(p, "email_b3")]
                })]
              }), (0, s.jsx)("input", {
                type: "email",
                value: eE,
                onChange: e => eq(e.target.value),
                onKeyDown: e => {
                  "Enter" === e.key && t()
                },
                placeholder: T(p, "email_ph"),
                className: "mt-4 w-full rounded-2xl border-2 bg-white px-4 py-3.5 text-center text-[16px]",
                style: {
                  borderColor: "#D8E4F0"
                }
              }), (0, s.jsx)("button", {
                disabled: !e || eS,
                onClick: t,
                className: "mt-3 w-full rounded-full px-6 py-4 text-[16px] font-extrabold text-white transition-transform active:scale-[0.98] disabled:opacity-40",
                style: {
                  background: "linear-gradient(100deg, #83C580, ".concat(C.cta, ")"),
                  boxShadow: "0 6px 18px rgba(117,183,83,.30)"
                },
                children: eS ? "…" : "".concat(T(p, "email_btn"), " →")
              }), (0, s.jsx)("p", {
                className: "mt-2.5 text-center text-[11px]",
                style: {
                  color: C.faint
                },
                children: T(p, "email_micro")
              }), (0, s.jsx)(R, {
                lang: p
              })]
            })]
          })
        }
        if ("portrait" === y.s) {
          if (!ex) return null;
          if ("below_floor" === ex.state) return (0, s.jsxs)(W, {
            children: [(0, s.jsx)(K, {}), (0, s.jsxs)("div", {
              className: "my-auto",
              children: [(0, s.jsx)("h2", {
                className: "text-center text-[19px] font-extrabold",
                style: {
                  color: C.brand
                },
                children: M(p, "floor_title")
              }), (0, s.jsxs)(I, {
                style: {
                  marginTop: 12
                },
                children: [(0, s.jsx)(Y, {
                  children: T(p, "activities_eyebrow")
                }), (ev.length ? ev.map(e => e.title[p] || e.title.en) : function(e, t) {
                  var a, s, l;
                  let n = null !== (l = null === (a = S[e]) || void 0 === a ? void 0 : a[t]) && void 0 !== l ? l : null === (s = S.en) || void 0 === s ? void 0 : s[t];
                  return Array.isArray(n) ? n : []
                }(p, "floor_activities")).map((e, t) => (0, s.jsxs)("div", {
                  className: "flex items-center gap-2.5 border-b py-2 text-[13px] last:border-b-0",
                  style: {
                    borderColor: "#F1EEE7"
                  },
                  children: [(0, s.jsx)("span", {
                    className: "flex h-8 w-8 shrink-0 items-center justify-center rounded-lg text-[15px]",
                    style: {
                      background: "#F0F6FB"
                    },
                    children: ["\uD83E\uDDF8", "\uD83D\uDCD6", "\uD83C\uDFB5"][t % 3]
                  }), (0, s.jsx)("span", {
                    children: e
                  })]
                }, t)), (0, s.jsx)("div", {
                  className: "mt-2.5 rounded-lg p-3 text-[12px] leading-relaxed",
                  style: {
                    background: "#F6F9FC",
                    color: C.sub
                  },
                  children: M(p, "floor_note")
                })]
              }), (0, s.jsx)(J, {
                onClick: () => U(b),
                children: T(p, "get_activities", {
                  name: eP
                })
              }), (0, s.jsx)(R, {
                lang: p
              })]
            })]
          });
          if ("ok" !== ex.state) return (0, s.jsxs)(W, {
            children: [(0, s.jsx)(K, {}), (0, s.jsxs)("div", {
              className: "my-auto text-center",
              children: [(0, s.jsx)("h2", {
                className: "text-[19px] font-extrabold",
                style: {
                  color: C.brand
                },
                children: M(p, "not_enough")
              }), (0, s.jsx)(J, {
                onClick: () => f({
                  s: "area",
                  idx: 0,
                  q: 0
                }),
                children: T(p, "continue_answering")
              })]
            })]
          });
          let e = ex.devAge,
            t = e / Math.max(ex.ageMonths, 1),
            a = z(M(p, "dev_detail_name"), {
              age: ex.ageMonths,
              name: eP === T(p, "your_baby") ? T(p, "your_baby_cap") : eP,
              D: ex.capped ? "".concat(e, "+") : e
            }),
            l = [];
          for (let e of ["Physical", "Cognitive", "Language", "Social-Emotional"]) {
            let t = eg.find(t => t.area === e && t.items.some(e => "open" === e.status)),
              a = null == t ? void 0 : t.items.find(e => "open" === e.status);
            t && a && l.push({
              area: e,
              title: F({
                id: a.id,
                area: e,
                skill: t.skill,
                title: a.title
              }, p)
            })
          }
          let n = ex.ageMonths >= 24,
            r = (eh && "ok" === eh.state && eh.areas && !eh.areasDefaultHidden ? eh.areas : []).filter(e => "ok" === e.state),
            o = r.length ? r.reduce((e, t) => t.months > e.months ? t : e) : null,
            i = null !== (m = null !== (u = null == o ? void 0 : o.area) && void 0 !== u ? u : ex.teaserArea) && void 0 !== m ? m : null;
          return (0, s.jsxs)(W, {
            children: [(0, s.jsx)(K, {}), (0, s.jsxs)("div", {
              className: "flex flex-col pb-24 text-center",
              children: [(0, s.jsx)("div", {
                className: "text-4xl",
                children: "\uD83C\uDF89"
              }), (0, s.jsx)("h2", {
                className: "mt-1 text-[20px] font-extrabold",
                style: {
                  color: C.brand,
                  letterSpacing: "-0.01em"
                },
                children: v.trim() ? T(p, "ready", {
                  name: v.trim()
                }) : T(p, "ready_generic")
              }), (0, s.jsxs)(I, {
                style: {
                  marginTop: 14,
                  textAlign: "left",
                  order: n ? 2 : 1
                },
                children: [(0, s.jsx)(Y, {
                  children: M(p, "picture_title")
                }), (0, s.jsx)("p", {
                  className: "text-[17px] font-bold leading-snug",
                  children: a
                }), ("well_ahead" === ex.band || "little_ahead" === ex.band) && (0, s.jsxs)("span", {
                  className: "mt-2.5 inline-flex items-center gap-1.5 rounded-full px-3 py-1.5 text-[12px] font-bold",
                  style: {
                    background: "#EAF5E9",
                    color: "#3E7C3E"
                  },
                  children: ["✦ ", O(p, ex.band)]
                }), ex.capped && (0, s.jsx)("p", {
                  className: "mt-2 text-[12px] leading-relaxed",
                  style: {
                    color: C.sub
                  },
                  children: M(p, "ceiling_note")
                }), (0, s.jsxs)("div", {
                  className: "mt-3.5 flex items-center gap-2",
                  children: [(0, s.jsx)("div", {
                    className: "flex-1",
                    children: (0, s.jsx)(V, {
                      ratio: t
                    })
                  }), (0, s.jsxs)("span", {
                    className: "whitespace-nowrap text-[10.5px]",
                    style: {
                      color: C.faint
                    },
                    children: ["→ ", M(p, "band_axis_faster")]
                  })]
                }), (0, s.jsx)("p", {
                  className: "mt-1.5 text-[10.5px]",
                  style: {
                    color: C.faint
                  },
                  children: T(p, "zone_at", {
                    age: ex.ageMonths
                  })
                }), (0, s.jsxs)("p", {
                  className: "mt-2.5 rounded-lg p-2.5 text-[11.5px] leading-relaxed",
                  style: {
                    background: "#F3F8F1",
                    color: "#3E7C3E"
                  },
                  children: ["✓ ", T(p, "reading_done")]
                }), el && (0, s.jsx)("p", {
                  className: "mt-2.5 rounded-lg p-2.5 text-[11.5px]",
                  style: {
                    background: "#EAF3FC",
                    color: "#33689E"
                  },
                  children: T(p, "born_at", {
                    weeks: ee
                  })
                })]
              }), (0, s.jsxs)(I, {
                style: {
                  textAlign: "left",
                  order: n ? 3 : 2
                },
                children: [(0, s.jsx)(Y, {
                  children: M(p, "areas_title")
                }), (0, s.jsx)("div", {
                  className: "grid grid-cols-2 gap-2.5",
                  children: ["Physical", "Cognitive", "Language", "Social-Emotional"].map(e => {
                    var t;
                    let a = null !== (t = N[e]) && void 0 !== t ? t : {
                      bg: "#fff",
                      border: C.line
                    };
                    if (i === e) {
                      let t = o && o.area === e ? o : null;
                      return (0, s.jsxs)("div", {
                        className: "relative rounded-xl border p-3 text-left",
                        style: {
                          background: a.bg,
                          borderColor: a.border
                        },
                        children: [(0, s.jsxs)("span", {
                          className: "flex items-center gap-1.5 text-[12px] font-bold",
                          children: [(0, s.jsx)("img", {
                            src: k[e],
                            alt: "",
                            className: "h-[18px] w-[18px]"
                          }), E(e, p, !0)]
                        }), t ? (0, s.jsxs)(s.Fragment, {
                          children: [(0, s.jsxs)("div", {
                            className: "mt-1.5 text-[15px] font-extrabold",
                            style: {
                              color: w[e],
                              letterSpacing: "-0.01em"
                            },
                            children: [t.atLeast ? T(p, "at_least_lbl") : T(p, "around_lbl"), " ", t.months, " ", T(p, "months_lbl")]
                          }), (0, s.jsx)(V, {
                            ratio: t.months / Math.max(ex.ageMonths, 1),
                            mini: !0,
                            color: w[e]
                          })]
                        }) : (0, s.jsxs)("div", {
                          className: "mt-1.5 text-[13px] font-extrabold leading-snug",
                          style: {
                            color: w[e]
                          },
                          children: ["✦ ", T(p, "strongest_today")]
                        })]
                      }, e)
                    }
                    return (0, s.jsxs)("button", {
                      onClick: () => U(b),
                      className: "relative rounded-xl border p-3 text-left active:scale-[0.98]",
                      style: {
                        background: a.bg,
                        borderColor: a.border
                      },
                      children: [(0, s.jsx)("span", {
                        className: "absolute right-2.5 top-2.5 text-[13px]",
                        children: "\uD83D\uDD12"
                      }), (0, s.jsxs)("span", {
                        className: "flex items-center gap-1.5 text-[12px] font-bold",
                        children: [(0, s.jsx)("img", {
                          src: k[e],
                          alt: "",
                          className: "h-[18px] w-[18px]"
                        }), E(e, p, !0)]
                      }), (0, s.jsxs)("div", {
                        className: "mt-1.5 select-none text-[15px] font-extrabold blur-[6px]",
                        style: {
                          color: w[e],
                          letterSpacing: "-0.01em"
                        },
                        "aria-hidden": "true",
                        children: [T(p, "around_lbl"), " 88"]
                      }), (0, s.jsx)("div", {
                        className: "text-[10.5px]",
                        style: {
                          color: "#7C8794"
                        },
                        children: T(p, "locked_hint")
                      }), (0, s.jsx)("div", {
                        className: "mt-2",
                        children: (0, s.jsx)("div", {
                          className: "relative h-2 rounded-full blur-[3px]",
                          style: {
                            background: "#EFECE5"
                          },
                          children: (0, s.jsx)("span", {
                            className: "absolute inset-y-0 rounded-full",
                            style: {
                              left: "38%",
                              width: "24%",
                              background: C.zone
                            }
                          })
                        })
                      })]
                    }, e)
                  })
                }), ex.teaserArea && (0, s.jsxs)("p", {
                  className: "mt-3 text-[12.5px] leading-relaxed",
                  style: {
                    color: C.sub
                  },
                  children: ["✨ ", z(M(p, "teaser"), {
                    name: E(ex.teaserArea, p)
                  })]
                })]
              }), l.length > 0 && (0, s.jsxs)(I, {
                style: {
                  textAlign: "left",
                  order: n ? 1 : 3
                },
                children: [(0, s.jsx)(Y, {
                  children: T(p, "opening_eyebrow", {
                    name: eP
                  })
                }), (0, s.jsxs)("div", {
                  className: "flex items-center gap-2.5 py-1.5 text-[13px]",
                  children: [(0, s.jsx)("img", {
                    src: k[l[0].area],
                    alt: "",
                    className: "h-[18px] w-[18px] shrink-0"
                  }), (0, s.jsx)("span", {
                    children: l[0].title
                  })]
                }), l.slice(1, 3).map(e => (0, s.jsxs)("button", {
                  onClick: () => U(b),
                  className: "flex w-full items-center gap-2.5 border-t py-2 text-left text-[13px]",
                  style: {
                    borderColor: "#F1EEE7"
                  },
                  children: [(0, s.jsx)("img", {
                    src: k[e.area],
                    alt: "",
                    className: "h-[18px] w-[18px] shrink-0"
                  }), (0, s.jsx)("span", {
                    className: "select-none blur-[5px]",
                    "aria-hidden": "true",
                    children: e.title
                  }), (0, s.jsx)("span", {
                    className: "ml-auto shrink-0 text-[12px]",
                    children: "\uD83D\uDD12"
                  })]
                }, e.area)), l.length > 1 && (0, s.jsx)("p", {
                  className: "mt-2 text-[11px]",
                  style: {
                    color: C.faint
                  },
                  children: T(p, "opening_more", {
                    n: Math.max(l.length - 1, 1)
                  })
                })]
              }), (0, s.jsx)("p", {
                className: "mx-auto mt-1 max-w-[44ch] text-[11.5px] leading-relaxed",
                style: {
                  color: C.faint,
                  order: 5
                },
                children: T(p, "every_pace")
              }), (0, s.jsx)("div", {
                style: {
                  order: 6
                },
                children: (0, s.jsx)(R, {
                  lang: p
                })
              })]
            }), (0, s.jsx)("div", {
              className: "fixed inset-x-0 bottom-0 border-t px-4 pb-3 pt-3",
              style: {
                background: "rgba(250,249,246,.96)",
                borderColor: C.line,
                backdropFilter: "blur(4px)"
              },
              children: (0, s.jsxs)("div", {
                className: "mx-auto w-full max-w-md",
                children: [(0, s.jsx)("button", {
                  onClick: () => U(b),
                  className: "w-full rounded-2xl py-3.5 text-[15.5px] font-extrabold text-white active:scale-[0.98]",
                  style: {
                    background: C.cta
                  },
                  children: T(p, "unlock_cta", {
                    name: v.trim() || T(p, "sticky_your")
                  })
                }), (0, s.jsx)("p", {
                  className: "mt-1.5 text-center text-[11px]",
                  style: {
                    color: C.faint
                  },
                  children: T(p, "unlock_note")
                }), (0, s.jsx)("p", {
                  className: "mt-0.5 text-center text-[10.5px]",
                  style: {
                    color: C.faint
                  },
                  children: T(p, "retro_note")
                })]
              })
            })]
          })
        }
        return null
      }
      var $ = a(5562);

      function X() {
        let [e, t] = (0, l.useState)(null);
        return ((0, l.useEffect)(() => {
          try {
            let e = new URLSearchParams(location.search);
            t(e.get("ui") || e.get("v") || "")
          } catch (e) {
            t("")
          }
        }, []), null === e) ? null : "hook" === e ? (0, s.jsx)($.default, {}) : "classic" === e ? (0, s.jsx)(Q, {}) : "classic-steps" === e ? (0, s.jsx)(Q, {
          steps: !0
        }) : (0, s.jsx)(_, {})
      }
    }
  },
  function(e) {
    e.O(0, [562, 971, 117, 744], function() {
      return e(e.s = 1976)
    }), _N_E = e.O()
  }
]);