from manim import *
from manim_slides import Slide


def tex_append_animation(tex: Tex, *strings: str, return_new_tex: bool = False):
    new_tex = Tex(
        *tex.tex_strings, *strings, tex_environment=tex.tex_environment
    ).move_to(tex)
    if return_new_tex:
        return TransformMatchingTex(tex, new_tex), new_tex
    return TransformMatchingTex(tex, new_tex)


class Intro(Slide):
    """
    풀이 개요
    문제 소개
    의도된 풀이
    """

    def construct(self):
        # TODO Fix broken tex

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
        self.wait()
        self.next_slide()

        overview_text = Text("Overview").scale(1).center().shift(UP * 3)

        overview_rectangle_style = (WHITE, 2.5, 4.5)
        overview_imgs = (
            Group(
                Rectangle(*overview_rectangle_style).add(
                    Tex(
                        r"0 \cdot 4 + 1 \cdot 0 + 2 \cdot 4 \rightarrow {_8C_4 \cdot _4C_0 \cdot _4C_4} \\ "
                        r"0 \cdot 3 + 1 \cdot 2 + 2 \cdot 3 \rightarrow {_8C_3 \cdot _5C_2 \cdot _3C_3} \\ "
                        r"0 \cdot 2 + 1 \cdot 4 + 2 \cdot 2 \rightarrow {_8C_2 \cdot _6C_4 \cdot _2C_2} \\ "
                        r"\vdots",
                        tex_environment="gather*",
                    ).scale(0.5)
                ),
                Rectangle(*overview_rectangle_style).add(
                    MathTex(
                        r"&f(x) = (1+x+x^2)^8 \\ "
                        r"=& \; c_0 + c_1 \cdot x + c_2 \cdot x^2 + \cdots  \\ "
                        r"&+ c_8 \cdot x^8 + \cdots + c_{16} \cdot x^{16}",
                    ).scale(0.65)
                ),
                Rectangle(*overview_rectangle_style).add(
                    MathTex(
                        r"c_8 =& {1 \over n}{\sum^{n-1}_{k=0} f(e^{2 k \pi i k \over n})e^{- 8 \cdot {2 k \pi i k \over n}}} \\"
                        r"=& {1 \over n}{\sum^{n-1}_{k=0} (1 + 2\cos{2 k \pi \over n})^8}",
                    ).scale(0.6)
                ),
                Rectangle(*overview_rectangle_style).add(
                    MathTex(
                        r"&\lim_{n \to \infty} {1 \over n}{\sum^{n-1}_{k=0} (1 + 2\cos{2 k \pi \over n})^8} \\ "
                        r"=& \sum^{8}_{k=0} {_8C_k} 2^k \int^1_0 \cos^k{2 \pi x} \> dx ",
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

        # TODO Add highlights and animations

        # Highlight a_8
        overview_imgs[1].submobjects[0][0][33:35].set_color(color=BLUE)
        overview_imgs[2].submobjects[0][0][0:2].set_color(color=BLUE)

        self.add(overview_text)
        self.add(overview_imgs)

        self.wait()
        self.next_slide()

        # <Problem introduction>
        self.clear()
        self.wait()
        self.next_slide()

        problem = Group(
            Group(
                Text("8개의 정수"),
                MathTex(r"a_1, a_2, a_3, \cdots , a_8").scale(1.2),
            ).arrange(),
            Group(
                Text("조건:"),
                MathTex(r"a_k \in \{0,1,2\} , \; \sum_{k=1}^8 a_k = 8"),
            ).arrange(),
            Group(
                Text("모든 순서쌍 "),
                MathTex(r"(a_1, a_2, a_3, \cdots , a_8)"),
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
        self.wait()
        self.next_slide()

        solution1 = MathTex("x")
        self.play(Create(solution1), run_time=0.5)
        self.wait()
        self.next_slide()
        self.play(
            Transform(
                solution1,
                MathTex("x", r", \; ", "y"),
            ),
            run_time=0.5,
        )
        self.wait()
        self.next_slide()
        self.play(
            TransformMatchingTex(
                solution1,
                MathTex("x", r" + 2 \cdot ", "y", " = 8"),
            ),
            run_time=0.5,
        )
        self.wait()
        self.next_slide()

        # Isolate subjects and set key map
        solution2_strings = []
        solution3_strings = []
        solution_key_map = {}
        for i in range(5):
            solution2_strings += [f"({2*i}, ", f"{4-i}) ", r"\quad "]
            solution3_strings += [f"_8C_{2*i} ", r"\cdot ", f"_{8-2*i}C_{4-i} ", "+ "]
            solution_key_map[f"({2*i}, "] = f"_8C_{2*i} "
            solution_key_map[f"{4-i}) "] = f"_{8-2*i}C_{4-i} "
        # Remove trailing \quad and +
        solution2_strings.pop()
        solution3_strings.pop()

        solution2 = MathTex(*solution2_strings)
        self.play(solution1.animate.shift(UP * 2), run_time=0.5)
        self.play(Create(solution2, run_time=2))
        self.wait()
        self.next_slide()

        solution3 = MathTex(*solution3_strings)
        self.play(solution2.animate.shift(UP * 1), run_time=0.5)
        self.play(
            TransformMatchingTex(solution2.copy(), solution3, key_map=solution_key_map)
        )

        self.wait()
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()


class Polynomial(Slide):
    """
    문제를 다항식 표현으로 변형
    """

    def construct(self):
        polynomial = MathTex(
            "(1+x+x^2)",
            "^8",
        ).scale(1.5)
        self.play(Create(polynomial))
        self.wait()
        self.next_slide()

        x0_rect = SurroundingRectangle(polynomial[0][1])
        x1_rect = SurroundingRectangle(polynomial[0][3])

        x0_tex = MathTex(
            "x^0",
        ).scale(1.3)
        x1_tex = MathTex(
            "x^1",
        ).scale(1.3)

        x0_tex.next_to(polynomial[0][1], DOWN * 1.2)
        x1_tex.next_to(polynomial[0][3], DOWN * 1.2)

        self.play(
            AnimationGroup(
                Create(x0_rect),
                Create(x0_tex),
                lag_ratio=0.5,
                run_time=0.7,
            )
        )
        self.play(FadeOut(x0_rect))
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                Create(x1_rect),
                Create(x1_tex),
                lag_ratio=0.5,
                run_time=0.7,
            )
        )
        self.play(FadeOut(x1_rect))
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                Indicate(x0_tex[0][1]),
                Indicate(x1_tex[0][1]),
                Indicate(polynomial[0][6]),
                lag_ratio=0.5,
            ),
        )
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                Indicate(polynomial[1][0]),
                FadeOut(x0_tex, x1_tex),
                lag_ratio=0.3,
            )
        )
        self.wait()
        self.next_slide()

        expansion1 = MathTex(
            "(1+x+x^2)",
            "(1+x+x^2)",
            r"\cdots",
            "(1+x+x^2)",
        ).shift(UP)
        self.play(polynomial.animate.scale(0.8).shift(UP * 1.5))
        self.play(TransformMatchingTex(polynomial, expansion1))
        self.wait()
        self.next_slide()

        a1_choice = MathTex(
            "1",
        )
        arrow1 = Arrow(
            start=UP,
            end=DOWN,
            max_tip_length_to_length_ratio=0.15,
            max_stroke_width_to_length_ratio=10,
        ).scale(0.5)
        a1 = MathTex(
            "a_1 = ",
            "0",
        )
        a1_group = Group(a1_choice, arrow1, a1)
        a1_group.arrange(DOWN)
        a1_group.next_to(expansion1[0][1], DOWN)
        self.play(
            AnimationGroup(
                Indicate(expansion1[0]),
                ReplacementTransform(expansion1[0][1].copy(), a1_choice),
                Create(arrow1),
                Create(a1),
                lag_ratio=0.8,
                run_time=1.5,
            )
        )
        self.wait()
        self.next_slide()

        a2_choice = MathTex(
            "x",
        )
        arrow2 = arrow1.copy()
        a2 = MathTex(
            "a_2 = ",
            "1",
        )
        a2_group = Group(a2_choice, arrow2, a2)
        a2_group.arrange(DOWN)
        a2_group.next_to(expansion1[1][3], DOWN)
        self.play(
            AnimationGroup(
                Indicate(expansion1[1]),
                ReplacementTransform(expansion1[1][3].copy(), a2_choice),
                Create(arrow2),
                Create(a2),
                lag_ratio=0.8,
                run_time=1.5,
            )
        )
        self.wait()
        self.next_slide()

        expansion1_wide = MathTex(
            "(1+x+x^2)",
            "(1+x+x^2)",
            r"\;",
            r"\cdots",
            r"\;",
            "(1+x+x^2)",
        ).shift(UP)
        dots = MathTex(
            r"\cdots",
        )
        dots.next_to(expansion1_wide[3], DOWN)
        dots.match_y(arrow1)

        a8_choice_ = MathTex(
            "x",
        ).set_opacity(0)
        arrow8 = arrow1.copy()
        a8 = MathTex(
            "a_8 = ",
            "1",
        )
        a8_group = Group(a8_choice_, arrow8, a8)
        a8_group.arrange(DOWN)
        a8_group.next_to(expansion1[3][3], DOWN)
        a8_choice = expansion1[3][3].copy()

        self.play(
            AnimationGroup(
                TransformMatchingTex(expansion1, expansion1_wide),
                Create(dots),
                a1_group.animate.next_to(expansion1_wide[0][1], DOWN),
                a2_group.animate.next_to(expansion1_wide[1][3], DOWN),
                AnimationGroup(
                    ReplacementTransform(a8_choice, a8_choice_),
                    Create(arrow8),
                    Create(a8),
                    lag_ratio=0.5,
                    run_time=0.6,
                ),
                a8_choice.animate.next_to(expansion1_wide[5][3], DOWN),
                a8_group.animate.next_to(expansion1_wide[5][3], DOWN),
            )
        )
        self.wait()
        self.next_slide()

        polynomial.shift(UP * 1.5, LEFT * 4)
        choices = [0, 1, 1, 2, 2, 1, 0, 1]
        multiplication = MathTex(
            "1",
            r" \cdot ",
            "x",
            r" \cdot ",
            r" \cdot ".join(["1", "x", "x^2"][i] for i in choices[2:7]),
            r" \cdot ",
            "x",
        )
        a_sum = MathTex(
            "0",
            "+",
            "1",
            "+",
            "+".join(str(i) for i in choices[2:7]),
            "+",
            "1",
        )

        multiplication.next_to(expansion1_wide, DOWN)
        a_sum.match_y(a1)

        self.play(
            AnimationGroup(
                AnimationGroup(
                    TransformMatchingTex(expansion1_wide, polynomial),
                    FadeOut(arrow1, arrow2, arrow8, dots),
                    TransformMatchingShapes(a1_choice, multiplication[0]),
                    TransformMatchingShapes(a2_choice, multiplication[2]),
                    TransformMatchingShapes(a8_choice, multiplication[6]),
                    TransformMatchingShapes(a1, a_sum[0]),
                    TransformMatchingShapes(a2, a_sum[2]),
                    TransformMatchingShapes(a8, a_sum[6]),
                ),
                AnimationGroup(
                    Create(multiplication),
                    Create(a_sum),
                ),
                lag_ratio=0.7,
            )
        )
        self.wait()
        self.next_slide()

        self.play(ApplyWave(multiplication))
        self.wait()
        self.next_slide()
        self.play(ApplyWave(a_sum))
        self.wait()
        self.next_slide()

        anim1, multiplication = tex_append_animation(
            multiplication, f" = x^{sum(choices)}", return_new_tex=True
        )
        anim2, a_sum = tex_append_animation(
            a_sum, f" = {sum(choices)}", return_new_tex=True
        )
        self.play(anim1, anim2)
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                Circumscribe(a_sum[-1][-1]),
                Circumscribe(multiplication[-1][-1]),
                lag_ratio=1,
            )
        )
        self.wait()
        self.next_slide()

        expansion2 = (
            MathTex(
                r"= c_0 + c_1 \cdot x + \cdots + ",
                "c_8",
                r" \cdot x^8 + \cdots + c_{16} \cdot x^{16}",
            )
            .scale(1.2)
            .match_y(polynomial)
            .shift(DOWN * 2)
        )
        self.play(
            AnimationGroup(
                FadeOut(multiplication, a_sum),
                polynomial.animate.shift(DOWN + RIGHT * 0.8),
                Create(expansion2),
                lag_ratio=0.7,
            )
        )
        self.wait()
        self.next_slide()

        self.play(
            Flash(expansion2[1], flash_radius=0.4),
            expansion2[1].animate.set_color(BLUE),
        )
        self.wait()
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()


class ComplexTrigonometry(Slide):
    """
    복소수와 삼각함수 관계
    nth root of unity
    복소수 거듭제곱의 주기성 활용
    """

    def construct(self):
        self.wait()
        self.next_slide()

        polynomial = MathTex("f(x) = ax + b")
        self.play(Create(polynomial))
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                Circumscribe(polynomial[0][5]),
                Circumscribe(polynomial[0][8]),
                lag_ratio=0.2,
            )
        )
        self.wait()
        self.next_slide()

        values = Group(
            MathTex("f(", "x_1", ")"),
            MathTex("f(", "x_2", ")"),
        ).arrange(RIGHT, buff=1)
        self.play(
            polynomial.animate.shift(UP),
        )
        self.play(AnimationGroup(*[Create(i) for i in values], lag_ratio=0.5))
        self.wait()
        self.next_slide()

        coeffs = (
            Group(
                MathTex(
                    r"a = {f(x_1)-f(x_2) \over x_1 - x_2}",
                    substrings_to_isolate=("f(", "x_1", "x_2", ")"),
                ),
                MathTex(
                    r"b = f(x_1) - a x_1",
                    substrings_to_isolate=("f(", "x_1", "x_2", ")"),
                ),
            )
            .arrange(RIGHT, buff=1)
            .shift(DOWN * 0.3)
        )

        self.play(
            TransformMatchingShapes(values[0].copy(), coeffs[1][:4]),
            TransformMatchingShapes(values[0].copy(), coeffs[1][4:]),
            TransformMatchingShapes(values.copy(), coeffs[0][:9]),
            TransformMatchingShapes(values, coeffs[0][9:]),
        )
        self.wait()
        self.next_slide()

        coeffs_new = (
            Group(
                MathTex("a = f(1) - f(0)"),
                MathTex("b = f(0)"),
            )
            .arrange(RIGHT, buff=1)
            .match_y(coeffs)
        )

        self.play(TransformMatchingShapes(coeffs[1], coeffs_new[1]))
        self.wait()
        self.next_slide()

        self.play(TransformMatchingShapes(coeffs[0], coeffs_new[0]))
        self.wait()
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])

        polynomial = MathTex("f(x) = ax^3 + bx^2 + cx + d")
        self.play(FadeIn(polynomial))
        self.wait()
        self.next_slide()

        values = MathTex(
            r"f(-1) &= - a + b - c + d \\ ",
            r"f(0) &= d  \\ ",
            r"f(1) &= a + b + c + d \\ ",
            r"f(2) &= 8a + 4b + 2c + d \\ ",
        ).shift(DOWN)

        coeffs = (
            MathTex(
                r"a &= - {1 \over 6} f(-1) + {1 \over 2} f(0) - {1 \over 2} f(1) + {1 \over 6} f(2) \\ ",
                r"b &= {1 \over 2} f(-1) - f(0) + {1 \over 2} f(1) \\ ",
                r"c &= - {1 \over 3} f(-1) - {1 \over 2} f(0) + f(1) - {1 \over 6} f(2) \\ ",
                r"d &= f(0) \\ ",
            )
            .scale(0.85)
            .shift(RIGHT * 2.8 + DOWN)
        )

        self.play(
            AnimationGroup(
                polynomial.animate.shift(UP * 2),
                AnimationGroup(
                    *[Create(i) for i in values],
                    lag_ratio=0.5,
                ),
                lag_ratio=0.8,
            )
        )
        self.wait()
        self.next_slide()

        self.play(
            AnimationGroup(
                values.animate.shift(LEFT * 3.7).scale(0.9),
                AnimationGroup(
                    *[Create(i) for i in coeffs],
                    lag_ratio=0.5,
                ),
                lag_ratio=0.8,
            )
        )
        self.wait()
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()

        complex_number = MathTex(
            "a", " + ", "bi", substrings_to_isolate=["a", "b", "i"]
        ).scale(1.5)
        self.play(FadeIn(complex_number))
        self.wait()
        self.next_slide()

        self.play(Indicate(complex_number[0]))
        self.play(Indicate(complex_number[2:]))

        self.wait()
        self.next_slide()

        complex_mult = MathTex(
            "(a + bi)",
            "(c + di)",
            substrings_to_isolate=["a", "b", "c", "d", "i"],
        ).scale(1.2)
        self.play(
            TransformMatchingShapes(complex_number, complex_mult[:6]),
            TransformMatchingShapes(complex_number.copy(), complex_mult[6:]),
        )
        self.wait()
        self.next_slide()

        complex_mult_result = MathTex(
            "(ac - bd) + ",
            "(ad + bc)i",
            substrings_to_isolate=["a", "b", "c", "d", "i"],
        ).scale(1.2)
        self.play(TransformMatchingTex(complex_mult, complex_mult_result))
        self.wait()
        self.next_slide()

        substitution = MathTex(
            r"a = \cos(\alpha) & ",
            r" \quad ",
            r"c = \cos(\beta) \\ ",
            r"b = \sin(\alpha) &",
            r"  \quad ",
            r"d = \sin(\beta) \\ ",
            substrings_to_isolate=[
                r"\cos(\alpha)",
                r"\cos(\beta)",
                r"\sin(\alpha)",
                r"\sin(\beta)",
            ],
        ).next_to(complex_mult_result, DOWN)
        self.play(Create(substitution))
        self.wait()
        self.next_slide()

        complex_mult_substituted = MathTex(
            r"( \cos(\alpha) \cos(\beta) - \sin(\alpha) \sin(\beta)) + ",
            r"( \cos(\alpha) \sin(\beta) + \sin(\alpha) \cos(\beta))i",
            substrings_to_isolate=[
                r"\cos(\alpha)",
                r"\cos(\beta)",
                r"\sin(\alpha)",
                r"\sin(\beta)",
                "i",
            ],
        )

        self.play(
            TransformMatchingTex(complex_mult_result, complex_mult_substituted),
            TransformMatchingTex(substitution, complex_mult_substituted),
        )
        self.wait()
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()


class ValueToCoeff(Slide):
    """
    다항함수 함숫값 -> 계수 구하기
    """

    def construct(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()


class Integral(Slide):
    """
    적분식 표현, 삼각함수 거듭제곱 적분, 최종 계산 결과
    """

    def construct(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()


class Outro(Slide):
    def construct(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()
        self.next_slide()
