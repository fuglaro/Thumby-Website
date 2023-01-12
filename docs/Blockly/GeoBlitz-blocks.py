{"blocks":{"languageVersion":0,"blocks":[{"type":"procedures_defnoreturn","id":"$%d8%0}c(XO]M+/-HjD)","x":-868,"y":818,"icons":{"comment":{"text":"Draw wiping lines on either side","pinned":false,"height":80,"width":160}},"fields":{"NAME":"do line"},"inputs":{"STACK":{"block":{"type":"drawLine","id":"fZk/7b4p3/,SNfp5s+_W","fields":{"COL":"1"},"inputs":{"X":{"shadow":{"type":"math_number","id":"[);}}5J3pAc.ZCWj;TyD","fields":{"NUM":0}}},"Y":{"shadow":{"type":"math_number","id":"nHN:0`f!cbD/kqO|Lp-y","fields":{"NUM":19}}},"X2":{"shadow":{"type":"math_number","id":"wc*}dn$!e$M;f)*si*Up","fields":{"NUM":20}},"block":{"type":"variables_get","id":";29c+B_,5[O5d:}8;zjm","fields":{"VAR":{"id":"n.[mBZ}0?exqKYg3]FAn"}}}},"Y2":{"shadow":{"type":"math_number","id":"Ek`Xu^TI|jp/{Y4c}@m`","fields":{"NUM":19}},"block":{"type":"math_modulo","id":"pvF[Mm_{93o_)Q6`XwQc","inputs":{"DIVIDEND":{"shadow":{"type":"math_number","id":";`*ywvF}SiN3uP5p$s|t","fields":{"NUM":61}},"block":{"type":"var_to_int","id":"KpD`v|W#kPYkxjgK_+S|","inputs":{"var":{"block":{"type":"math_arithmetic","id":"-9zf!|jJCM9y_Fjf]{:4","fields":{"OP":"DIVIDE"},"inputs":{"A":{"shadow":{"type":"math_number","id":"~c3P7v{UI,-o6?IC=Sg}","fields":{"NUM":1}},"block":{"type":"variables_get","id":"0^m;tS9fdaCHSCMK(e$~","fields":{"VAR":{"id":"I.l(x3AK)mRwJRN-n~Ck"}}}},"B":{"shadow":{"type":"math_number","id":".CBUO3%ADs,Sf#}f@0*G","fields":{"NUM":10}}}}}}}}},"DIVISOR":{"shadow":{"type":"math_number","id":".e_d/_-F2YMo{{uzvti;","fields":{"NUM":39}}}}}}},"next":{"block":{"type":"drawLine","id":"~2fw!!b}6|WX{Y#LO3Bs","fields":{"COL":"1"},"inputs":{"X":{"shadow":{"type":"math_number","id":"i=9VpQ5ocd#yop${2Yop","fields":{"NUM":71}}},"Y":{"shadow":{"type":"math_number","id":"}sCUE6kNK?,5oF+|+9DU","fields":{"NUM":19}}},"X2":{"shadow":{"type":"math_number","id":"4J1hvNHSCwPKH.2CQu|T","fields":{"NUM":51}},"block":{"type":"math_arithmetic","id":"`d|+jjIv9r#,-(/[jY9j","fields":{"OP":"MINUS"},"inputs":{"A":{"shadow":{"type":"math_number","id":"giLb!c(WjTDxBSlRCB#Z","fields":{"NUM":71}}},"B":{"shadow":{"type":"math_number","id":"B39jhL`A@|Oyffc2+As.","fields":{"NUM":1}},"block":{"type":"variables_get","id":"P?I3r9LtFo+[q#_Z6W^G","fields":{"VAR":{"id":"n.[mBZ}0?exqKYg3]FAn"}}}}}}},"Y2":{"shadow":{"type":"math_number","id":"s*q_4M6YcpVCuKn#NQim","fields":{"NUM":19}},"block":{"type":"math_arithmetic","id":"!s(M4xl[{^LXO9|PocXX","fields":{"OP":"MINUS"},"inputs":{"A":{"shadow":{"type":"math_number","id":"XV*pd_R3*YTs?=/wH=j{","fields":{"NUM":39}}},"B":{"shadow":{"type":"math_number","id":":GUD$,]Q7U**!FO1zu|7","fields":{"NUM":1}},"block":{"type":"math_modulo","id":"{gyKY}sFP~![Yrvz0#Cy","inputs":{"DIVIDEND":{"shadow":{"type":"math_number","id":";`*ywvF}SiN3uP5p$s|t","fields":{"NUM":61}},"block":{"type":"var_to_int","id":"!.-EUA^$9{UDRn[`2{7V","inputs":{"var":{"block":{"type":"math_arithmetic","id":"vG`V:}b.bH@Lec~OWKPE","fields":{"OP":"DIVIDE"},"inputs":{"A":{"shadow":{"type":"math_number","id":"~c3P7v{UI,-o6?IC=Sg}","fields":{"NUM":1}},"block":{"type":"variables_get","id":"T:1]/E[{?0ThVyf`Qd31","fields":{"VAR":{"id":"I.l(x3AK)mRwJRN-n~Ck"}}}},"B":{"shadow":{"type":"math_number","id":"7*?v5TkDDYgal(M/xiE[","fields":{"NUM":10}}}}}}}}},"DIVISOR":{"shadow":{"type":"math_number","id":"=W2:Ehuxaw:ol?gkU4Jo","fields":{"NUM":39}}}}}}}}}}}}}}}},{"type":"procedures_defnoreturn","id":"f{k=%/}GB?+nYa:iiko*","x":-868,"y":746,"icons":{"comment":{"text":"Describe this function...","pinned":false,"height":80,"width":160}},"fields":{"NAME":"setup line"},"inputs":{"STACK":{"block":{"type":"variables_set","id":"xysLSSOs:5X*LdDxH~]n","fields":{"VAR":{"id":"n.[mBZ}0?exqKYg3]FAn"}},"inputs":{"VALUE":{"block":{"type":"math_number","id":"^,spkIg|d_[I[W~tCdM=","fields":{"NUM":20}}}}}}}},{"type":"procedures_defnoreturn","id":"UpY#h+JWeH~TngJ7PfQI","x":-868,"y":1235,"icons":{"comment":{"text":"Draw a border around the game area","pinned":false,"height":80,"width":160}},"fields":{"NAME":"do border"},"inputs":{"STACK":{"block":{"type":"drawRectangle","id":"CrPz!*@S3@RY9Kw{2ftP","fields":{"COL":"1","SHAPE":"Rectangle"},"inputs":{"X":{"shadow":{"type":"math_number","id":"B:Tw;6v^A;BXTR7w6Xh5","fields":{"NUM":0}}},"Y":{"shadow":{"type":"math_number","id":"0.35=EUH[t_NCx8UI{/{","fields":{"NUM":0}}},"X2":{"shadow":{"type":"math_number","id":"HKWe[0nagmp.*UT}u_`(","fields":{"NUM":72}}},"Y2":{"shadow":{"type":"math_number","id":"GhH(1@9!|DH?bLE#nmB^","fields":{"NUM":40}}}}}}}},{"type":"procedures_defnoreturn","id":"*KvRMxHv|Rh+!j]T;,Pe","x":-869,"y":1447,"icons":{"comment":{"text":"set up the initial position of box","pinned":false,"height":80,"width":160}},"fields":{"NAME":"setup box"},"inputs":{"STACK":{"block":{"type":"variables_set","id":":ne+9e)$1@^a:pRLki5;","fields":{"VAR":{"id":"M2:JuNi|%(hg-D*;kX[("}},"inputs":{"VALUE":{"block":{"type":"math_number","id":"tc(~D):c}lMyekSu{q%i","fields":{"NUM":30}}}},"next":{"block":{"type":"variables_set","id":"qJkR-+UCp/:4Ss$k7Fx[","fields":{"VAR":{"id":")H}#]R2Va?*JLJ4X0[?f"}},"inputs":{"VALUE":{"block":{"type":"math_number","id":"f`gre2p+/qSU]zrN[aaH","fields":{"NUM":0}}}}}}}}}},{"type":"procedures_defnoreturn","id":"L;ZNX-V9-JyWXTTtn0Sx","x":-868,"y":1547,"icons":{"comment":{"text":"draw and move a box that flips in random directions and stays in the game area","pinned":false,"height":80,"width":160}},"fields":{"NAME":"do box"},"inputs":{"STACK":{"block":{"type":"drawRectangle","id":"@Mz*jocwg`J@.X$vh(Ov","fields":{"COL":"1","SHAPE":"FilledRectangle"},"inputs":{"X":{"shadow":{"type":"math_number","id":"0eS~KIn./KLT7/:y/*l/","fields":{"NUM":40}},"block":{"type":"variables_get","id":"MFahG-sTg9be|;hf:;Co","fields":{"VAR":{"id":"M2:JuNi|%(hg-D*;kX[("}}}},"Y":{"shadow":{"type":"math_number","id":"N!:aakC_JgFi/oHARRIn","fields":{"NUM":20}},"block":{"type":"variables_get","id":"+c@8ij=F{2@8UNP*BLJY","fields":{"VAR":{"id":")H}#]R2Va?*JLJ4X0[?f"}}}},"X2":{"shadow":{"type":"math_number","id":"_lU0S9JmC`iry4=;WieH","fields":{"NUM":6}}},"Y2":{"shadow":{"type":"math_number","id":"qn4yiDJx=Kxx-`,t/$v0","fields":{"NUM":4}}}},"next":{"block":{"type":"procedures_ifreturn","id":"n*~+sZjE.6@Ft=7Qwp,r","extraState":"<mutation value=\"0\"></mutation>","inputs":{"CONDITION":{"block":{"type":"logic_compare","id":"E7:g|lLle%rDG=@EM[vu","fields":{"OP":"NEQ"},"inputs":{"A":{"block":{"type":"math_modulo","id":"XW:gA[jO2@G%Qd1nQD#B","inputs":{"DIVIDEND":{"shadow":{"type":"math_number","id":"`Ftwh}$lj5uUnIC.@W/5","fields":{"NUM":61}},"block":{"type":"variables_get","id":"PX~ddawK[Tj]sGA);=V[","fields":{"VAR":{"id":"I.l(x3AK)mRwJRN-n~Ck"}}}},"DIVISOR":{"shadow":{"type":"math_number","id":"W8tpI651HcSbdA^pH7mV","fields":{"NUM":20}}}}}},"B":{"block":{"type":"math_number","id":"450qVi/Dczy.vsy1ByYm","fields":{"NUM":0}}}}}}},"next":{"block":{"type":"controls_if","id":":+%93z?R%bwdZpMtUlT#","extraState":{"hasElse":true},"inputs":{"IF0":{"block":{"type":"logic_compare","id":"Gh.%YJ0M(CcnL][uy^}/","fields":{"OP":"EQ"},"inputs":{"A":{"block":{"type":"math_random_int","id":"?V@3df{L?IZ0gS)p0/.g","inputs":{"FROM":{"shadow":{"type":"math_number","id":"pM9u`|s}YieT!8Ma!|9U","fields":{"NUM":0}}},"TO":{"shadow":{"type":"math_number","id":"8pFweLt:z+S:q,g?`q50","fields":{"NUM":1}}}}}},"B":{"block":{"type":"math_number","id":"7PY?uaiE@kp:IS?4%k-f","fields":{"NUM":1}}}}}},"DO0":{"block":{"type":"math_change","id":"vxke`tN5L#@n4B[iOpF;","fields":{"VAR":{"id":"M2:JuNi|%(hg-D*;kX[("}},"inputs":{"DELTA":{"shadow":{"type":"math_number","id":"4-1/kE{TG@tcXA?q@F#b","fields":{"NUM":1}},"block":{"type":"math_arithmetic","id":"M4!=-:dbO~bSK[[;*u%h","fields":{"OP":"MULTIPLY"},"inputs":{"A":{"shadow":{"type":"math_number","id":"Ckggt[hJ=PV9Vg:8gpEJ","fields":{"NUM":1}},"block":{"type":"math_random_int","id":"kD_#/v?+jU}5aYhCPf2M","inputs":{"FROM":{"shadow":{"type":"math_number","id":"~DyPua(mcpp0o50H|?et","fields":{"NUM":-1}}},"TO":{"shadow":{"type":"math_number","id":",-kKul@cgS$SB`L09):t","fields":{"NUM":1}}}}}},"B":{"shadow":{"type":"math_number","id":"v0J%!(3|(_//^-Gby:h}","fields":{"NUM":6}}}}}}}}},"ELSE":{"block":{"type":"math_change","id":"GE/[bSViT07kX%?emKCV","fields":{"VAR":{"id":")H}#]R2Va?*JLJ4X0[?f"}},"inputs":{"DELTA":{"shadow":{"type":"math_number","id":"U3,JN(iRyQoMTt~2[?}:","fields":{"NUM":1}},"block":{"type":"math_arithmetic","id":"*DV`oP=@TLwk:?Kr()M?","fields":{"OP":"MULTIPLY"},"inputs":{"A":{"shadow":{"type":"math_number","id":"Ckggt[hJ=PV9Vg:8gpEJ","fields":{"NUM":1}},"block":{"type":"math_random_int","id":"6$JB.EqQPR!jW;y1C|X-","inputs":{"FROM":{"shadow":{"type":"math_number","id":"_jrT|9_oTl5P?]m_1(P0","fields":{"NUM":-1}}},"TO":{"shadow":{"type":"math_number","id":"tR@JDIc.#n[A*Q/fB4(}","fields":{"NUM":1}}}}}},"B":{"shadow":{"type":"math_number","id":"|@ebhFNkJC0AAOpU$~m|","fields":{"NUM":4}}}}}}}}}},"next":{"block":{"type":"variables_set","id":"M%-;tuJy/wAmE4{fo%7B","fields":{"VAR":{"id":"M2:JuNi|%(hg-D*;kX[("}},"inputs":{"VALUE":{"block":{"type":"math_constrain","id":"q,Y;Y8vjN@z3keZ46)vX","inputs":{"VALUE":{"shadow":{"type":"math_number","id":"/^gwdx*08WsT7cBDV^]H","fields":{"NUM":50}},"block":{"type":"variables_get","id":"QHf9p_`HMFy)1Sn|n0am","fields":{"VAR":{"id":"M2:JuNi|%(hg-D*;kX[("}}}},"LOW":{"shadow":{"type":"math_number","id":"76Q%Pcf_T3Csn!lN+57Q","fields":{"NUM":0}}},"HIGH":{"shadow":{"type":"math_number","id":"nmC?sFDq/qA}1vY;e@US","fields":{"NUM":65}}}}}}},"next":{"block":{"type":"variables_set","id":"|{$5JWBBT|Ot99#0yA7e","fields":{"VAR":{"id":")H}#]R2Va?*JLJ4X0[?f"}},"inputs":{"VALUE":{"block":{"type":"math_constrain","id":"RWsJF/._+Q}g(tkdwuWR","inputs":{"VALUE":{"shadow":{"type":"math_number","id":"/^gwdx*08WsT7cBDV^]H","fields":{"NUM":50}},"block":{"type":"variables_get","id":"G@WfEWPyHV:x#E|+=8|6","fields":{"VAR":{"id":")H}#]R2Va?*JLJ4X0[?f"}}}},"LOW":{"shadow":{"type":"math_number","id":".bi08+[,MO2.Mr}e.!_`","fields":{"NUM":0}}},"HIGH":{"shadow":{"type":"math_number","id":"VeNQFJa.k*]ILKZ4Sb).","fields":{"NUM":35}}}}}}}}}}}}}}}}}}},{"type":"procedures_defnoreturn","id":"-?qhS:)%m4D~4[nS*ebN","x":-869,"y":2945,"icons":{"comment":{"text":"Create the sprite and starting location for footsteps that cycle up the screen","pinned":false,"height":80,"width":160}},"fields":{"NAME":"setup walker"},"inputs":{"STACK":{"block":{"type":"load_anim_sprite","id":"MYunBrK4A6YUxE`*w3g*","data":"# BITMAP: width: 32, height: 8\nbitmap2 = bytearray([15,31,248,240,30,30,120,120,60,60,60,60,120,120,30,30,240,248,31,15,120,120,30,30,60,60,60,60,30,30,120,120])","fields":{"VAR":{"id":"3ji2~Vh$Rt8bxaq!*LQJ"},"FRMS":8},"next":{"block":{"type":"set_transparency","id":"5*OqWFU9!=9.7c!YnBxF","fields":{"VAR":{"id":"3ji2~Vh$Rt8bxaq!*LQJ"},"VAL":"0"}}}}}}},{"type":"procedures_defnoreturn","id":"+,Q3WWipZ+8OGpjn.Ho.","x":-869,"y":3059,"icons":{"comment":{"text":"Draw and move the footsteps that cycle up the screen","pinned":false,"height":80,"width":160}},"fields":{"NAME":"do walker"},"inputs":{"STACK":{"block":{"type":"drawSprite","id":"~dE$5NzjXz0_(U(G7ni}","fields":{"VAR":{"id":"3ji2~Vh$Rt8bxaq!*LQJ"}},"next":{"block":{"type":"procedures_ifreturn","id":"G|~FD^zA_}~M9WPjreKb","extraState":"<mutation value=\"0\"></mutation>","inputs":{"CONDITION":{"block":{"type":"logic_compare","id":"S}9^vk{OU`^2ar=~A8o[","fields":{"OP":"NEQ"},"inputs":{"A":{"block":{"type":"math_modulo","id":"o@cl+m+=DVu]95:ZU/4{","inputs":{"DIVIDEND":{"shadow":{"type":"math_number","id":"`Ftwh}$lj5uUnIC.@W/5","fields":{"NUM":61}},"block":{"type":"variables_get","id":"+#aCS`wQNj^oCSurdjp5","fields":{"VAR":{"id":"I.l(x3AK)mRwJRN-n~Ck"}}}},"DIVISOR":{"shadow":{"type":"math_number","id":"1sz.|S?({U7(=NkpC5q=","fields":{"NUM":4}}}}}},"B":{"block":{"type":"math_number","id":"8,Lf*K%spRevHNOSc)|i","fields":{"NUM":0}}}}}}},"next":{"block":{"type":"setFrame","id":"5$}1bkbB@qnRt3,e6#kC","fields":{"VAR":{"id":"3ji2~Vh$Rt8bxaq!*LQJ"}},"inputs":{"FRM":{"shadow":{"type":"math_number","id":"hau]aXsP%!-W5_MdUR)*","fields":{"NUM":1}},"block":{"type":"math_arithmetic","id":"0N+a+(B4pCDy^`EEqkFL","fields":{"OP":"ADD"},"inputs":{"A":{"shadow":{"type":"math_number","id":"-1F((UKTbLW($sMHk9W3","fields":{"NUM":1}},"block":{"type":"get_sprite_frame","id":"J[)fFsTZ7Twsq/dcvE$B","fields":{"VAR":{"id":"3ji2~Vh$Rt8bxaq!*LQJ"}}}},"B":{"shadow":{"type":"math_number","id":"Ed)*wqVw[]clZ1maE)$n","fields":{"NUM":1}}}}}}},"next":{"block":{"type":"move_y_by","id":"n22@oMNit3e:pg9$qN2v","fields":{"VAR":{"id":"3ji2~Vh$Rt8bxaq!*LQJ"}},"inputs":{"V":{"shadow":{"type":"math_number","id":"ud_f~7{a)_|JP(yE%|%r","fields":{"NUM":-1}}}},"next":{"block":{"type":"controls_if","id":"!d:kLU6Uv2?[4h2ABL=,","inputs":{"IF0":{"block":{"type":"logic_compare","id":"{,4MAz/A9Wx~ZdQ0#g[e","fields":{"OP":"LT"},"inputs":{"A":{"block":{"type":"get_sprite_size","id":"Zil`j6RV;BegUrNAi{ah","fields":{"VAR":{"id":"3ji2~Vh$Rt8bxaq!*LQJ"},"ATTR":"y"}}},"B":{"block":{"type":"math_number","id":"T^}sSEf;:;{8ly5GT^[{","fields":{"NUM":-7}}}}}},"DO0":{"block":{"type":"move_y_to","id":":tqgI#9SRY*ivTS~6CSj","fields":{"VAR":{"id":"3ji2~Vh$Rt8bxaq!*LQJ"}},"inputs":{"V":{"shadow":{"type":"math_number","id":"MWg;,YWNtxF[2Zr(BkLH","fields":{"NUM":47}}}},"next":{"block":{"type":"move_x_to","id":"3*A|_$fVcs*1rsL;-o?x","fields":{"VAR":{"id":"3ji2~Vh$Rt8bxaq!*LQJ"}},"inputs":{"V":{"shadow":{"type":"math_number","id":"sLlq+`^D9%[$zX/.tWaX","fields":{"NUM":30}},"block":{"type":"math_random_int","id":"b{pCo16c_/1GUR{{2ICw","inputs":{"FROM":{"shadow":{"type":"math_number","id":")(|+tlNlB=@(%,bXsX~.","fields":{"NUM":0}}},"TO":{"shadow":{"type":"math_number","id":"7TI)UJgb~Q|-spG+,V!i","fields":{"NUM":67}}}}}}}}}}}}}}}}}}}}}}}},{"type":"procedures_defnoreturn","id":"6g7D8vA{i|~h0I?ucSo-","x":-869,"y":2073,"icons":{"comment":{"text":"Make the sprite and set the starting location and direction for a kite that bounces around the screen","pinned":false,"height":80,"width":160}},"fields":{"NAME":"setup kite"},"inputs":{"STACK":{"block":{"type":"load_sprite","id":"s=^kiVb?^Kp#;CQa/qMI","data":"# BITMAP: width: 8, height: 8\nbitmap4 = bytearray([255,63,15,7,35,51,65,1])","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"}},"next":{"block":{"type":"set_transparency","id":"Ioal6B*?zrK@*qW`00=b","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"},"VAL":"0"},"next":{"block":{"type":"move_x_to","id":"0oGM_^gAtVQ,*Ng?)vNy","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"}},"inputs":{"V":{"shadow":{"type":"math_number","id":"1Yn9QyNBK:9}}x1Z[#C[","fields":{"NUM":64}}}},"next":{"block":{"type":"move_y_to","id":"mt!^9}QAz}M_{L-HHh:{","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"}},"inputs":{"V":{"shadow":{"type":"math_number","id":"Y__q0JTP]sE`6MQ)2r41","fields":{"NUM":32}}}},"next":{"block":{"type":"variables_set","id":"qQuY*@F0``ae)3-A},R!","fields":{"VAR":{"id":"{FG/%QL#1-NTW}S$F[j4"}},"inputs":{"VALUE":{"block":{"type":"math_number","id":"H|JquHk;r4yyO]K]qIo,","fields":{"NUM":-1}}}},"next":{"block":{"type":"variables_set","id":"V@%4?dqe]I7RYbX8+as}","fields":{"VAR":{"id":"CQP[|F6CP;bX1O!7H}dj"}},"inputs":{"VALUE":{"block":{"type":"math_number","id":"]`R:rY}|HJKW`6{1Op3J","fields":{"NUM":-1}}}}}}}}}}}}}}}}}},{"type":"procedures_defnoreturn","id":"I/]|O!3lh0.Z~LY30$uM","x":-868,"y":2298,"icons":{"comment":{"text":"Draw and move the kite that bounces around the screen","pinned":false,"height":80,"width":160}},"fields":{"NAME":"do kite"},"inputs":{"STACK":{"block":{"type":"drawSprite","id":"us-.8^6Zc1Q2xpuVo,/O","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"}},"next":{"block":{"type":"procedures_ifreturn","id":"C%R-f]p{*HHtty5t:4!*","extraState":"<mutation value=\"0\"></mutation>","inputs":{"CONDITION":{"block":{"type":"logic_compare","id":"hparG[+TYfPLU:9)S|8n","fields":{"OP":"NEQ"},"inputs":{"A":{"block":{"type":"math_modulo","id":"GTtzBKzWpa+x`vY75iGZ","inputs":{"DIVIDEND":{"shadow":{"type":"math_number","id":"`Ftwh}$lj5uUnIC.@W/5","fields":{"NUM":61}},"block":{"type":"variables_get","id":"k!C,DSOpJ!#U[!85;EAD","fields":{"VAR":{"id":"I.l(x3AK)mRwJRN-n~Ck"}}}},"DIVISOR":{"shadow":{"type":"math_number","id":"1)W{+d@VumRnCxv]Ddvz","fields":{"NUM":4}}}}}},"B":{"block":{"type":"math_number","id":"rwY:Q4g=z{Z2pz?yt+I|","fields":{"NUM":0}}}}}}},"next":{"block":{"type":"move_x_by","id":"N1fbc(B=DO9$HfflH0[9","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"}},"inputs":{"V":{"shadow":{"type":"math_number","id":"Oge$4X~@ju6~XYI[x!!+","fields":{"NUM":1}},"block":{"type":"variables_get","id":"r:A]qpa7+j]UPO:Q6-9G","fields":{"VAR":{"id":"{FG/%QL#1-NTW}S$F[j4"}}}}},"next":{"block":{"type":"move_y_by","id":"Wd7oRt/wd[+=[45|I_EY","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"}},"inputs":{"V":{"shadow":{"type":"math_number","id":";gy$m_]I2na)9m8L|d!Z","fields":{"NUM":-1}},"block":{"type":"variables_get","id":"3dI|BSx~X~Qpa]O0M#t:","fields":{"VAR":{"id":"CQP[|F6CP;bX1O!7H}dj"}}}}},"next":{"block":{"type":"controls_if","id":"W)Z7ib8pRA{^g6+(@;jP","inputs":{"IF0":{"block":{"type":"logic_compare","id":"zb3I@~PuQ#8=ymR8nO|Y","fields":{"OP":"LT"},"inputs":{"A":{"block":{"type":"get_sprite_size","id":"/Uc6#.V9,[i@DB4g0!z@","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"},"ATTR":"x"}}},"B":{"block":{"type":"math_number","id":"5}A8Vmt~=M~ATbeo]z9,","fields":{"NUM":0}}}}}},"DO0":{"block":{"type":"variables_set","id":"VhH[@~M=X/ytUp%^U1wu","fields":{"VAR":{"id":"{FG/%QL#1-NTW}S$F[j4"}},"inputs":{"VALUE":{"block":{"type":"math_number","id":",$Ce`]kxm_vxhs^x])29","fields":{"NUM":1}}}},"next":{"block":{"type":"mirror","id":"EFE0L+7pU[iG-R!bt}1=","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"}}}}}}},"next":{"block":{"type":"controls_if","id":"Hqx:hKsUwaNN_Jv_6/4m","inputs":{"IF0":{"block":{"type":"logic_compare","id":"F8y1W9:Y2/P+.z~gi)*j","fields":{"OP":"GT"},"inputs":{"A":{"block":{"type":"get_sprite_size","id":"XkixCs78SQLnZmjWmd(S","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"},"ATTR":"x"}}},"B":{"block":{"type":"math_number","id":"P}P^9iYl?9mFZ!aJw1GI","fields":{"NUM":63}}}}}},"DO0":{"block":{"type":"variables_set","id":"pu[`yFL9Gh{kL?l-nRL6","fields":{"VAR":{"id":"{FG/%QL#1-NTW}S$F[j4"}},"inputs":{"VALUE":{"block":{"type":"math_number","id":"n^@w1`NS+LnVe7K-a+|{","fields":{"NUM":-1}}}},"next":{"block":{"type":"mirror","id":"pA88Im$lAjlEl+lP{z]-","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"}}}}}}},"next":{"block":{"type":"controls_if","id":"ng90._.FK?B5;B?zc8!?","inputs":{"IF0":{"block":{"type":"logic_compare","id":"7Eaf!VO6Q5FOOG()PV!O","fields":{"OP":"LT"},"inputs":{"A":{"block":{"type":"get_sprite_size","id":"c1^6.zXNp=}=B8a%R7t{","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"},"ATTR":"y"}}},"B":{"block":{"type":"math_number","id":"`DSds3Ozw37eXv$HDZv(","fields":{"NUM":0}}}}}},"DO0":{"block":{"type":"variables_set","id":"@rVU/r2^!_cw=rD7+`]k","fields":{"VAR":{"id":"CQP[|F6CP;bX1O!7H}dj"}},"inputs":{"VALUE":{"block":{"type":"math_number","id":"uF/`[Io$g/#~aLrxbGp%","fields":{"NUM":1}}}},"next":{"block":{"type":"flip","id":"IWxyEyK]O3K=s@l)xP#)","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"}}}}}}},"next":{"block":{"type":"controls_if","id":"vmNZ=#1AVsd~I_9Sa=g4","inputs":{"IF0":{"block":{"type":"logic_compare","id":"]#.s}yu$q(wVFRhT(~w=","fields":{"OP":"GT"},"inputs":{"A":{"block":{"type":"get_sprite_size","id":"1/8^f+{]p1GSCNFe?C_{","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"},"ATTR":"y"}}},"B":{"block":{"type":"math_number","id":"K{PttzueO`:U7)Gh]`Y*","fields":{"NUM":31}}}}}},"DO0":{"block":{"type":"variables_set","id":"E7v;21$(DI8{sXm(s5wj","fields":{"VAR":{"id":"CQP[|F6CP;bX1O!7H}dj"}},"inputs":{"VALUE":{"block":{"type":"math_number","id":"==T0A$^sC)?)HZE{T:N}","fields":{"NUM":-1}}}},"next":{"block":{"type":"flip","id":"2MDuY;WOJ6cWLz`}`wL/","fields":{"VAR":{"id":"3aXk?x36f]s//OcS.=(`"}}}}}}}}}}}}}}}}}}}}}}}}},{"type":"procedures_defnoreturn","id":"h3mEJ(J3vPHd^vBylD^G","x":-869,"y":3407,"icons":{"comment":{"text":"Make the player sprite and set the initial location","pinned":false,"height":80,"width":160}},"fields":{"NAME":"setup bird"},"inputs":{"STACK":{"block":{"type":"load_anim_sprite","id":":a=Y,tTA]4k7]I0.)$I1","data":"# BITMAP: width: 16, height: 7\nbitmap8 = bytearray([12,14,11,31,61,124,15,3,20,22,26,31,61,60,110,71])","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"},"FRMS":2},"next":{"block":{"type":"load_anim_sprite","id":"qwYQhtR45MnU@eshFMx1","data":"# BITMAP: width: 16, height: 7\nbitmap12 = bytearray([30,31,31,63,127,126,127,15,62,63,63,63,127,126,127,111])","fields":{"VAR":{"id":"tqzNgIxRp/BdM*m?P*z~"},"FRMS":2},"next":{"block":{"type":"move_x_to","id":"zai%TV|I`jqs{xQe9*:I","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"}},"inputs":{"V":{"shadow":{"type":"math_number","id":"r.b`H2+3156Io-^}-(nw","fields":{"NUM":32}}}},"next":{"block":{"type":"move_y_to","id":"WSiX/~.Qf|2,,gcrFL;R","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"}},"inputs":{"V":{"shadow":{"type":"math_number","id":"r)sh=kxp`Bj{[%EOV~,V","fields":{"NUM":18}}}}}}}}}}}}}},{"type":"procedures_defnoreturn","id":"T%34|2??q_%X0|r=s;(f","x":-867,"y":3589,"icons":{"comment":{"text":"Draw the player ship and respond to movement input.","pinned":false,"height":80,"width":160}},"fields":{"NAME":"do bird"},"inputs":{"STACK":{"block":{"type":"drawSpriteWithMask","id":"=cV[n_APuHBVt$M+.!lg","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"},"MSK":{"id":"tqzNgIxRp/BdM*m?P*z~"}},"next":{"block":{"type":"setFrame","id":"Zblf8PbR#TH(ALUUZQMx","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"}},"inputs":{"FRM":{"shadow":{"type":"math_number","id":"FYhFKI}XJCCe)ni%YV=n","fields":{"NUM":0}},"block":{"type":"logic_ternary","id":"oCh]7YDlIQrj8`lC;djK","inputs":{"IF":{"block":{"type":"button_pressed","id":";l!IhARbwC!AjSI#vX0]","fields":{"BUTTON":"actionPressed"}}},"THEN":{"block":{"type":"math_number","id":"4oL!maX^Ez*sone+8^tY","fields":{"NUM":1}}},"ELSE":{"block":{"type":"math_number","id":"7-IP%a}Oz[n!uvBr=HwQ","fields":{"NUM":0}}}}}}},"next":{"block":{"type":"setFrame","id":"k;w!YqG$6RSbmq+SZ!VP","fields":{"VAR":{"id":"tqzNgIxRp/BdM*m?P*z~"}},"inputs":{"FRM":{"shadow":{"type":"math_number","id":"sL+}WskP2?(KfsgSbL/K","fields":{"NUM":1}},"block":{"type":"get_sprite_frame","id":"xD@5HMqE`RvqA#mEye|E","fields":{"VAR":{"id":"tqzNgIxRp/BdM*m?P*z~"}}}}},"next":{"block":{"type":"procedures_ifreturn","id":"V2IYI:Ev,:UAeRB;4_Pg","extraState":"<mutation value=\"0\"></mutation>","inputs":{"CONDITION":{"block":{"type":"logic_compare","id":"0{2BmBvPkOpAyR^?y:^:","fields":{"OP":"EQ"},"inputs":{"A":{"block":{"type":"math_modulo","id":"HamkK#%sp.z%e-G,4TJW","inputs":{"DIVIDEND":{"shadow":{"type":"math_number","id":"`Ftwh}$lj5uUnIC.@W/5","fields":{"NUM":61}},"block":{"type":"variables_get","id":"9},%9HPC!UT`$ht,i6?;","fields":{"VAR":{"id":"I.l(x3AK)mRwJRN-n~Ck"}}}},"DIVISOR":{"shadow":{"type":"math_number","id":"mViC?kVOoJ1iPfO6qwe$","fields":{"NUM":3}}}}}},"B":{"block":{"type":"math_number","id":"2n3W%C@$7j+A`z,%)]Eo","fields":{"NUM":0}}}}}}},"next":{"block":{"type":"controls_if","id":"^FoYpH%eK7:`_(%19^Pf","inputs":{"IF0":{"block":{"type":"button_pressed","id":"@EdhPHlCUN%Y*1@h|aLA","fields":{"BUTTON":"buttonU.pressed"}}},"DO0":{"block":{"type":"move_y_by","id":"eva/e$sQ0b]a!@xRuSzE","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"}},"inputs":{"V":{"shadow":{"type":"math_number","id":"R7tZhTvbto73*~DjqSTi","fields":{"NUM":-1}}}}}}},"next":{"block":{"type":"controls_if","id":"Pz@fDNJRkhQoek4rp/N6","inputs":{"IF0":{"block":{"type":"button_pressed","id":"%r?IU51!Na^BF4{bk-w8","fields":{"BUTTON":"buttonD.pressed"}}},"DO0":{"block":{"type":"move_y_by","id":"0YIjXfOf1^e)G3xkx!T~","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"}},"inputs":{"V":{"shadow":{"type":"math_number","id":"9vQ3Vl-X=v{]e8:CUo%6","fields":{"NUM":1}}}}}}},"next":{"block":{"type":"controls_if","id":"yQ.s-Mp_VwyN-`E}qd.(","inputs":{"IF0":{"block":{"type":"button_pressed","id":"^{3hEG~ISr?1IRj3]P5~","fields":{"BUTTON":"buttonL.pressed"}}},"DO0":{"block":{"type":"move_x_by","id":"|P#i{4YN5])s{!#jt_+-","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"}},"inputs":{"V":{"shadow":{"type":"math_number","id":"SGHAhmg``+{TCEG;aS05","fields":{"NUM":-1}}}},"next":{"block":{"type":"controls_if","id":"l*v]X1MnG3cPa~EpV=L2","inputs":{"IF0":{"block":{"type":"get_sprite_orien","id":"vGLfb3{mJ7x8,M2?Wu.5","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"},"ATTR":"mirrorX"}}},"DO0":{"block":{"type":"mirror","id":";s0$:*e)5%+DSMgFmS[W","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"}}}}}}}}}},"next":{"block":{"type":"controls_if","id":"m(C*hw!j{A{V5-P-{SGZ","inputs":{"IF0":{"block":{"type":"button_pressed","id":"yGU*2MSJYI0V}LvSi/Tp","fields":{"BUTTON":"buttonR.pressed"}}},"DO0":{"block":{"type":"move_x_by","id":"jgD:q49?V)22DRp7=L;g","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"}},"inputs":{"V":{"shadow":{"type":"math_number","id":"*UBuZ_oKKH|5Cj9}iA}?","fields":{"NUM":1}}}},"next":{"block":{"type":"controls_if","id":"@lDgB)HhaY2YXAMTK16O","inputs":{"IF0":{"block":{"type":"logic_negate","id":"ky3{h7PVe,e_*$-*4O9I","inputs":{"BOOL":{"block":{"type":"get_sprite_orien","id":"M}H-4V.MDz|COvwvC5[X","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"},"ATTR":"mirrorX"}}}}}},"DO0":{"block":{"type":"mirror","id":"3n/6z_p7KVne}09`FkYw","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"}}}}}}}}}},"next":{"block":{"type":"move_y_to","id":"9y!Q;HgMJmzZhPg_D}03","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"}},"inputs":{"V":{"shadow":{"type":"math_number","id":";Xt2h*UIMIha1f|`NcS$","fields":{"NUM":20}},"block":{"type":"math_constrain","id":"qn#a=CIE[gxDq,Vz{FZT","inputs":{"VALUE":{"shadow":{"type":"math_number","id":"/^gwdx*08WsT7cBDV^]H","fields":{"NUM":50}},"block":{"type":"get_sprite_size","id":"|4hIK?mDFc`YlOPA/Y`4","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"},"ATTR":"y"}}},"LOW":{"shadow":{"type":"math_number","id":"lCG@bBrY=P$OR43M]6Ys","fields":{"NUM":0}}},"HIGH":{"shadow":{"type":"math_number","id":"`D-S1F_;;,;^+deI4.@-","fields":{"NUM":33}}}}}}},"next":{"block":{"type":"move_x_to","id":"w..7a%_iLQ:MZXRv/FPG","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"}},"inputs":{"V":{"shadow":{"type":"math_number","id":"nM.pSrT+v,.j8#VsJX1m","fields":{"NUM":30}},"block":{"type":"math_constrain","id":"0{GY875(LPctk}H:ZL~!","inputs":{"VALUE":{"shadow":{"type":"math_number","id":"/^gwdx*08WsT7cBDV^]H","fields":{"NUM":50}},"block":{"type":"get_sprite_size","id":"qI+jcLEA@U0|u@#/h|QE","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"},"ATTR":"x"}}},"LOW":{"shadow":{"type":"math_number","id":"ZX8jid/g^sjA.H#=dm(k","fields":{"NUM":0}}},"HIGH":{"shadow":{"type":"math_number","id":"ROSM-nVAbG}+[VF}|Ylt","fields":{"NUM":64}}}}}}}}}}}}}}}}}}}}}}}}}}}}},{"type":"procedures_defnoreturn","id":"/1MM~Rk3m@*_gpokd^5!","x":-867,"y":4479,"icons":{"comment":{"text":"Move the player's bullet and shoot in response to buttons.","pinned":false,"height":80,"width":160}},"fields":{"NAME":"do bullet"},"inputs":{"STACK":{"block":{"type":"drawPixel","id":"@V8|A,:vxyGe4SQnUC6a","fields":{"COL":"1"},"inputs":{"X":{"shadow":{"type":"math_number","id":"Aaw;O[,JzfdpGQ|V;$2+","fields":{"NUM":0}},"block":{"type":"variables_get","id":"!tSt|j-UPXeXdaW=W4q0","fields":{"VAR":{"id":"?[4~c[u3HW5m^8t}uvcy"}}}},"Y":{"shadow":{"type":"math_number","id":"kDhn3`6qAhGDcvU6.}3-","fields":{"NUM":0}},"block":{"type":"variables_get","id":"ya$KPC__B1~aq`~Wrm$k","fields":{"VAR":{"id":"]1}?Z$Ct,(2W(!?i#W@f"}}}}},"next":{"block":{"type":"math_change","id":"|Dd{WShk]yfUmRYMf!V#","fields":{"VAR":{"id":"?[4~c[u3HW5m^8t}uvcy"}},"inputs":{"DELTA":{"shadow":{"type":"math_number","id":"[!C#3v0dgCT$Uu^IS9D[","fields":{"NUM":1}},"block":{"type":"variables_get","id":"`oq7zxuIm%/I67YoVA[+","fields":{"VAR":{"id":"DQRH|7)}~FZVmJT[WOX]"}}}}},"next":{"block":{"type":"controls_if","id":"y^TXK]7o#wl8^~$ET69y","inputs":{"IF0":{"block":{"type":"button_justPressed","id":"ZBxPkETiN*.)tOE2SMht","fields":{"BUTTON":"actionJustPressed"}}},"DO0":{"block":{"type":"variables_set","id":"/8_zbRRx[|?{vb)|9Etx","fields":{"VAR":{"id":"DQRH|7)}~FZVmJT[WOX]"}},"inputs":{"VALUE":{"block":{"type":"logic_ternary","id":"2;idn)z;F^zM?~o+CcGt","inputs":{"IF":{"block":{"type":"get_sprite_orien","id":"vQA|jX`zR.mvdf)C#x]:","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"},"ATTR":"mirrorX"}}},"THEN":{"block":{"type":"math_number","id":"1`JSUO^0ScOBKtKb0+-2","fields":{"NUM":1}}},"ELSE":{"block":{"type":"math_number","id":"#_V8t]CP2oedlj^+F6h?","fields":{"NUM":-1}}}}}}},"next":{"block":{"type":"variables_set","id":"DtfB)noMH;f]}/9=H6Rr","fields":{"VAR":{"id":"?[4~c[u3HW5m^8t}uvcy"}},"inputs":{"VALUE":{"block":{"type":"get_sprite_size","id":"Ph)r`t=(LD9LO0o6imop","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"},"ATTR":"x"}}}},"next":{"block":{"type":"variables_set","id":"d/U-T|.}~TUrVd@GDZ*x","fields":{"VAR":{"id":"]1}?Z$Ct,(2W(!?i#W@f"}},"inputs":{"VALUE":{"block":{"type":"math_arithmetic","id":"]chin=)DOd(EU8~[clFD","fields":{"OP":"ADD"},"inputs":{"A":{"shadow":{"type":"math_number","id":"2|VO43Q5g:~)Lx}I|i/:","fields":{"NUM":1}},"block":{"type":"get_sprite_size","id":"-5E2Jvd~Vs|xNY6OBU3V","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"},"ATTR":"y"}}},"B":{"shadow":{"type":"math_number","id":"Cpw4n{gZ]HSnJ]LojGAx","fields":{"NUM":3}}}}}}}}}}}}}}}}}}}}}},{"type":"procedures_defnoreturn","id":"feoD!U89?WR{JAcDOtu]","x":-868,"y":4351,"icons":{"comment":{"text":"Set up the  player's bullet to start off screen","pinned":false,"height":80,"width":160}},"fields":{"NAME":"setup bullet"},"inputs":{"STACK":{"block":{"type":"variables_set","id":"x!6M8UX.@^ceEkVS-~8:","fields":{"VAR":{"id":"DQRH|7)}~FZVmJT[WOX]"}},"inputs":{"VALUE":{"block":{"type":"math_number","id":"qNnk9TFsH?k8Eo;MhAQn","fields":{"NUM":1}}}},"next":{"block":{"type":"variables_set","id":"Ll-A,,@Ih!ZV0U-,I4*i","fields":{"VAR":{"id":"?[4~c[u3HW5m^8t}uvcy"}},"inputs":{"VALUE":{"block":{"type":"math_number","id":"$Oy|(DPg).}r2wba??8K","fields":{"NUM":-99}}}},"next":{"block":{"type":"variables_set","id":"{YDP%TZ;*1}i#z}Z-Ua=","fields":{"VAR":{"id":"]1}?Z$Ct,(2W(!?i#W@f"}},"inputs":{"VALUE":{"block":{"type":"math_number","id":")Hda39Blou7}=9|8rLr`","fields":{"NUM":-99}}}}}}}}}}}},{"type":"procedures_callnoreturn","id":"9aeCr5sa7=d2c?I|UhSx","x":-867,"y":-323,"extraState":{"name":"setup bullet"},"next":{"block":{"type":"procedures_callnoreturn","id":"e+vIwgu/6pDsI+C;%=4^","extraState":{"name":"setup bird"},"next":{"block":{"type":"procedures_callnoreturn","id":"[3N0SQ$97~4.!J%;_W6p","extraState":{"name":"setup walker"},"next":{"block":{"type":"procedures_callnoreturn","id":"083C]DV:WfGp]BaC1++B","extraState":{"name":"setup kite"},"next":{"block":{"type":"procedures_callnoreturn","id":"+Je{M#9A|v7uBZoP#HyC","extraState":{"name":"setup box"},"next":{"block":{"type":"procedures_callnoreturn","id":"CGmy!X.W^u2O%J4~_k9X","extraState":{"name":"setup line"},"next":{"block":{"type":"setFPS","id":"{d7c_Z.ya2M,!i-.91N!","inputs":{"FPS":{"shadow":{"type":"math_number","id":"L.G`)j0.wQg12Qp,]J4a","fields":{"NUM":60}}}},"next":{"block":{"type":"controls_whileUntil","id":";bWO/96p(C72*Igt}#)T","fields":{"MODE":"WHILE"},"inputs":{"BOOL":{"block":{"type":"logic_boolean","id":"8KljcJ`UqH!Vq5@%!{f=","fields":{"BOOL":"TRUE"}}},"DO":{"block":{"type":"math_change","id":"|i{Q]pF;{vqm@XVDAfU(","fields":{"VAR":{"id":"I.l(x3AK)mRwJRN-n~Ck"}},"inputs":{"DELTA":{"shadow":{"type":"math_number","id":"$/}ZMx]xsQL1IlA3K8^@","fields":{"NUM":1}}}},"next":{"block":{"type":"procedures_callnoreturn","id":"7,J{n$Z~`X_PUlwi^ChH","extraState":{"name":"do line"},"next":{"block":{"type":"controls_if","id":"IITP@;zR7IdYmA,=q1V^","inputs":{"IF0":{"block":{"type":"get_drawn_pixel","id":"18y1-l{$8BDoZErM}A#0","inputs":{"X":{"block":{"type":"variables_get","id":"ch4h#t?gzk:nlHnf36Y.","fields":{"VAR":{"id":"?[4~c[u3HW5m^8t}uvcy"}}}},"Y":{"block":{"type":"variables_get","id":"]wgx5T1+(xxse.A|J05|","fields":{"VAR":{"id":"]1}?Z$Ct,(2W(!?i#W@f"}}}}}}},"DO0":{"block":{"type":"math_change","id":"3*7!~6QY1ha`kPQgw%v=","fields":{"VAR":{"id":"n.[mBZ}0?exqKYg3]FAn"}},"inputs":{"DELTA":{"shadow":{"type":"math_number","id":"2G)PNljT[iqkX[9r/{fT","fields":{"NUM":-1}}}}}}},"next":{"block":{"type":"controls_if","id":"rq?t(Nr1xWvNaEw5k1?4","inputs":{"IF0":{"block":{"type":"logic_compare","id":"O88^_DQb;bfmG)4I8h.o","fields":{"OP":"EQ"},"inputs":{"A":{"block":{"type":"variables_get","id":"a/#LXsv$b9k?WN(N$gd+","fields":{"VAR":{"id":"n.[mBZ}0?exqKYg3]FAn"}}}},"B":{"block":{"type":"math_number","id":"MamYfu!gP|S5q:zi|H.3","fields":{"NUM":0}}}}}},"DO0":{"block":{"type":"print_to_display","id":"en$BNLdCA1GB#,Vgv+ku","inputs":{"VAL":{"block":{"type":"text","id":"4vDF3oOwHL)CV*yw6Z;C","fields":{"TEXT":"YOU WIN!"}}}},"next":{"block":{"type":"wait","id":"(B+q2R}(s{=q#+`jS?Xr","fields":{"SCALE":"sleep"},"inputs":{"TIME":{"shadow":{"type":"math_number","id":"/w6%^+VQv(n,24eg7)2[","fields":{"NUM":3}}}},"next":{"block":{"type":"reset","id":"wTjnD63Ody=M*[)--v8l"}}}}}}},"next":{"block":{"type":"procedures_callnoreturn","id":"ia0cEh.llaPuVb.O.dIy","extraState":{"name":"do border"},"next":{"block":{"type":"procedures_callnoreturn","id":".nbIzj}{-Fy})G}P[XNI","extraState":{"name":"do box"},"next":{"block":{"type":"procedures_callnoreturn","id":"crQ}*8+x}9{F|cW!sgom","extraState":{"name":"do kite"},"next":{"block":{"type":"procedures_callnoreturn","id":"Ta4%kQ49K9uc147=8}wc","extraState":{"name":"do walker"},"next":{"block":{"type":"controls_if","id":"FG|HXk]!6f(6In4$m[4z","inputs":{"IF0":{"block":{"type":"get_drawn_pixel","id":"}Za/xnr)w_)nIhrok7wd","inputs":{"X":{"block":{"type":"variables_get","id":"K~F54djijYr[:{kTAIsL","fields":{"VAR":{"id":"?[4~c[u3HW5m^8t}uvcy"}}}},"Y":{"block":{"type":"variables_get","id":"7(EYtau3M0kZ2|jBKjUf","fields":{"VAR":{"id":"]1}?Z$Ct,(2W(!?i#W@f"}}}}}}},"DO0":{"block":{"type":"variables_set","id":"GWr_#{d6,QQdTr@;lBZ$","fields":{"VAR":{"id":"]1}?Z$Ct,(2W(!?i#W@f"}},"inputs":{"VALUE":{"block":{"type":"math_number","id":"d8E*$85,:Lfu`11.F)NV","fields":{"NUM":-99}}}}}}},"next":{"block":{"type":"controls_if","id":".`g)xcw/WTV]u_yE`Su!","inputs":{"IF0":{"block":{"type":"get_drawn_pixel","id":"SKYU*={)BVi#N@4ja#3K","inputs":{"X":{"block":{"type":"math_arithmetic","id":"QHLS?Ggd1spgkcWRaTPS","fields":{"OP":"ADD"},"inputs":{"A":{"shadow":{"type":"math_number","id":"^}V:4Bt5pRyKf3GAOLam","fields":{"NUM":1}},"block":{"type":"get_sprite_size","id":"e@|]1B$UyT=3R9iECl6_","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"},"ATTR":"x"}}},"B":{"shadow":{"type":"math_number","id":"$1W:ufQX;SYA@jTG..K%","fields":{"NUM":3}}}}}},"Y":{"block":{"type":"math_arithmetic","id":"kM{?qocN`+RA=gwwIOv(","fields":{"OP":"ADD"},"inputs":{"A":{"shadow":{"type":"math_number","id":"^}V:4Bt5pRyKf3GAOLam","fields":{"NUM":1}},"block":{"type":"get_sprite_size","id":"1jP_;JQ8YNAe4iW_XfsV","fields":{"VAR":{"id":"V{eL+Uu^!v-oN3:di_fu"},"ATTR":"y"}}},"B":{"shadow":{"type":"math_number","id":"[^O$AZUG7{G?ouiSR[0a","fields":{"NUM":3}}}}}}}}},"DO0":{"block":{"type":"print_to_display","id":"+O#iupVq-BJ#j^w2P-H,","inputs":{"VAL":{"block":{"type":"text","id":"OH|F)6a!qZ8xY3hFzU`p","fields":{"TEXT":"GAME OVER!"}}}},"next":{"block":{"type":"wait","id":"5E:6)2m;~em`mwP[+SPv","fields":{"SCALE":"sleep"},"inputs":{"TIME":{"shadow":{"type":"math_number","id":"[wXEgTTqokklpqqmscrK","fields":{"NUM":3}}}},"next":{"block":{"type":"reset","id":"`DzK#EWIU^G|2#`XI,#c"}}}}}}},"next":{"block":{"type":"procedures_callnoreturn","id":"R.L1Q_db@r8,FEO^yP/Y","extraState":{"name":"do bird"},"next":{"block":{"type":"procedures_callnoreturn","id":"z*c+BF7.PI?=l(%kN/M@","extraState":{"name":"do bullet"},"next":{"block":{"type":"send_drawn_frame_to_display","id":"Vds4K;d$MmWdyAvLAe8E","next":{"block":{"type":"drawFill","id":"0HJx}SVlwpS$v{zjo=0J","fields":{"COL":"0"}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}]},"variables":[{"name":"kiteDirectionY","id":"CQP[|F6CP;bX1O!7H}dj"},{"name":"counter","id":"I.l(x3AK)mRwJRN-n~Ck"},{"name":"boxX","id":"M2:JuNi|%(hg-D*;kX[("},{"name":"boxY","id":")H}#]R2Va?*JLJ4X0[?f"},{"name":"bulletX","id":"?[4~c[u3HW5m^8t}uvcy"},{"name":"bulletY","id":"]1}?Z$Ct,(2W(!?i#W@f"},{"name":"bulletDirection","id":"DQRH|7)}~FZVmJT[WOX]"},{"name":"lineWidth","id":"n.[mBZ}0?exqKYg3]FAn"},{"name":"kiteDirectionX","id":"{FG/%QL#1-NTW}S$F[j4"},{"name":"kite","id":"3aXk?x36f]s//OcS.=(`","type":"Sprite"},{"name":"walker","id":"3ji2~Vh$Rt8bxaq!*LQJ","type":"Sprite"},{"name":"bird","id":"V{eL+Uu^!v-oN3:di_fu","type":"Sprite"},{"name":"birdMask","id":"tqzNgIxRp/BdM*m?P*z~","type":"Sprite"}]}