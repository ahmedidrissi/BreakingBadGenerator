from website import create_app
import os
print(os.getcwd())

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
