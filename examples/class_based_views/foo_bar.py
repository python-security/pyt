# ipdb> class_definition.name
# 'Foo'
class Foo():
    def bar(evil_param):
        command = 'echo ' + evil_param + ' >> ' + 'menu.txt'

        subprocess.call(command, shell=True)

        with open('menu.txt','r') as f:
            menu = f.read()

        return render_template('command_injection.html', menu=menu)


def menu(param):
    command = 'echo ' + param + ' >> ' + 'menu.txt'

    subprocess.call(command, shell=True)

    with open('menu.txt','r') as f:
        menu = f.read()

    return render_template('command_injection.html', menu=menu)
