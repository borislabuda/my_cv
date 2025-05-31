cv_css = """
    <style>
        .fixed-banner {
            top: 0px;
            left: 0;
            right: 0;
            height: 220px;
            background: linear-gradient(135deg, #f26c3f, #f4a261);
            color: white;
            border-radius: 40px 40px 0px 0px;
            font-size: 18px;
            font-weight: normal;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            align-items: center;
            justify-content: left;
            padding: 40px;
            z-index: 1000;
        }
        .content {
            margin-top: 70px;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        .big-font {
            font-size: 40px !important;
            font-weight: normal;
            line-height: 0.5;
            color: white;
        }
        .tight-font {
            font-weight: normal;
            padding: 0px;
            font-size: 25px !important;
            margin: 0px;
            line-height: 0.5;
        }
        body {
            font-family: ""Helvetica Neue", Helvetica, Arial, sans-serif";
            color: #dimgray;
        }
        hd1 {
            font-family: ""Helvetica Neue", Helvetica, Arial, sans-serif";
            color: #2E8B57;
        }
        hd2 {
            font-family: ""Helvetica Neue", Helvetica, Arial, sans-serif";
        }
        hd3 {
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        .custom-title {
            font-size: 36px;
            color: navy;
            font-weight: bold;
        }
        html, body, [class*="css"]  {
             line-height: 1;
        }
        ul.modern-list {
        list-style: none;
        padding: 0;
        font-size: 15px;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        ul.modern-list li {
            margin: 8px 0;
            padding: 10px 14px;
            border-radius: 12px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            transition: all 0.2s ease-in-out;
        }
        ul.modern-list li:hover {
            background: #e0e4ea;
            transform: translateX(4px);
        }
        p.modern-text {
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        font-size: 16px;
        line-height: 1.6;
        margin-bottom: 1em;
        max-width: 700px;
        text-align: justify;
        }
        .contact-style a {
            all: unset;
            cursor: pointer;
            font-weight: 500;
            line-height: 1.5;
            color: white;
        }
        .contact-style a:hover {
            color: #f26c3f;
            text-decoration: underline;
        }
        .vis-timeline {
            font-family: 'Segoe UI', sans-serif !important;
            font-size: 14px;
        }
        .skill-badge {
            display: inline-block;
            border: 0.5px solid silver;
            border-radius: 20px;
            padding: 5px 8px;
            margin: 14px 6px 14px 0;
            font-size: 0.9em;
            font-weight: 500;
        }
        
        .timeline-step {
        border: 1px solid #e3e3e3;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        width: 700px;
        margin: 0px 0px 20px 0px;
        }

        .timeline-circle {
        position: absolute;
        text-align: center;
        padding: 10px 20px;
        top: -20px;
        left: -20px;
        width: auto;
        height: 30px;
        border-radius: 45%;
        background: #f26c3f;
        color: white;
        line-height: 15px;
        margin: 0 auto 10px;
        font-weight: bold;
        font-style: italic;
        }

        svg {
        position: absolute;
        top: 20px;
        left: 100px;
        width: 100%;
        height: 2px;
        z-index: -1;
        }
        
        .step-container {
        display: flex;
        flex-direction: column;
        gap: 20px;
        max-width: 300px;
        margin: auto;
        margin-top: 50px;
        }

        .step {
        opacity: 0;
        transform: translateY(20px);
        animation: fadeIn 0.6s forwards;
        padding: 15px;  
        border-left: 5px solid #f26c3f;
        border-radius: 5px;
        margin: 0px 0px 40px 0px;
        }

        .step:nth-child(1) { animation-delay: 0s; }
        .step:nth-child(2) { animation-delay: 0.4s; }
        .step:nth-child(3) { animation-delay: 0.8s; }
        .step:nth-child(4) { animation-delay: 1.2s; }

        @keyframes fadeIn {
        to {
            opacity: 1;
            transform: translateY(0);
        }
}
    </style>
"""