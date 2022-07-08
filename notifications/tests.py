from django.test import TestCase

# Create your tests here.
const listemojipost=[{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'hạnh phúc'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yd/r/SbLxX4jljCS.png",
name:'có phúc'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yB/r/jnaR01aXOKF.png",
name:'được yêu'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'buồn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yB/r/jnaR01aXOKF.png",
name:'đáng yêu'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/8HG4ArhYqqm.png",
name:'biết ơn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yl/r/GTVH05GEVXD.png",
name:'hào hứng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yB/r/jnaR01aXOKF.png",
name:'đang yêu'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yL/r/D5AOH5Rt9K8.png",
name:'điên'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yG/r/84_AfuO7-Sk.png",
name:'cảm kích'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yl/r/-Oz0Mt1ODxc.png",
name:'sung sướng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y2/r/7EP_wi4-K-2.png",
name:'tuyệt vời'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8XwN6UuxTMh.png",
name:'khờ khạo'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yN/r/9Te0n4rkLpK.png",
name:'vui vẻ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'tuyệt vời'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yz/r/TLm2OJzKubg.png",
name:'tuyệt'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'thú vị'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/zhi6jtmTu3-.png",
name:'thư giãn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/zhi6jtmTu3-.png",
name:'tích cực'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/zhi6jtmTu3-.png",
name:'thoải mái'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yJ/r/-QMIhlwCYdo.png",
name:'đầy hy vọng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yl/r/-Oz0Mt1ODxc.png",
name:'hân hoan'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/XUxJKsLyvQ4.png",
name:'mệt mỏi'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yA/r/vqNLyDJn0LW.png",
name:'có động lực'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yA/r/vqNLyDJn0LW.png",
name:'tự hào'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yw/r/2OPxnmzWJKZ.png",
name:'cô đơn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yY/r/5AnCiyS_9cd.png",
name:'chu đáo'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/VvIMJyzy948.png",
name:'OK'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yf/r/oMOT1mZQEl_.png",
name:'hoài niệm'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/USUgQ58uDx-.png",
name:'giận dữ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yr/r/1Se99YgIwLT.png",
name:'ốm yếu'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y2/r/7EP_wi4-K-2.png",
name:'hài lòng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yX/r/gXjnOZhx3oz.png",
name:'kiệt sức'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yi/r/02a2H2B9Ec7.png",
name:'xúc động'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yA/r/vqNLyDJn0LW.png",
name:'tự tin'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/8HG4ArhYqqm.png",
name:'rất tuyệt'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yA/r/vqNLyDJn0LW.png",
name:'tươi mới'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/TTm3hch87J7.png",
name:'quyết đoán'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yR/r/qwkICZ8qkDL.png",
name:'kiệt sức'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/USUgQ58uDx-.png",
name:'bực mình'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/Zq_QZwVGoqX.png",
name:'vui vẻ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yY/r/Doy76OT15hh.png",
name:'may mắn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/l0h4FhPauYc.png",
name:'đau khổ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yf/r/l61F6_7qt8r.png",
name:'buồn tẻ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/XUxJKsLyvQ4.png",
name:'buồn ngủ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y2/r/7EP_wi4-K-2.png",
name:'tràn đầy sinh lực'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yB/r/gTtDa0D7Kt9.png",
name:'đói'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yA/r/vqNLyDJn0LW.png",
name:'chuyên nghiệp'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yZ/r/A6RS5poIYbi.png",
name:'đau đớn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/zhi6jtmTu3-.png",
name:'thanh thản'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'thất vọng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yA/r/vqNLyDJn0LW.png",
name:'lạc quan'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yf/r/kb_BaCTS07b.png",
name:'lạnh'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yW/r/XXa65GQHGQp.png",
name:'dễ thương'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yz/r/TLm2OJzKubg.png",
name:'tuyệt cú mèo'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/8HG4ArhYqqm.png",
name:'thật tuyệt'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/2jDz-deNGrq.png",
name:'hối tiếc'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yD/r/h-6zozwrF3r.png",
name:'thật giỏi'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yd/r/Xs7vOCLE3qu.png",
name:'lo lắng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yL/r/nSF2F851epw.png",
name:'vui nhộn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'tồi tệ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yw/r/2OPxnmzWJKZ.png",
name:'xuống tinh thần'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/ya/r/UGwrAPxJM9s.png",
name:'đầy cảm hứng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'hài lòng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yA/r/vqNLyDJn0LW.png",
name:'phấn khích'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/zhi6jtmTu3-.png",
name:'bình tĩnh'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/LbV-kw7aU4K.png",
name:'bối rối'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8XwN6UuxTMh.png",
name:'ngớ ngẩn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yG/r/84_AfuO7-Sk.png",
name:'trống vắng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'tốt'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/ya/r/EsVCKErmClv.png",
name:'mỉa mai'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'cô đơn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yD/r/h-6zozwrF3r.png",
name:'mạnh mẽ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yJ/r/um_yQgR5G3L.png",
name:'lo lắng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yl/r/GTVH05GEVXD.png",
name:'đặc biệt'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yw/r/2OPxnmzWJKZ.png",
name:'chán nản'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yG/r/Ln8Jt7O9E6n.png",
name:'vui vẻ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/ya/r/UGwrAPxJM9s.png",
name:'tò mò'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'ủ dột'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'được chào đón'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yI/r/IUAvWtouCkM.png",
name:'đau khổ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/_TZbNRGVjQo.png",
name:'xinh đẹp'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yl/r/GTVH05GEVXD.png",
name:'tuyệt vời'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yi/r/9VzoHiB2sW3.png",
name:'cáu'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'căng thẳng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/KND4MZeohIT.png",
name:'thiếu vắng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/ye/r/8XwN6UuxTMh.png",
name:'quá siêu'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yU/r/AL9NGhl006C.png",
name:'tinh quái'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y2/r/7EP_wi4-K-2.png",
name:'kinh ngạc'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/USUgQ58uDx-.png",
name:'tức giận'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yZ/r/A6RS5poIYbi.png",
name:'buồn chán'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y2/r/O0XxUXwnqpq.png",
name:'bối rối'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y3/r/9XdcKFX2O43.png",
name:'giận dữ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/USUgQ58uDx-.png",
name:'phẫn nộ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'mới mẻ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yU/r/AL9NGhl006C.png",
name:'thành công'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yv/r/A360uqNMpcP.png",
name:'ngạc nhiên'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y2/r/O0XxUXwnqpq.png",
name:'bối rối'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'nản lòng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yc/r/DPFf568WJRf.png",
name:'tẻ nhạt'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yW/r/XXa65GQHGQp.png",
name:'xinh xắn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/Zq_QZwVGoqX.png",
name:'khá hơn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'tội lỗi'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yx/r/vTeCt9V__aX.png",
name:'an toàn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'tự do'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/LbV-kw7aU4K.png",
name:'hoang mang'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yr/r/3fCnxVGYwTa.png",
name:'già nua'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/zhi6jtmTu3-.png",
name:'lười biếng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'tồi tệ hơn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/USUgQ58uDx-.png",
name:'khủng khiếp'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'thoải mái'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/XUxJKsLyvQ4.png",
name:'ngốc nghếch'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/2jDz-deNGrq.png",
name:'hổ thẹn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yw/r/2OPxnmzWJKZ.png",
name:'kinh khủng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/XUxJKsLyvQ4.png",
name:'đang ngủ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'khỏe'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'nhanh nhẹn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yW/r/XXa65GQHGQp.png",
name:'ngại ngùng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yF/r/sStyNmFW9xC.png",
name:'gay go'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yv/r/Bu57dnmNtdt.png",
name:'kỳ lạ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'như con người'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yZ/r/A6RS5poIYbi.png",
name:'bị tổn thương'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yQ/r/DLgydu3LLkn.png",
name:'khủng khiếp'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/Zq_QZwVGoqX.png",
name:'bình thường'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yn/r/vm_19q6gADx.png",
name:'ấm áp'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yc/r/DPFf568WJRf.png",
name:'không an toàn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/XUxJKsLyvQ4.png",
name:'yếu'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/Zq_QZwVGoqX.png",
name:'tốt đẹp'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/Zq_QZwVGoqX.png",
name:'khỏe'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/XUxJKsLyvQ4.png",
name:'ngu ngốc'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'dễ chịu'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yU/r/AL9NGhl006C.png",
name:'quan trọng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yQ/r/DLgydu3LLkn.png",
name:'dở tệ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'không thoải mái'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/XUxJKsLyvQ4.png",
name:'chẳng được tích sự gì'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yA/r/vqNLyDJn0LW.png",
name:'sẵn sàng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yL/r/nSF2F851epw.png",
name:'khác biệt'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'bất lực'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yc/r/DPFf568WJRf.png",
name:'hèn nhát'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yJ/r/rJtHLlG4Fm0.png",
name:'say'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yB/r/OQv1OHMN3kt.png",
name:'choáng ngợp'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'vô vọng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'toàn vẹn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/USUgQ58uDx-.png",
name:'khổ sở'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/USUgQ58uDx-.png",
name:'tức điên'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'thâm trầm'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yQ/r/DLgydu3LLkn.png",
name:'kinh tởm'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'bồn chồn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y2/r/JKEqLFZ3qRw.png",
name:'buồn bã'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'được yêu mến'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/Zq_QZwVGoqX.png",
name:'vinh dự'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'thư thái'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yQ/r/DLgydu3LLkn.png",
name:'choáng váng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yx/r/vTeCt9V__aX.png",
name:'an toàn'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yS/r/O_9mSdIbFWO.png",
name:'trống rỗng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yT/r/a4VuRwFNsgi.png",
name:'bẩn thỉu,li ari"https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/XUxJKsLyvQ4.png",
name:'không quan trọng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/8HG4ArhYqqm.png",
name:'vĩ đại'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yA/r/Dxg7LlsBAFd.png",
name:'sợ hãi'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y3/r/9XdcKFX2O43.png",
name:'ghen tuông'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yZ/r/A6RS5poIYbi.png",
name:'đau nhức'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/XUxJKsLyvQ4.png",
name:'không ai cần mình'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yA/r/vqNLyDJn0LW.png",
name:'được coi trọng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yK/r/Iu45bu7idw4.png",
name:'đầy đủ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yc/r/DPFf568WJRf.png",
name:'bận bịu'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yY/r/FOXyv5kMlip.png",
name:'nhỏ bé'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/l0h4FhPauYc.png",
name:'không được yêu'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yw/r/2OPxnmzWJKZ.png",
name:'vô dụng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yU/r/AL9NGhl006C.png",
name:'đủ điều kiện'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yF/r/Svm03GM3eXC.png",
name:'thờ ơ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yf/r/l61F6_7qt8r.png",
name:'nôn nóng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yC/r/bIWUEPoNY9W.png",
name:'được ưu tiên'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yD/r/VU_ofChVPBA.png",
name:'mắc lừa'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yQ/r/DLgydu3LLkn.png",
name:'khát'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yr/r/1Se99YgIwLT.png",
name:'gớm ghiếc'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'khó chịu'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/USUgQ58uDx-.png",
name:'phản cảm'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yf/r/kb_BaCTS07b.png",
name:'vô cảm'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yl/r/GTVH05GEVXD.png",
name:'hoàn hảo'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yY/r/5AnCiyS_9cd.png",
name:'bị thách thức'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yR/r/qwkICZ8qkDL.png",
name:'bị đe dọa'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yf/r/DxnxXXkYiSX.png",
name:'yên lòng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yX/r/gXjnOZhx3oz.png",
name:'bế tắc'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yv/r/Bu57dnmNtdt.png",
name:'lạ lùng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yW/r/XXa65GQHGQp.png",
name:'xấu hổ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/zhi6jtmTu3-.png",
name:'đầy năng lượng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yL/r/xOjVJ2q9bEF.png",
name:'lanh lợi'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'bị lừa'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y0/r/MqU4w6kG_-T.png",
name:'bị phản bội'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yR/r/qwkICZ8qkDL.png",
name:'lo âu'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/USUgQ58uDx-.png",
name:'tức tối'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y9/r/USUgQ58uDx-.png",
name:'xấu xa'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/XUxJKsLyvQ4.png",
name:'bị thờ ơ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yj/r/XUxJKsLyvQ4.png",
name:'hối hận'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yl/r/-Oz0Mt1ODxc.png",
name:'khỏe mạnh'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yb/r/Zq_QZwVGoqX.png",
name:'hào phóng'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yD/r/6Nc6PBM5UGj.png",
name:'giàu có'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yB/r/OQv1OHMN3kt.png",
name:'lo sợ'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/y6/r/r1VAo2m4J3d.png",
name:'hết tiền'},{src:"https://static.xx.fbcdn.net/rsrc.php/v3/yq/r/LbV-kw7aU4K.png",
name:'vô hình'}]