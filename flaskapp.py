from flask import Flask, render_template, url_for, request, redirect, flash
import amof

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

def render(page, *args, **kwargs):
    '''Simple page rendering function with Exception handling'''
    try:
        return render_template(page, *args, **kwargs)
    except Exception as e:
        return str(e)


@app.route('/')
def home():  
    page = 'home.html'
    return render(page)


@app.route('/about/')
def about():
    page = 'about.html'
    return render(page)

@app.route('/faq/')
def faq():
    page = 'faq.html'
    return render(page)


@app.route('/amof/')
def form():
    page = 'amof.html'
    placeholder = "Paste here..."
    message = "Waithing for input..."
    return render(page, message=message, output=False)

@app.route('/amof/', methods=['POST'])
def parse_input_sequence():
    page = 'amof.html'
    raw_sequence = request.form['raw_sequence']
    
    placeholder = raw_sequence
    parsed_sequence = amof.auto_parse(raw_sequence)
    
    if parsed_sequence:
        message  = ">>> Input parsed correctly: "
        num_seq = len(parsed_sequence)
        if num_seq > 1:
            message += "{} sequences found.".format(num_seq)
        else:
            message += "{} sequence found.".format(num_seq)
        
        raw_sequence = ''
        for id_, sequence in parsed_sequence.items(): #auto_parse() return an OrderedDict()
            raw_sequence += '{}\n{}\n\n'.format(id_,sequence)

        job_output  = amof.simple_finder(parsed_sequence, motif_length=4, min_repetition=3)

    else:
        message = "Error while parsing the sequence/s."
        job_output = False

    return render(page, message=message, output=job_output, raw_sequence=raw_sequence)



if __name__ == "__main__":
	app.run(debug=True)#, host='0.0.0.0', port=8080, passthrough_errors=True)








