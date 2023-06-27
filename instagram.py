from flask import Flask,render_template,request,redirect,make_response,flash

from database import db
db.create_all()
from database import Users,post,id,like,comment,send
from database import app
import os
path= './static/'
@app.route('/',methods=['GET','POST'])
def index():
    dir_list = os.listdir(path)
    return render_template('first.html',result_c=comment.query.all(),likee=like.query.all(),lenlike=len(like.query.all()),dir_list=dir_list,id=id.query.all(), post=post.query.all(), user=request.cookies.get("user"))
@app.route('/profile',methods=['GET','POST'])
def profile():
    if request.cookies.get("user"):

        return render_template('profile.html',lenpost=post.query.all() ,user=request.cookies.get("user"))
    else:
        return redirect('/login')
@app.route('/searchuser',methods=['GET','POST'])
def searchuser():
    if request.cookies.get("user"):
        suser = request.form.get('suser')
        print(suser)
        rest = Users.query.filter_by(username=suser)
        return render_template('searchuser.html',result_users=rest,user=request.cookies.get("user"))
    else:
        return redirect('/login')

@app.route('/"/like/<int:post_id>"',methods=['GET','POST'])
def like_add(post_id):
    
    admin15= like(user_like=request.cookies.get("user"),post_like=post_id)
    print(admin15)
    db.session.add(admin15)
    db.session.commit()
    return redirect('/')
@app.route('/"/add_comment/<int:post_id>"',methods=['GET','POST'])
def add_comment(post_id):
    comment1 = request.form.get('comment1')
    admin16= comment(user_comment=request.cookies.get("user"),text_comment=comment1,post_comment=post_id)
    print(admin16)
    db.session.add(admin16)
    db.session.commit()
    return redirect('/')
@app.route('/"/result_comment/<int:post_id>"',methods=['GET','POST'])
def result_comment(post_id):
    recome = comment.query.filter_by(post_comment=post_id)
    return render_template('result.html',user=request.cookies.get("user"),com=recome,com1=len(comment.query.all()))

@app.route('/post', methods=['GET', 'POST'])
def addpost():
    if request.cookies.get("user"):
        if request.method == 'POST':
            pic = request.files.get('pic')
            text = request.form.get('text')
            flash("پست اضافه شد", "info")
            adad=id.query.all()[0].id_picture
            adad=int(adad)+1
            id.query.all()[0].id_picture=str(adad)

            db.session.commit()
            pic.save(os.path.join(path, request.cookies.get("user")+str(adad)+ ".jpg"))
            print(request.cookies.get("user")+str(adad)+ ".jpg")
            admin1= post(text=text,static_pic="./static/"+request.cookies.get("user")+str(adad)+ ".jpg")
            print(admin1)
            db.session.add(admin1)
            db.session.commit()
            return redirect('/post',)
        else:
            return render_template('post.html',user=request.cookies.get("user"))
    else:
        return redirect('/login')
@app.route('/change_image',methods=['GET','POST'])
def change_image():
    file1 = request.files.get('image')

    file1.save(os.path.join(path, request.cookies.get("user") + ".jpg"))

    return redirect('/profile')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user = request.form.get('user')
        pass1 = request.form.get('pass')
        found=False
        for u in range(len(Users.query.all())):
            if user==Users.query.all()[u].username and pass1==Users.query.all()[u].password:
                flash("کاربر وارد شد", "success")
                response=make_response(redirect('/'))
                response.set_cookie("user",user)
                found = True
                return response
        if found==False:
                flash("ایمیل یا رمز عبور اشتباه است", "danger")
                return render_template('login.html',user=request.cookies.get("in_email"))
    return render_template('login.html',user=request.cookies.get("user"))
@app.route('/register',methods=['POST','GET'])
def Register():
    if request.method=='POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        if password==re_password and len(password)==8:
            flash("کاربر ثبت نام شد پروفایل کاربری خود را کامل کنید", "info")
            admin=Users(username=username,password=password,email=email)
            db.session.add(admin)
            db.session.commit()
            return redirect('/login')
        else:
            flash("رمز عبور با تکرار آن هم خوانی ندارد یا تعداد رمز عبور کم تر از 8 میباشد ", "danger")
            return redirect('/login')
    else:
        return render_template('Register.html',user=request.cookies.get("user"))
@app.errorhandler(404)
def showerror(error):
    return render_template("error.html"),404
@app.route("/logout")
def logout():
    flash("کاربر خارج شد", "danger")
    response = make_response(redirect('/login'))
    response.delete_cookie("user")
    return response
@app.route('/send_m',methods=['POST','GET'])
def send_m():
    if request.cookies.get("user"):
        if request.method == 'POST':
            user_receive1 = request.form.get('user_receive1')
            text_send1 = request.form.get('text_send1')
            flash("پیغام ارسال شد", "success")
            admin2 = send(user_send=request.cookies.get("user"), text_send=text_send1, user_receive=user_receive1)
            db.session.add(admin2)
            db.session.commit()
            print(admin2)
            return redirect('/')
        return render_template('send_m.html', user=request.cookies.get("user"))
    else:
        return redirect('/login')
@app.route('/inbox', methods=['POST', 'GET'])
def inbox():
    if request.cookies.get("user"):
        in1=send.query.filter_by(user_send=request.cookies.get("user"))
        print(in1)
        return render_template('inbox.html', user=request.cookies.get("user"),in1=in1)
    else:
        return redirect('/login')
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)