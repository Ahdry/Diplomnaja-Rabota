from flask import Flask, render_template, request, redirect, url_for, flash
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на свой секретный ключ

# Список для хранения зарегистрированных пользователей
registered_users = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            num_users = int(request.form['num_users'])
            if num_users <= 0:
                flash('Количество пользователей должно быть положительным!')
                return redirect(url_for('index'))

            start_time = time.time()
            for i in range(num_users):
                username = f'User{i + 1}'
                registered_users.append(username)
            end_time = time.time()

            elapsed_time = end_time - start_time
            flash(f'Зарегистрировано {num_users} пользователей за {elapsed_time:.2f} секунд!')
            return redirect(url_for('index'))
        except ValueError:
            flash('Пожалуйста, введите корректное число.')
            return redirect(url_for('index'))

    return render_template('index.html', registered_users=registered_users)


if __name__ == '__main__':
    app.run(debug=True)