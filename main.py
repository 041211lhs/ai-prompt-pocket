# main.py
# 현서의 AI Prompt Pocket

CATEGORIES = ["국어 수업", "경제·학업", "취업·자소서", "AI·자동화", "글쓰기·문서"]

prompts = [
    {
        "title": "국어 지문 기반 문제 생성",
        "content": """너는 중·고등학교 국어 문제를 제작하는 전문 교사야.

아래에 제공하는 국어 지문을 분석한 후 학생의 독해력과 사고력을 평가할 수 있는 문제를 만들어줘.

다음 조건을 지켜줘.
1. 객관식 5문제, 5지선다형으로 제작
2. 지문의 핵심 내용을 정확하게 반영
3. 내용 확인 문제와 추론·사고력 문제를 적절히 구성
4. 지나치게 쉬운 문제만 만들지 않기
5. 각 문제마다 정답과 해설 제공
6. 각 선택지가 왜 맞거나 틀렸는지 설명

[지문]
{지문 입력}""",
        "category": "국어 수업",
        "favorite": False,
    },
    {
        "title": "난이도별 국어 문제 생성",
        "content": """다음 국어 지문을 바탕으로 난이도별 문제를 만들어줘.

난이도를 하·중·상으로 나누고 각 난이도별로 2문제씩 총 6문제를 제작해줘.

하: 지문의 명시적인 내용을 확인하는 문제
중: 지문의 내용을 종합하거나 문맥을 이해해야 하는 문제
상: 추론, 비판적 사고, 표현의 의미 등을 묻는 문제

모든 문제는 5지선다형으로 만들고 정답과 해설을 함께 제공해줘.

[지문]
{지문 입력}""",
        "category": "국어 수업",
        "favorite": False,
    },
    {
        "title": "경제 뉴스 요약",
        "content": """다음 경제 뉴스를 경제학과 학생이 이해하기 쉽게 정리해줘.

다음 순서로 작성해줘.

1. 핵심 내용 5줄 요약
2. 주요 경제 개념
3. 사건이 발생한 원인
4. 경제·시장에 미칠 수 있는 영향
5. 관련 산업이나 기업
6. 경제학과 학생이 알아두면 좋은 핵심 키워드 5개

기사에 명확하게 제시되지 않은 내용은 사실처럼 단정하지 말고,
기사의 사실과 해석을 구분해서 작성해줘.

[뉴스]
{뉴스 내용}""",
        "category": "경제·학업",
        "favorite": True,
    },
    {
        "title": "경제학 과제 자료 정리",
        "content": """다음 자료를 경제학 과제를 작성하기 위한 형태로 정리해줘.

1. 연구 주제
2. 문제 제기
3. 핵심 주장
4. 관련 경제학 개념
5. 활용할 수 있는 데이터
6. 분석 방법
7. 예상되는 결과
8. 연구의 한계
9. 추가로 조사해야 할 내용

자료에 없는 사실을 임의로 만들어내지 말고,
추가 조사가 필요한 부분은 별도로 표시해줘.

[자료]
{자료 입력}""",
        "category": "경제·학업",
        "favorite": False,
    },
    {
        "title": "자소서 문항 분석",
        "content": """다음 기업의 자기소개서 문항을 분석해줘.

1. 기업이 이 문항을 통해 확인하려는 역량
2. 문항의 핵심 키워드
3. 반드시 포함하면 좋은 내용
4. 활용하기 좋은 경험
5. 피하면 좋은 내용
6. 추천하는 글의 구조
7. 내가 답변을 작성할 때 주의할 점

단순히 문장을 작성하기보다 먼저 문항의 의도를 분석해줘.

[기업명]
{기업명}

[자기소개서 문항]
{문항}

[내 경험]
{경험 목록}""",
        "category": "취업·자소서",
        "favorite": True,
    },
    {
        "title": "자소서 경험 소재 발굴",
        "content": """내가 제공하는 경험 목록을 분석해서 자기소개서에 활용하기 좋은 경험을 찾아줘.

각 경험에 대해 다음 내용을 정리해줘.

1. 경험의 핵심 내용
2. 드러나는 역량
3. 활용하기 좋은 자기소개서 문항
4. 강조하면 좋은 행동
5. 강조하면 좋은 결과
6. 다른 경험과 중복되는 부분

내가 제공하지 않은 경험이나 성과를 임의로 만들어내지 마.

[내 경험 목록]
{경험 입력}""",
        "category": "취업·자소서",
        "favorite": False,
    },
    {
        "title": "뉴스레터 핵심 요약",
        "content": """다음 뉴스레터를 읽고 경제학과 학생이 빠르게 확인할 수 있도록 요약해줘.

다음 형식으로 작성해줘.

[오늘의 핵심 뉴스]
- 가장 중요한 뉴스 3개

[경제 영향]
- 금리
- 환율
- 물가
- 증시
- 산업

[핵심 경제 개념]
- 뉴스와 관련된 경제 개념 설명

[한 줄 정리]
- 오늘 뉴스에서 가장 중요한 흐름을 한 문장으로 정리

확인되지 않은 내용은 추측해서 작성하지 마.

[뉴스레터]
{뉴스레터 내용}""",
        "category": "AI·자동화",
        "favorite": False,
    },
    {
        "title": "긴 자료 핵심 정리",
        "content": """다음 자료를 읽고 핵심 내용만 정리해줘.

다음 순서로 작성해줘.

1. 전체 내용 5줄 요약
2. 핵심 주장 3개
3. 중요한 숫자와 통계
4. 중요한 개념
5. 반드시 기억해야 할 내용
6. 추가로 확인해야 할 내용

원문에 없는 정보는 추가하지 말고,
내용이 불확실한 경우 불확실하다고 표시해줘.

[자료]
{자료 입력}""",
        "category": "AI·자동화",
        "favorite": False,
    },
    {
        "title": "이메일 작성 도우미",
        "content": """다음 상황을 바탕으로 교수님이나 기관 담당자에게 보낼
공손하고 자연스러운 이메일을 작성해줘.

조건:
1. 핵심 요청이 명확하게 드러나도록 작성
2. 지나치게 딱딱한 표현은 피하기
3. 불필요하게 길게 작성하지 않기
4. 대학생이 실제로 작성한 것처럼 자연스럽게 작성
5. 제목도 함께 작성

[상황]
{상황 입력}""",
        "category": "글쓰기·문서",
        "favorite": True,
    },
    {
        "title": "보고서 문장 다듬기",
        "content": """다음 내용을 대학생의 학술 보고서에 적합한 문체로 다듬어줘.

조건:
1. 원래 의미와 주장은 유지
2. 근거 없는 내용을 추가하지 않기
3. 지나치게 어려운 표현은 사용하지 않기
4. 문장 간 논리적 연결을 자연스럽게 만들기
5. 반복되는 표현 제거
6. AI가 작성한 것처럼 지나치게 매끄러운 표현은 피하기

먼저 수정이 필요한 부분을 간단히 설명한 후 최종 수정본을 작성해줘.

[원문]
{내용 입력}""",
        "category": "글쓰기·문서",
        "favorite": False,
    },
]


def show_menu():
    print("\n=== 현서의 AI Prompt Pocket ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input("제목: ").strip()
    while title == "":
        title = input("제목을 입력해주세요: ").strip()

    content = input("내용: ").strip()
    while content == "":
        content = input("내용을 입력해주세요: ").strip()

    print("\n카테고리 선택:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")
    print(f"{len(CATEGORIES) + 1}) 직접 입력")

    cat_choice = input("선택: ").strip()
    if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(CATEGORIES):
        category = CATEGORIES[int(cat_choice) - 1]
    else:
        category = input("카테고리명을 입력해주세요: ").strip()
        if category == "":
            category = "기타"

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    })
    print("\n프롬프트가 추가되었습니다!")


def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, 1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star}")
    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")
    choice = input("선택: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES)):
        print("잘못된 번호입니다.")
        return
    selected = CATEGORIES[int(choice) - 1]
    filtered = [p for p in prompts if p["category"] == selected]

    print(f"\n[{selected}] 카테고리 프롬프트:")
    if not filtered:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return
    for i, p in enumerate(filtered, 1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']}{star}")
    print(f"\n총 {len(filtered)}개의 프롬프트")


def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip()
    results = [p for p in prompts if keyword in p["title"] or keyword in p["content"]]

    print("\n검색 결과:")
    if not results:
        print("검색 결과가 없습니다.")
        return
    for i, p in enumerate(results, 1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star}")
    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")

def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    show_list()
    choice = input("\n번호 입력: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(prompts)):
        print("잘못된 번호입니다.")
        return
    p = prompts[int(choice) - 1]
    star = "⭐" if p["favorite"] else "즐겨찾기 안 함"
    print("\n" + "─" * 30)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print("─" * 30)
    print("내용:")
    print(p["content"])
    print("─" * 30)


def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")
    show_list()
    choice = input("\n프롬프트 번호 입력: ").strip()
    if not (choice.isdigit() and 1 <= int(choice) <= len(prompts)):
        print("잘못된 번호입니다.")
        return
    p = prompts[int(choice) - 1]
    p["favorite"] = not p["favorite"]
    status = "추가" if p["favorite"] else "해제"
    print(f"\n'{p['title']}' 프롬프트를 즐겨찾기에서 {status}했습니다!")


def show_favorites():
    print("(준비 중)")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 번호입니다. 다시 입력해주세요.")


if __name__ == "__main__":
    main()