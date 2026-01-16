import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load 20 tasks with UTF-8 encoding / 以UTF-8编码加载20道题目
with open('tasks.json', 'r', encoding='utf-8') as f:
    tasks = json.load(f)

@app.route('/get_task', methods=['GET'])
def get_task():
    idx = int(request.args.get('idx', 0)) % len(tasks)
    return jsonify(tasks[idx])

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    task_id = data.get("id")
    answer = data.get("answer", "").lower()
    
    current_task = next((t for t in tasks if t["id"] == task_id), None)
    if not current_task:
        return jsonify({"score": 0, "feedback": "Task not found / 任务未找到"}), 404

    # Scoring logic / 评分逻辑
    keywords = [k.lower() for k in current_task["key_points"]]
    matched = [kp for kp in keywords if kp in answer]
    score = int((len(matched) / len(keywords)) * 100)

    return jsonify({
        "score": score,
        "details": f"Matched / 匹配项: {', '.join(matched)}",
        "feedback": "Bilingual Evaluation Complete / 中英双语评估完成"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)