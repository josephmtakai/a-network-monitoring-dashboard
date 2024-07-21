from flask import render_template, jsonify
from app import app, socketio
import psutil
import json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/network-stats')
def network_stats():
    # Example stats, replace with actual data gathering
    stats = {
        'bytes_sent': psutil.net_io_counters().bytes_sent,
        'bytes_recv': psutil.net_io_counters().bytes_recv,
        'packets_sent': psutil.net_io_counters().packets_sent,
        'packets_recv': psutil.net_io_counters().packets_recv
    }
    return jsonify(stats)
