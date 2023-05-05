from manim import *
from manim_slides import Slide


class CreateCircle(Slide):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))


class Intro(Slide):
    """
    풀이 개요
    문제 소개
    의도된 풀이
    """

    def construct(self):
        # <Title>
        title = Group(
            Text("미적분을 활용한").scale(1.5),
            Text("확률과 통계 문제 풀이").scale(1.5),
            Text("30301 김건우").scale(0.8),
        ).arrange_in_grid(
            col_alignments="c",
            row_alignments="ccc",
            row_heights=[None, None, 1.5],
            flow_order="dr",
        )
        self.add(title)
        self.wait()
        self.next_slide()

        # <Overview>
        self.clear()

        overview_text = Text("Overview").scale(1).center().shift(UP * 3)

        overview_rectangle_style = (WHITE, 2.5, 4.5)
        overview_imgs = (
            Group(
                Rectangle(*overview_rectangle_style).add(
                    Tex(
                        r"0 \cdot 0 + 1 \cdot 8 + 2 \cdot 0 \rightarrow {_8C_0 \cdot _8C_8 \cdot _0C_0} \\ "
                        r"0 \cdot 1 + 1 \cdot 6 + 2 \cdot 1 \rightarrow {_8C_1 \cdot _7C_6 \cdot _1C_1} \\ "
                        r"0 \cdot 2 + 1 \cdot 4 + 2 \cdot 2 \rightarrow {_8C_2 \cdot _6C_4 \cdot _2C_2} \\ "
                        r"\vdots",
                        tex_environment="gather*",
                    ).scale(0.5)
                ),
                Rectangle(*overview_rectangle_style).add(
                    Tex(
                        r"&f(x) = (1+x+x^2)^8 \\ "
                        r"=& \; a_0 + a_1 \cdot x + a_2 \cdot x^2 + \cdots  \\ "
                        r"&+ a_8 \cdot x^8 + \cdots + a_{16} \cdot x^{16}",
                        tex_environment="align*",
                    ).scale(0.65)
                ),
                Rectangle(*overview_rectangle_style).add(
                    Tex(
                        r"a_8 =& {1 \over n}{\sum^{n-1}_{k=0} f(e^{2 k \pi i k \over n})e^{- 8 \cdot {2 k \pi i k \over n}}} \\"
                        r"=& {1 \over n}{\sum^{n-1}_{k=0} (1 + 2\cos{2 k \pi \over n})^8}",
                        tex_environment="align*",
                    ).scale(0.6)
                ),
                Rectangle(*overview_rectangle_style).add(
                    Tex(
                        r"&\lim_{n \to \infty} {1 \over n}{\sum^{n-1}_{k=0} (1 + 2\cos{2 k \pi \over n})^8} \\ "
                        r"=& \sum^{8}_{k=0} {_8C_k} 2^k \int^1_0 \cos^k{2 \pi x} \> dx ",
                        tex_environment="align*",
                    ).scale(0.6)
                ),
            )
            .arrange_in_grid(
                buff=(1, 0.5),
                col_alignments="cc",
                row_alignments="cc",
                flow_order="rd",
            )
            .shift(DOWN * 0.7)
        )

        # Highlight a_8
        overview_imgs[1].submobjects[0][0][28:30].set_color(color=BLUE)
        overview_imgs[2].submobjects[0][0][0:2].set_color(color=BLUE)

        self.add(overview_text)
        self.add(overview_imgs)

        self.wait()
        self.next_slide()

        # <Problem introduction>
        self.clear()
        problem = Group(
            Group(
                Text("8개의 정수"),
                Tex(r"\; a_1, a_2, a_3, \cdots , a_8", tex_environment="gather*").scale(
                    1.2
                ),
            ).arrange(),
            Group(
                Text("조건:"),
                Tex(
                    r"\; \sum_{k=1}^8 a_k = 8, \; a_k \in \{0,1,2\}",
                    tex_environment="gather*",
                ),
            ).arrange(),
            Group(
                Text("모든 순서쌍 "),
                Tex(r"(a_1, a_2, a_3, \cdots , a_8)", tex_environment="gather*"),
                Text("의 수는?"),
            ).arrange(),
        ).arrange(DOWN, buff=0.75)

        self.play(
            AnimationGroup(
                *[Create(text) for text in problem[0]], lag_ratio=1, run_time=0.3
            )
        )
        self.wait()
        self.next_slide()
        self.play(
            AnimationGroup(
                *[Create(text) for text in problem[1]], lag_ratio=1, run_time=0.3
            )
        )
        self.wait()
        self.next_slide()
        self.play(
            AnimationGroup(
                *[Create(text) for text in problem[2]], lag_ratio=1, run_time=0.3
            )
        )
        self.wait()
        self.next_slide()

        # <Solution>
        self.clear()
        (0, 4), (2, 3), (4, 2), (6, 1), (8, 0)


class Polynomial(Slide):
    """
    문제를 다항식 표현으로 변형
    """

    def construct(self):
        pass


class ComplexTrigonometry(Slide):
    """
    복소수와 삼각함수 관계
    nth root of unity
    복소수 거듭제곱의 주기성 활용
    """

    def construct(self):
        pass


class ValueToCoeff(Slide):
    """
    다항함수 함숫값 -> 계수 구하기
    """

    def construct(self):
        pass


class Integral(Slide):
    """
    적분식 표현, 삼각함수 거듭제곱 적분, 최종 계산 결과
    """

    def construct(self):
        pass


class Outro(Slide):
    def construct(self):
        pass
