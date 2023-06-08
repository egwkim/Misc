from typing import Any, Type

# TODO Highlight equations

from manim import *
from manim_slides import Slide


def tex_append_animation(tex: Tex, *strings: str, return_new_tex: bool = False):
    new_tex = Tex(
        *tex.tex_strings, *strings, tex_environment=tex.tex_environment
    ).move_to(tex)
    if return_new_tex:
        return TransformMatchingTex(tex, new_tex), new_tex
    return TransformMatchingTex(tex, new_tex)


def animate_submobjects(
    mobject: Mobject,
    AnimClass: Type[Animation],
    animation_options: dict[str, Any] = {},
    group_options: dict[str, Any] = {},
    **kwargs,
):
    return AnimationGroup(
        *(AnimClass(i, **animation_options) for i in mobject), **group_options, **kwargs
    )


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
        self.wait(0.1)
        self.next_slide()

        # <Overview>
        self.play(FadeOut(title), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        overview_text = Text("Overview").scale(1).center().shift(UP * 3)

        overview_rectangle_style = {
            "color": WHITE,
            "height": 2.5,
            "width": 4.5,
            "stroke_width": 1.5,
        }
        overview_imgs = (
            Group(
                Rectangle(**overview_rectangle_style).add(
                    Tex(
                        r"0 \cdot 4 + 1 \cdot 0 + 2 \cdot 4 \rightarrow {_8C_4 \cdot _4C_0 \cdot _4C_4} \\ "
                        r"0 \cdot 3 + 1 \cdot 2 + 2 \cdot 3 \rightarrow {_8C_3 \cdot _5C_2 \cdot _3C_3} \\ "
                        r"0 \cdot 2 + 1 \cdot 4 + 2 \cdot 2 \rightarrow {_8C_2 \cdot _6C_4 \cdot _2C_2} \\ "
                        r"\vdots",
                        tex_environment="gather*",
                    ).scale(0.5)
                ),
                Rectangle(**overview_rectangle_style).add(
                    MathTex(
                        r"&f(x) = (1+x+x^2)^8 \\ "
                        r"=& \; c_0 + c_1 \cdot x + c_2 \cdot x^2 + \cdots  \\ "
                        r"&+ c_8 \cdot x^8 + \cdots + c_{16} \cdot x^{16}",
                    ).scale(0.65)
                ),
                Rectangle(**overview_rectangle_style).add(
                    MathTex(
                        r"c_8 =& {1 \over n} \sum^{n-1}_{k=0} f(z^k) z^{-8k} \\"
                        r"=& {1 \over n} \sum^{n-1}_{k=0} (1 + 2\cos{2 k \pi \over n})^8",
                    ).scale(0.6)
                ),
                Rectangle(**overview_rectangle_style).add(
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

        # Highlight c_8
        overview_imgs[1].submobjects[0][0][33:35].set_color(color=BLUE)
        overview_imgs[2].submobjects[0][0][0:2].set_color(color=BLUE)

        self.play(FadeIn(overview_text, scale=0.8), run_time=0.7)
        self.wait(0.1)
        self.next_slide()

        self.play(FadeIn(overview_imgs[0], scale=0.9), run_time=0.7)
        self.wait(0.1)
        self.next_slide()

        self.play(FadeIn(overview_imgs[1], scale=0.9), run_time=0.7)
        self.wait(0.1)
        self.next_slide()

        self.play(FadeIn(overview_imgs[2], scale=0.9), run_time=0.7)
        self.wait(0.1)
        self.next_slide()

        self.play(FadeIn(overview_imgs[3], scale=0.9), run_time=0.7)
        self.wait(0.1)
        self.next_slide()

        self.play(FadeOut(*self.mobjects), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        # <Problem introduction>
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
                *[Write(text) for text in problem[0]], lag_ratio=1, run_time=0.25
            )
        )
        self.wait(0.1)
        self.next_slide()
        self.play(
            AnimationGroup(
                *[Write(text) for text in problem[1]], lag_ratio=1, run_time=0.25
            )
        )
        self.wait(0.1)
        self.next_slide()
        self.play(
            AnimationGroup(
                *[Write(text) for text in problem[2]], lag_ratio=1, run_time=0.25
            )
        )
        self.wait(0.1)
        self.next_slide()

        self.play(FadeOut(*self.mobjects), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        # <Solution>
        solution1_1 = MathTex("x")
        solution1_2 = MathTex("x", r", \; ", "y")
        solution1_3 = MathTex("x", r" + 2 ", "y", " = 8")
        self.play(Create(solution1_1), run_time=0.2)
        self.wait(0.1)
        self.next_slide()
        self.play(
            ReplacementTransform(solution1_1, solution1_2),
            run_time=0.4,
        )
        self.wait(0.1)
        self.next_slide()
        self.play(
            TransformMatchingTex(solution1_2, solution1_3),
            run_time=0.4,
        )
        self.wait(0.1)
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

        solution2 = MathTex(*solution2_strings).shift(UP * 0.4)
        self.play(solution1_3.animate.shift(UP * 2), run_time=0.5)
        self.play(
            AnimationGroup(
                *(Create(i) for i in solution2),
                lag_ratio=1,
                run_time=0.7,
            )
        )
        self.wait(0.1)
        self.next_slide()

        solution3 = MathTex(*solution3_strings).shift(DOWN)
        self.play(Indicate(solution2[6:8]))
        self.wait(0.1)
        self.next_slide()

        self.play(Transform(solution2[6][1].copy(), solution3[8]), run_time=0.8)
        self.wait(0.1)
        self.next_slide()

        self.play(Transform(solution2[7][0].copy(), solution3[9:11]), run_time=0.8)
        self.wait(0.1)
        self.next_slide()

        transforms = []
        for i in [0, 1]:
            transforms.append(
                Transform(solution2[3 * i][1].copy(), solution3[4 * i : 4 * i + 2])
            )
            transforms.append(
                Transform(
                    solution2[3 * i + 1][0].copy(), solution3[4 * i + 2 : 4 * i + 4]
                )
            )
        for i in [3, 4]:
            transforms.append(
                Transform(solution2[3 * i][1].copy(), solution3[4 * i - 1 : 4 * i + 1])
            )
            transforms.append(
                Transform(
                    solution2[3 * i + 1][0].copy(), solution3[4 * i + 1 : 4 * i + 3]
                )
            )
        self.play(AnimationGroup(*transforms, lag_ratio=0.2, run_time=1.2))
        self.wait(0.1)
        self.next_slide()

        answer = MathTex("= 1107")
        answer.scale(1.2).next_to(solution3, DOWN, buff=1)
        self.play(Write(answer), run_time=0.7)
        self.wait(0.1)
        self.next_slide()

        self.play(FadeOut(*self.mobjects))
        self.wait(0.1)
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
        self.wait(0.1)
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
        self.wait(0.1)
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
        self.wait(0.1)
        self.next_slide()

        self.play(
            AnimationGroup(
                Indicate(x0_tex[0][1]),
                Indicate(x1_tex[0][1]),
                Indicate(polynomial[0][6]),
                lag_ratio=0.5,
            ),
        )
        self.wait(0.1)
        self.next_slide()

        self.play(Indicate(polynomial[1][0]))
        self.wait(0.1)
        self.next_slide()

        expansion1 = MathTex(
            "(1+x+x^2)",
            "(1+x+x^2)",
            r"\cdots",
            "(1+x+x^2)",
        ).shift(UP)
        self.play(
            AnimationGroup(
                FadeOut(x0_tex, x1_tex),
                polynomial.animate.scale(0.8).shift(UP * 1.5),
                lag_ratio=0.5,
            )
        )
        self.play(TransformMatchingTex(polynomial, expansion1))
        self.wait(0.1)
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
        self.play(Indicate(expansion1[0]))
        self.play(
            AnimationGroup(
                ReplacementTransform(expansion1[0][1].copy(), a1_choice),
                Create(arrow1),
                Create(a1),
                lag_ratio=0.8,
                run_time=1.5,
            )
        )
        self.wait(0.1)
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
        self.play(Indicate(expansion1[1]))
        self.play(
            AnimationGroup(
                ReplacementTransform(expansion1[1][3].copy(), a2_choice),
                Create(arrow2),
                Create(a2),
                lag_ratio=0.8,
                run_time=1.5,
            )
        )
        self.wait(0.1)
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
        self.wait(0.1)
        self.next_slide()

        polynomial.shift(UP * 1.5, LEFT * 4)
        choices = [
            [0, 1, 1, 2, 2, 1, 0, 1],
            [0, 0, 0, 2, 1, 0, 1, 2],
            [0, 2, 0, 0, 2, 1, 2, 0],
            [0, 1, 1, 2, 2, 1, 1, 1],
            [1, 2, 1, 0, 2, 2, 1, 2],
            [0, 1, 1, 2, 0, 2, 0, 2],
        ]
        multiplication = MathTex(
            "1",
            r" \cdot ",
            "x",
            r" \cdot ",
            r" \cdot ".join(["1", "x", "x^2"][i] for i in choices[0][2:7]),
            r" \cdot ",
            "x",
        )
        a_sum = MathTex(
            "0",
            "+",
            "1",
            "+",
            "+".join(str(i) for i in choices[0][2:7]),
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
        self.wait(0.1)
        self.next_slide()

        self.play(Circumscribe(multiplication))
        self.wait(0.1)
        self.next_slide()
        self.play(Circumscribe(a_sum))
        self.wait(0.1)
        self.next_slide()

        anim1, multiplication = tex_append_animation(
            multiplication, f" = x^{sum(choices[0])}", return_new_tex=True
        )
        anim2, a_sum = tex_append_animation(
            a_sum, f" = {sum(choices[0])}", return_new_tex=True
        )
        self.play(anim1, anim2)
        self.wait(0.1)
        self.next_slide()

        self.play(
            AnimationGroup(
                Circumscribe(a_sum[-1][-1]),
                Circumscribe(multiplication[-1][-1]),
                lag_ratio=1,
            )
        )
        self.wait(0.1)
        self.next_slide()

        multiplications = [
            MathTex(
                r" \cdot ".join(["1", "x", "x^2"][i] for i in choices[j]),
                r" = x^{" + str(sum(choices[j])) + r"}",
            ).move_to(multiplication)
            for j in range(1, len(choices))
        ]
        a_sums = [
            MathTex(
                "+".join(str(i) for i in choices[j]),
                rf" = {sum(choices[j])}",
            ).move_to(a_sum)
            for j in range(1, len(choices))
        ]

        self.remove(multiplication, a_sum)

        for i in range(len(multiplications) - 1):
            self.add(multiplications[i], a_sums[i])
            self.wait(0.1)
            self.next_slide()
            self.remove(multiplications[i], a_sums[i])

        self.add(multiplications[-1], a_sums[-1])
        self.wait(0.1)
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
                FadeOut(multiplications[-1], a_sums[-1]),
                polynomial.animate.shift(DOWN + RIGHT * 0.8),
                Create(expansion2),
                lag_ratio=0.7,
            )
        )
        self.wait(0.1)
        self.next_slide()

        self.play(
            Flash(expansion2[1], flash_radius=0.4),
            expansion2[1].animate.set_color(BLUE),
        )
        self.wait(0.1)
        self.next_slide()

        self.play(FadeOut(*self.mobjects), run_time=0.5)
        self.wait(0.1)
        self.next_slide()


class ComplexTrigonometry(Slide):
    """
    복소수와 삼각함수 관계
    nth root of unity
    복소수 거듭제곱의 주기성 활용
    """

    def construct(self):
        polynomial = MathTex("f(x) = ax + b")
        self.play(Write(polynomial), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        self.play(
            AnimationGroup(
                Circumscribe(polynomial[0][5]),
                Circumscribe(polynomial[0][8]),
                lag_ratio=0.3,
            )
        )
        self.wait(0.1)
        self.next_slide()

        values = Group(
            MathTex("f(", "x_1", ")"),
            MathTex("f(", "x_2", ")"),
        ).arrange(RIGHT, buff=1)
        self.play(
            polynomial.animate.shift(UP),
        )
        self.play(animate_submobjects(values, Write, lag_ratio=0.5, run_time=0.8))
        self.wait(0.1)
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
        self.wait(0.1)
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
        self.wait(0.1)
        self.next_slide()

        self.play(TransformMatchingShapes(coeffs[0], coeffs_new[0]))
        self.wait(0.1)
        self.next_slide()

        self.play(FadeOut(*self.mobjects), run_time=0.5)

        polynomial = MathTex("f(x) = ax^3 + bx^2 + cx + d")
        self.play(FadeIn(polynomial), run_time=0.5)
        self.wait(0.1)
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
                animate_submobjects(values, Write, lag_ratio=0.5, run_time=1.5),
                lag_ratio=0.8,
            )
        )
        self.wait(0.1)
        self.next_slide()

        self.play(
            AnimationGroup(
                values.animate.shift(LEFT * 3.7).scale(0.9),
                animate_submobjects(coeffs, Write, lag_ratio=0.5, run_time=2),
                lag_ratio=0.7,
            )
        )
        self.wait(0.1)
        self.next_slide()

        self.play(FadeOut(*self.mobjects), run_time=0.6)
        self.wait(0.1)
        self.next_slide()

        complex_number = MathTex("a + b i", substrings_to_isolate=" ").scale(1.8)
        self.play(FadeIn(complex_number, scale=0.5))
        self.wait(0.1)
        self.next_slide()

        self.play(Indicate(complex_number[0]))
        self.play(Indicate(complex_number[4:]))
        self.wait(0.1)
        self.next_slide()

        complex_sum = MathTex(
            "( a + b i )",
            "+" "( c + d i )",
            substrings_to_isolate=" ",
        ).scale(1.4)
        self.play(TransformMatchingTex(complex_number, complex_sum))
        self.wait(0.1)
        self.next_slide()
        complex_sum_result = MathTex(
            "= ( a + c ) + ( b + d ) i",
            substrings_to_isolate=" ",
        )
        complex_sum_result.scale(1.4).shift(UP * 0.5)
        self.play(
            complex_sum.animate.shift(UP * 1.5),
            TransformMatchingShapes(complex_sum.copy(), complex_sum_result),
        )
        self.wait(0.1)
        self.next_slide()

        complex_mult = MathTex(
            "( a + b i )",
            "( c + d i )",
            substrings_to_isolate=" ",
        ).scale(1.4)

        complex_mult.match_y(complex_sum)
        self.play(
            TransformMatchingShapes(complex_sum, complex_mult),
            FadeOut(complex_sum_result),
        )
        self.wait(0.1)
        self.next_slide()
        complex_mult_result = MathTex(
            "= ( a c - b d ) + ",
            "( a d + b c ) i",
            substrings_to_isolate=" ",
        )
        complex_mult_result.scale(1.4).shift(UP * 0.5)
        self.play(
            TransformMatchingTex(complex_mult.copy(), complex_mult_result),
        )
        self.wait(0.1)
        self.next_slide()

        substitution = MathTex(
            r"a = \cos(\alpha) & ",
            r" \quad ",
            r"c = \cos(\beta) \\ ",
            r"b = \sin(\alpha) &",
            r"  \quad ",
            r"d = \sin(\beta) \\ ",
            substrings_to_isolate=" ",
        )
        substitution.scale(1.4).next_to(complex_mult_result, DOWN, buff=1)
        self.play(animate_submobjects(substitution, Create, lag_ratio=0.1, run_time=1))
        self.wait(0.1)
        self.next_slide()

        complex_mult_subs = MathTex(
            r"& ( \cos(\alpha) + i \sin(\alpha) ) ",
            r"( \cos(\beta) + i \sin(\beta) ) \\ ",
            r"= \; & ( \cos(\alpha) \cos(\beta) - \sin(\alpha) \sin(\beta) ) \\ ",
            r"& + i \cdot ( \cos(\alpha) \sin(\beta) + \sin(\alpha) \cos(\beta) )",
            substrings_to_isolate=" ",
        )
        complex_mult_subs.scale(1.2).shift(UP * 0.5)
        complex_mult_subs_result = MathTex(
            r"=\;& \cos ( \alpha + \beta ) + i \sin( \alpha + \beta )",
            substrings_to_isolate=" ",
        )
        complex_mult_subs_result.scale(1.2)

        Group(complex_mult_subs, complex_mult_subs_result).arrange(
            DOWN, center=False, aligned_edge=LEFT
        )

        self.play(
            TransformMatchingTex(complex_mult, complex_mult_subs),
            TransformMatchingTex(complex_mult_result, complex_mult_subs),
            TransformMatchingTex(substitution, complex_mult_subs),
            run_time=0.9,
        )
        self.wait(0.1)
        self.next_slide()

        # Highlight cos addition
        self.play(Circumscribe(complex_mult_subs[36:45]))
        self.wait(0.1)
        self.next_slide()

        # Highlight sin addition
        self.play(Circumscribe(complex_mult_subs[60:69]))
        self.wait(0.1)
        self.next_slide()

        self.play(
            animate_submobjects(
                complex_mult_subs_result, Create, lag_ratio=1, run_time=1
            )
        )
        self.wait(0.1)
        self.next_slide()

        self.play(
            AnimationGroup(
                FadeOut(complex_mult_subs[27:]),
                AnimationGroup(
                    complex_mult_subs[:27].animate.shift(DOWN * 0.7).scale(1.2),
                    complex_mult_subs_result.animate.shift(UP * 0.5).scale(1.2),
                ),
                lag_ratio=0.7,
            )
        )
        self.play(
            AnimationGroup(
                Circumscribe(complex_mult_subs[3:11]),
                Circumscribe(complex_mult_subs[16:23]),
                lag_ratio=0.8,
            )
        )
        self.wait(0.1)
        self.next_slide()

        self.play(
            Indicate(complex_mult_subs_result[5:12]),
            Indicate(complex_mult_subs_result[19:25]),
        )
        self.wait(0.1)
        self.next_slide()

        self.play(FadeOut(*self.mobjects), run_time=0.5)
        self.wait(0.1)
        self.next_slide()


class ComplexPlaneSlide(Slide):
    def construct(self):
        plane = ComplexPlane(
            x_range=(-2.88, 2.88, 1),
            y_range=(-1.6, 1.6, 1),
            x_length=14.4,
            y_length=8,
            faded_line_ratio=4,
        )
        coord_labels = plane.get_coordinate_labels()

        self.play(FadeIn(plane, coord_labels), run_time=0.6)
        self.wait(0.1)
        self.next_slide()

        # Indicate y-axis labels (Imaginary labels)
        factor = 1.5
        self.play(Indicate(coord_labels[4], factor), Indicate(coord_labels[5], factor))
        self.wait(0.1)
        self.next_slide()

        dot = Circle(0.07, BLUE, fill_opacity=1)

        label = VGroup(
            DecimalNumber(), DecimalNumber(include_sign=True), MathTex("\, i")
        )

        def update_label(mobject):
            mobject[0].set_value(plane.p2c(dot.get_center())[0])
            mobject[1].set_value(plane.p2c(dot.get_center())[1])
            mobject.arrange(buff=0.05)
            mobject.next_to(dot, UR)

        label.add_updater(update_label)

        self.play(FadeIn(dot, scale=0), Write(label))
        self.wait(0.1)
        self.next_slide()

        self.start_loop()
        self.play(dot.animate.move_to(plane.n2p(1)))
        self.wait(0.5)
        self.play(dot.animate.move_to(plane.n2p(-1)))
        self.wait(0.5)
        self.play(dot.animate.move_to(plane.n2p(0)))
        self.wait()
        self.end_loop()

        self.wait()
        self.start_loop()
        self.play(dot.animate.move_to(plane.n2p(1j)))
        self.wait(0.5)
        self.play(dot.animate.move_to(plane.n2p(-1j)))
        self.wait(0.5)
        self.play(dot.animate.move_to(plane.n2p(0)))
        self.wait()
        self.end_loop()

        self.wait()
        self.play(dot.animate.move_to(plane.n2p(1 + 0.5j)))
        self.wait(0.5)
        self.play(dot.animate.move_to(plane.n2p(-2 + 1j)))
        self.wait(0.5)
        self.play(dot.animate.move_to(plane.n2p(-1.5 + 0.2j)))
        self.wait(0.5)
        self.play(dot.animate.move_to(plane.n2p(-0.5 - 0.7j)))
        self.wait(0.5)
        self.play(dot.animate.move_to(plane.n2p(1 - 1j)))
        self.wait(0.5)
        self.play(dot.animate.move_to(plane.n2p(0.7 + 0.3j)))
        self.wait(0.5)
        self.play(dot.animate.move_to(plane.n2p(0)))
        self.wait(0.1)
        self.next_slide()

        self.play(FadeOut(dot, label), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        dot2 = dot.copy()
        label = MathTex("z_1")
        label2 = MathTex("z_2")
        dot.move_to(plane.n2p(0.5 + 1j))
        label.next_to(dot, UR)
        dot2.move_to(plane.n2p(1 - 0.5j))
        label2.next_to(dot2, UR)

        self.play(Create(dot), Write(label), Create(dot2), Write(label2), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        complex_sum_tex = MathTex(
            r"z_1 &= a + bi \\ ",
            r"z_2 &= c + di \\ ",
            r"z_1 + z_2 &= (a + c) + (b + d)i",
        )
        complex_sum_tex.shift(LEFT * 3).scale(1.2)
        complex_sum_rect = SurroundingRectangle(
            complex_sum_tex, buff=0.4, corner_radius=0.2
        )
        complex_sum_rect.set_stroke(width=3)
        complex_sum_rect.set_fill(color=BLACK, opacity=0.5)
        complex_sum_tex.set_z_index(1)

        self.play(
            AnimationGroup(
                FadeIn(complex_sum_rect, scale=0.6),
                Write(complex_sum_tex),
                lag_ratio=0.9,
                run_time=1.6,
            )
        )
        self.wait(0.1)
        self.next_slide()

        parts = VGroup(complex_sum_tex[0][3].copy(), complex_sum_tex[1][3].copy())
        parts.generate_target()
        parts.target = VGroup(complex_sum_tex[2][7], complex_sum_tex[2][9])

        self.play(
            AnimationGroup(
                Indicate(complex_sum_tex[0][3]), Indicate(complex_sum_tex[1][3])
            )
        )
        self.play(MoveToTarget(parts))
        self.remove(parts)
        self.wait(0.1)
        self.next_slide()

        parts = VGroup(complex_sum_tex[0][5].copy(), complex_sum_tex[1][5].copy())
        parts.generate_target()
        parts.target = VGroup(complex_sum_tex[2][13], complex_sum_tex[2][15])

        self.play(
            AnimationGroup(
                Indicate(complex_sum_tex[0][5]), Indicate(complex_sum_tex[1][5])
            )
        )
        self.play(MoveToTarget(parts))
        self.remove(parts)
        self.wait(0.1)
        self.next_slide()

        self.play(FadeOut(complex_sum_tex, complex_sum_rect, scale=0.6))
        self.wait(0.1)
        self.next_slide()

        # Vector sum
        vec = Vector([dot.get_x(), dot.get_y()])
        vec2 = Vector([dot2.get_x(), dot2.get_y()])
        self.play(Create(vec, lag_ratio=0.7), Create(vec2, lag_ratio=0.7))
        self.wait(0.1)
        self.next_slide()

        vec2_copy = vec2.copy()
        self.play(vec2_copy.animate.move_to(plane.n2p(1 + 0.75j)), run_time=0.5)

        dot3 = dot.copy()
        dot3.move_to(plane.n2p(1.5 + 0.5j))
        vec3 = Vector(plane.n2p(1.5 + 0.5j))
        label3 = MathTex("z_1 + z_2")
        label3.next_to(dot3, UR)

        self.play(Create(vec3, lag_ratio=0.5))
        self.play(AnimationGroup(FadeIn(dot3), Write(label3)), lag_ratio=0.3)
        self.wait(0.1)
        self.next_slide()

        self.play(
            FadeOut(dot, dot2, dot3, vec, vec2, vec2_copy, vec3, label, label2, label3),
            run_time=0.5,
        )
        self.wait(0.1)
        self.next_slide()

        unit_circle = Circle.from_three_points(
            *(plane.n2p(1), plane.n2p(-1), plane.n2p(1j)),
            color=GREEN,
        )

        self.play(Create(unit_circle))
        self.wait(0.1)
        self.next_slide()

        def create_point_on_unit_circle(
            angle: float,
            text: str,
            arc_radius: float,
            color: str,
            angle_text: bool = True,
        ):
            objs = {}
            objs["point"] = unit_circle.point_at_angle(angle)
            objs["circle"] = Circle(0.07, color=color, fill_opacity=1)
            objs["label"] = MathTex(rf"\cos {text} + i \sin {text}")
            objs["label"].scale(0.7).next_to(objs["point"], objs["point"], 0.1)

            objs["path"] = Arc(radius=plane.get_x_unit_size(), angle=angle)
            objs["segment"] = Line(plane.n2p(0), plane.n2p(1))
            objs["arc"] = Arc(
                plane.get_x_unit_size() * arc_radius, angle=angle, color=color
            )

            text_anim = Wait(run_time=0)
            if angle_text:
                objs["text"] = MathTex(text)
                objs["text"].scale(0.6).move_to(plane.pr2pt(0.32, angle * 0.5))
                text_anim = Write(objs["text"])

            objs["circle"].move_to(plane.n2p(1)).set_z_index(1)

            self.play(
                AnimationGroup(
                    Create(objs["segment"], run_time=0.5),
                    GrowFromCenter(objs["circle"], run_time=0.5),
                    lag_ratio=0.7,
                )
            )
            self.play(
                AnimationGroup(
                    MoveAlongPath(objs["circle"], objs["path"]),
                    Rotate(objs["segment"], angle=angle, about_point=plane.n2p(0)),
                    Create(objs["arc"]),
                    lag_ratio=0,
                )
            )
            self.play(
                AnimationGroup(
                    text_anim,
                    Flash(
                        objs["point"],
                        line_length=0.1,
                        flash_radius=0.2,
                        line_stroke_width=2,
                    ),
                    Write(objs["label"], run_time=0.8),
                    lag_ratio=0.3,
                )
            )

            displayed_mobjs = []
            for key in "segment circle arc label".split():
                displayed_mobjs.append(objs[key])
            if angle_text:
                displayed_mobjs.append(objs["text"])

            return objs, displayed_mobjs

        alpha = PI * 3 / 17
        alpha_objs, alpha_mobjs = create_point_on_unit_circle(
            alpha, r"\alpha", 0.25, RED
        )
        self.wait(0.1)
        self.next_slide()

        alpha_x = Line(plane.n2p(0), (alpha_objs["point"][0], 0, 0))
        alpha_x_label = MathTex(r"\cos \alpha").scale(0.7).next_to(alpha_x, DOWN)
        alpha_y = Line((alpha_objs["point"][0], 0, 0), alpha_objs["point"])
        alpha_y_label = MathTex(r"\sin \alpha").scale(0.7).next_to(alpha_y, RIGHT)

        self.play(Create(alpha_x), Write(alpha_x_label))
        self.wait(0.1)
        self.next_slide()
        self.play(Create(alpha_y), Write(alpha_y_label))
        self.wait(0.1)
        self.next_slide()

        self.play(
            Uncreate(
                VGroup(alpha_x, alpha_x_label, alpha_y, alpha_y_label), run_time=0.6
            )
        )
        self.wait(0.1)
        self.next_slide()

        beta = PI * 7 / 11
        beta_objs, beta_mobjs = create_point_on_unit_circle(beta, r"\beta", 0.225, BLUE)
        self.wait(0.1)
        self.next_slide()

        angle_sum = alpha + beta
        angle_sum_objs, angle_sum_mobjs = create_point_on_unit_circle(
            angle_sum, r"( \alpha + \beta )", 0.2, PURPLE, False
        )
        self.wait(0.1)
        self.next_slide()

        self.play(AnimationGroup(FadeOut(*beta_mobjs, *angle_sum_mobjs)))
        self.wait(0.1)
        self.next_slide()

        alpha_mobjs.append(MathTex(" = z").scale(0.7).next_to(alpha_objs["label"]))
        self.play(Write(alpha_mobjs[-1]), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        alpha_double = {
            "segment": alpha_objs["segment"].copy(),
            "circle": alpha_objs["circle"].copy(),
            "arc": alpha_objs["arc"].copy(),
        }
        self.play(
            AnimationGroup(
                *[
                    Rotate(alpha_double[key], angle=alpha, about_point=plane.n2p(0))
                    for key in ["segment", "circle", "arc"]
                ]
            )
        )
        alpha_double["label"] = (
            MathTex(r"z ^ 2")
            .scale(0.7)
            .next_to(alpha_double["segment"], alpha_double["segment"].get_center(), 0.2)
        )
        alpha_double["text"] = (
            MathTex(r"\alpha").scale(0.6).move_to(plane.pr2pt(0.32, alpha * 1.5))
        )
        self.play(
            Write(alpha_double["label"]), Write(alpha_double["text"]), run_time=0.5
        )
        self.wait(0.1)
        self.next_slide()

        alpha_triple = {
            "segment": alpha_objs["segment"].copy(),
            "circle": alpha_objs["circle"].copy(),
            "arc": alpha_objs["arc"].copy(),
        }
        self.play(
            AnimationGroup(
                *[
                    Rotate(alpha_triple[key], angle=2 * alpha, about_point=plane.n2p(0))
                    for key in ["segment", "circle", "arc"]
                ]
            )
        )
        alpha_triple["label"] = (
            MathTex(r"z ^ 3")
            .scale(0.7)
            .next_to(alpha_triple["segment"], alpha_triple["segment"].get_center(), 0.2)
        )
        alpha_triple["text"] = (
            MathTex(r"\alpha").scale(0.6).move_to(plane.pr2pt(0.32, alpha * 2.5))
        )
        self.play(
            Write(alpha_triple["label"]), Write(alpha_triple["text"]), run_time=0.5
        )
        self.wait(0.1)
        self.next_slide()

        equation = MathTex("x^n = 1")
        equation.scale(0.9).shift(RIGHT * 4.5 + UP * 3)
        self.play(Write(equation), run_time=0.4)
        self.wait(0.1)
        self.next_slide()

        self.play(
            *[FadeOut(i) for i in alpha_mobjs],
            *[FadeOut(i) for _, i in alpha_double.items()],
            *[FadeOut(i) for _, i in alpha_triple.items()],
            run_time=0.5,
        )

        plane.generate_target()
        plane.target = ComplexPlane(
            x_range=(-1.2, 1.2, 1),
            y_range=(-1.2, 1.2, 1),
            x_length=4,
            y_length=4,
            faded_line_ratio=4,
        ).shift(LEFT * 3.8)
        coord_labels.generate_target()
        coord_labels.target = plane.target.get_coordinate_labels()
        unit_circle.generate_target()
        unit_circle.target = Circle.from_three_points(
            *(plane.target.n2p(1), plane.target.n2p(-1), plane.target.n2p(1j)),
            color=GREEN,
        )
        self.play(
            ReplacementTransform(plane, plane.target),
            MoveToTarget(coord_labels),
            MoveToTarget(unit_circle),
            equation.animate.shift(LEFT * 4.4, DOWN * 0.7),
        )
        plane = plane.target

        self.wait(0.1)
        self.next_slide()

        roots_tex = MathTex(r"\cos {2 \pi m \over n} + i \sin {2 \pi m \over n}")
        roots_tex.scale(0.7).next_to(equation, DOWN, 0.8, aligned_edge=LEFT)
        self.play(Write(roots_tex), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        roots_tex_2 = MathTex(
            r"&(",
            r"\cos {2 \pi m \over n} + i \sin {2 \pi m \over n}",
            r")",
            r"^n \\ ",
            r"&= \cos {2 \pi m} + i \sin {2 \pi m} \\ ",
            r"&= 1",
        )
        roots_tex_2.scale(0.7).next_to(equation, DOWN, 0.8, aligned_edge=LEFT)

        self.play(TransformMatchingTex(roots_tex, roots_tex_2))
        self.wait(0.1)
        self.next_slide()

        self.play(TransformMatchingTex(roots_tex_2, roots_tex, shift=ORIGIN))
        self.wait(0.1)
        self.next_slide()

        roots_tex_3 = MathTex(
            "= (", r"\cos {2 \pi \over n} + i \sin {2 \pi \over n}", ")^m"
        )
        roots_tex_3.scale(0.7).next_to(roots_tex, DOWN, aligned_edge=LEFT)

        self.play(Write(roots_tex_3), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        z = MathTex(
            "& z = ",
            r"\cos {2 \pi \over n} + i \sin {2 \pi \over n}",
            r"\\ & z^0, z^1, \cdots, z^{n-1}",
        )
        z.scale(0.7).next_to(roots_tex_3, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(TransformMatchingShapes(roots_tex_3.copy(), z[:2]), run_time=0.7)
        self.wait(0.1)
        self.next_slide()
        self.play(Write(z[2]), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(
            AnimationGroup(
                FadeOut(roots_tex, roots_tex_3),
                z.animate.next_to(equation, DOWN, 0.5, aligned_edge=LEFT),
                lag_ratio=0.8,
                run_time=1,
            )
        )
        self.wait(0.1)
        self.next_slide()

        # Iterate n = 1 to n = 6
        n_tex = MathTex("n = 1")
        n_tex.scale(0.7).next_to(plane, DOWN, 0.8)
        n_tex.generate_target()

        for n in range(1, 7):
            anim = []
            if n > 1:
                n_tex.target = MathTex(f"n = {n}")
                n_tex.target.scale(0.7).move_to(n_tex)
                anim.append(MoveToTarget(n_tex))
                anim.append(FadeOut(*root_segments, *root_points))
            root_points = [
                Circle(0.07, YELLOW, fill_opacity=1).move_to(
                    unit_circle.point_at_angle(2 * PI * i / n)
                )
                for i in range(n)
            ]
            root_segments = [
                Line(plane.n2p(0), unit_circle.point_at_angle(2 * PI * i / n))
                for i in range(n)
            ]
            if n == 1:
                anim.append(FadeIn(*root_segments, *root_points))
                anim.append(Write(n_tex))
            else:
                anim.append(FadeIn(*root_segments, *root_points))
            self.play(*anim, run_time=0.8)
            self.wait(0.1)
            self.next_slide()

        self.play(FadeOut(n_tex), run_time=0.7)
        self.wait(0.3)

        # Show roots sum equation
        roots_sum = MathTex(
            r"S_k = ",
            r"\sum^{n-1}_{m=0}",
            r"&(",
            r"z^m",
            r")",
            r"^k",
            r"\qquad (k \in \mathbb{Z})",
        ).scale(0.7)
        roots_sum.next_to(z, DOWN, 0.4, LEFT)
        self.play(Write(roots_sum), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        roots_sum_result = MathTex(
            r"S_k = {\begin{cases} n & (k = \cdots, -2n, -n, 0, n, 2n, \cdots) \\ 0 & (otherwise) \end{cases}}",
        )
        roots_sum_result.scale(0.7).next_to(roots_sum, DOWN, 0.45, LEFT)
        self.play(Write(roots_sum_result), run_time=1)
        self.wait(0.1)
        self.next_slide()

        # Iterate k = 1 to k = 6 and show average point
        k_tex = MathTex("k = 1")
        avg_point = Circle(0.08, BLUE, fill_opacity=1).move_to(plane.n2p(0))
        k_tex.scale(0.7).next_to(plane, DOWN, 0.8)
        self.play(FadeIn(k_tex), run_time=0.3)
        self.wait(0.1)
        self.next_slide()

        self.play(
            AnimationGroup(
                FadeIn(avg_point, scale=0.5),
                Flash(avg_point, color=BLUE),
                run_time=0.7,
            )
        )
        self.wait(0.1)
        self.next_slide()
        self.play(FadeOut(avg_point, scale=0.5), run_time=0.4)
        self.wait(0.1)
        self.next_slide()

        k_tex.generate_target()
        for i in range(2, 7):
            k_tex.target = MathTex(f"k = {i}")
            k_tex.target.scale(0.7).move_to(k_tex)
            self.play(ReplacementTransform(k_tex, k_tex.target), run_time=0.4)
            k_tex = k_tex.target
            anim = []
            for j in range(n):
                anim.append(
                    Rotate(root_points[j], 2 * PI * j / n, about_point=plane.n2p(0))
                )
                anim.append(
                    Rotate(root_segments[j], 2 * PI * j / n, about_point=plane.n2p(0))
                )
            self.play(*anim, run_time=2.2)
            self.wait(0.1)
            self.next_slide()

            if i == 6:
                avg_point.move_to(plane.n2p(1))
            self.play(
                AnimationGroup(
                    FadeIn(avg_point, scale=0.5),
                    Flash(avg_point, color=BLUE),
                    run_time=0.7,
                )
            )
            self.wait(0.1)
            self.next_slide()
            self.play(FadeOut(avg_point, scale=0.5), run_time=0.4)
            self.wait(0.1)
            self.next_slide()

        # Remove complex plane and show geometric series equations
        to_remove = Group(
            k_tex, coord_labels, plane, unit_circle, *root_points, *root_segments
        )
        self.play(FadeOut(to_remove, scale=0.5), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        series = MathTex(
            r"S_k ",
            r"&= \sum^{n-1}_{m=0} (z^m)^k \\ ",
            r"&= \sum^{n-1}_{m=0} (z^k)^m \\ ",
            r"&= (z^k)^0 + (z^k)^1 + \cdots + (z^k)^{n-1} \\ ",
            r"&= { 1 - (z^k)^n \over 1 - z^k}",
            r"\quad (z^k \ne  1) \\ ",
            r"&= 0",
        )
        series.scale(0.7).next_to(equation, LEFT, aligned_edge=UP)

        anim = [
            AnimationGroup(Write(series[0]), Write(series[1]), run_time=0.6),
            AnimationGroup(
                Transform(series[1][:10].copy(), series[2][:10]),
                Transform(series[1][10].copy(), series[2][12]),
                Transform(series[1][11].copy(), series[2][11]),
                Transform(series[1][12].copy(), series[2][10]),
                run_time=0.7,
            ),
            Write(series[3], run_time=0.3),
            Write(series[4], run_time=0.3),
            FadeIn(series[5], shift=LEFT * 0.2, scale=1.4),
            Indicate(series[4][3:8]),
            Write(series[6], run_time=0.3),
        ]

        for a in anim:
            self.play(a)
            self.wait(0.1)
            self.next_slide()

        self.play(FadeOut(*self.mobjects), run_time=0.5)
        self.wait(0.1)
        self.next_slide()


class ValueToCoeffCubic(Slide):
    def construct(self):
        polynomial = MathTex("f(x) = ax^3 + bx^2 + cx + d")
        polynomial.shift(UP * 3)
        self.play(Write(polynomial), run_time=0.4)
        self.wait(0.1)
        self.next_slide()

        z = MathTex(r"z = \cos {2 \pi \over 4} + i \sin {2 \pi \over 4}")
        z.next_to(polynomial[0][4], DOWN, 1, submobject_to_align=z[0][1])
        self.play(Write(z), run_time=0.3)
        self.wait(0.1)
        self.next_slide()

        z_is_i = MathTex("\; ( = i)")
        z_is_i.scale(0.8).next_to(z)
        self.play(FadeIn(z_is_i), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(FadeOut(z_is_i), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        values = VGroup(
            *[
                MathTex(
                    f"f(z^{i})",
                    " = ",
                    f"a (z^{i})^3",
                    " + ",
                    f"b (z^{i})^2",
                    " + ",
                    f"c (z^{i})^1",
                    " + ",
                    f"d (z^{i})^0",
                )
                for i in range(4)
            ]
        ).arrange(DOWN)
        values.scale(0.8).next_to(z, DOWN, 0.5).set_x(0)
        self.play(
            AnimationGroup(*[Write(i) for i in values], lag_ratio=0.3, run_time=1)
        )
        self.wait(0.1)
        self.next_slide()

        line = Line(LEFT * 4.5, RIGHT * 4.5, stroke_width=1.5)
        line.next_to(values, DOWN)

        sum = MathTex(
            r"\sum_{k=0}^3 f(z^k)",
            " = ",
            "0 a",
            " + ",
            "0 b",
            " + ",
            "0 c",
            " + ",
            "4 d",
        )
        sum.scale(0.8)
        sum.next_to(values[-1][1], DOWN, 1.2, submobject_to_align=sum[1])
        for i in range(2, 9):
            sum[i].match_x(values[-1][i])
        self.play(
            AnimationGroup(
                Create(line),
                Write(sum),
                lag_ratio=0.5,
                run_time=1,
            )
        )
        self.wait(0.1)
        self.next_slide()

        for i in range(4):
            rect = SurroundingRectangle(
                Group(*[values[j][2 * i + 2][1:] for j in range(4)]),
                buff=0.05,
            )
            self.play(Create(rect), run_time=0.5)
            self.wait(0.1)
            self.next_slide()
            self.play(Indicate(sum[2 * i + 2][0]))
            self.wait(0.1)
            self.next_slide()
            self.play(FadeOut(rect), run_time=0.3)

        self.wait(0.1)
        self.next_slide()

        values.generate_target()
        values.target = VGroup(
            *[
                MathTex(
                    f"z^{{-{i}}} f(z^{i})",
                    " = ",
                    f"a (z^{i})^2",
                    " + ",
                    f"b (z^{i})^1",
                    " + ",
                    f"c (z^{i})^0",
                    " + ",
                    f"d (z^{i})^{{-1}}",
                )
                for i in range(4)
            ]
        ).arrange(DOWN, index_of_submobject_to_align=1)
        values.target.scale(0.8)
        for i in range(4):
            values.target[i].match_y(values[i])

        # BUG Incorect transform of plus signs on the second row
        anim = []
        for i, j in zip(values, values.target):
            for l in [0, 1, 3, 5, 7]:
                anim.append(TransformMatchingShapes(i[l], j[l]))
            for l in [2, 4, 6, 8]:
                anim.append(TransformMatchingShapes(i[l][:-1], j[l][:-1]))
                anim.append(ReplacementTransform(i[l][-1], j[l][-1]))
        self.play(*anim)
        self.wait(0.1)
        self.next_slide()

        sum.generate_target()
        sum.target = MathTex(
            r"\sum_{k=0}^3 z^{-k} f(z^k)",
            " = ",
            "0 a",
            " + ",
            "0 b",
            " + ",
            "4 c",
            " + ",
            "0 d",
        )
        sum.target.scale(0.8)
        sum.target.next_to(
            values.target[-1][1], DOWN, 1.2, submobject_to_align=sum.target[1]
        )
        for i in range(2, 9):
            sum.target[i].match_x(values.target[-1][i])
        self.play(TransformMatchingShapes(sum, sum.target))
        self.wait(0.1)
        self.next_slide()

        values = values.target
        sum = sum.target

        for i in range(4):
            rect = SurroundingRectangle(
                Group(*[values[j][2 * i + 2][1:] for j in range(4)]),
                buff=0.05,
            )
            self.play(Create(rect), run_time=0.5)
            self.wait(0.1)
            self.next_slide()
            self.play(Indicate(sum[2 * i + 2][0]))
            self.wait(0.1)
            self.next_slide()
            self.play(FadeOut(rect), run_time=0.3)
        self.wait(0.1)
        self.next_slide()

        for k in (2, 3):
            values.generate_target()
            values.target = VGroup(
                *[
                    MathTex(
                        f"(z^{{-{i}}})^{k} f(z^{i})",
                        " = ",
                        f"a (z^{i})^{{{3-k}}}",
                        " + ",
                        f"b (z^{i})^{{{2-k}}}",
                        " + ",
                        f"c (z^{i})^{{{1-k}}}",
                        " + ",
                        f"d (z^{i})^{{{-k}}}",
                    )
                    for i in range(4)
                ]
            ).arrange(DOWN, index_of_submobject_to_align=1)
            values.target.scale(0.8)
            for i in range(4):
                values.target[i].match_y(values[i])
            anim = []
            for i, j in zip(values, values.target):
                if k < 3:
                    anim.append(TransformMatchingShapes(i[0], j[0]))
                else:
                    anim.append(TransformMatchingShapes(i[0][:5], j[0][:5]))
                    anim.append(Transform(i[0][5], j[0][5]))
                    anim.append(TransformMatchingShapes(i[0][6:], j[0][6:]))
                for l in [1, 3, 5, 7]:
                    anim.append(TransformMatchingShapes(i[l], j[l]))
                for l in [2, 4, 6, 8]:
                    anim.append(TransformMatchingShapes(i[l][:-1], j[l][:-1]))
                    anim.append(ReplacementTransform(i[l][-1], j[l][-1]))

            sum.generate_target()
            sum.target = MathTex(
                rf"\sum_{{k=0}}^3 (z^{{-k}})^{k} f(z^k)",
                " = ",
                f"{(k-2)*4} a",
                " + ",
                f"{(3-k)*4} b",
                " + ",
                "0 c",
                " + ",
                "0 d",
            )
            sum.target.scale(0.8)
            sum.target.next_to(
                values.target[-1][1], DOWN, 1.2, submobject_to_align=sum.target[1]
            )
            for i in range(2, 9):
                sum.target[i].match_x(values.target[-1][i])
            if k < 3:
                anim.append(TransformMatchingShapes(sum, sum.target))
            else:
                anim += [
                    TransformMatchingShapes(sum[0][:10], sum.target[0][:10]),
                    Transform(sum[0][10], sum.target[0][10]),
                    TransformMatchingShapes(sum[0][11:], sum.target[0][11:]),
                    TransformMatchingShapes(sum[1:], sum.target[1:]),
                ]
            self.play(*anim)
            self.wait(0.1)
            self.next_slide()

            values = values.target
            sum = sum.target

            rect = SurroundingRectangle(
                Group(*[values[j][8 - 2 * k][1:] for j in range(4)]),
                buff=0.05,
            )
            self.play(
                AnimationGroup(
                    Create(rect),
                    Indicate(sum[8 - 2 * k][0]),
                    run_time=1,
                    lag_ratio=0.7,
                )
            )
            self.play(FadeOut(rect), run_time=0.3)
            self.wait(0.1)
            self.next_slide()

        self.play(FadeOut(*self.mobjects), run_time=0.8)
        self.wait(0.1)
        self.next_slide()


class ValueToCoeff(Slide):
    """
    다항함수 함숫값 -> 계수 구하기
    """

    def construct(self):
        polynomial = MathTex(r"f(x) = \sum_{k=0}^{n-1} c_k x", r"^k")
        sum = MathTex(r"c_m = {1 \over n} \sum_{k=0}^{n-1} (z^k)^{-m} f(z^k)")
        z = MathTex(r"z = \cos {2 \pi \over n} + i \sin {2 \pi \over n}")
        Group(polynomial, sum, z).arrange(DOWN, buff=1)

        self.play(Write(polynomial), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(Write(sum), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(Write(z), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        z.save_state()
        self.play(
            AnimationGroup(
                FadeOut(polynomial, sum),
                z.animate.move_to(UP * 2 + LEFT * 2.5),
                lag_ratio=0.5,
            )
        )
        self.wait(0.1)
        self.next_slide()

        z_equation = VGroup(
            MathTex(r"x^n - 1", r"= 0"),
            MathTex(r"(x-z^0)(x-z^1)(x-z^2) \cdots (x-z^{n-1})", r"= 0"),
        )
        z_equation.scale(0.9).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        z_equation.next_to(z, DOWN, 0.6, LEFT)

        self.play(Write(z_equation[0]), run_time=0.5)
        self.wait(0.1)
        self.next_slide()
        self.play(TransformFromCopy(z_equation[0], z_equation[1]), run_time=0.9)
        self.wait(0.1)
        self.next_slide()

        z_sum = MathTex(
            r"{1 \over n} \sum ^{n-1} _{m=0} (z^m)^k",
            "=",
            r"\begin{cases} 1 & (k = \cdots, -2n, -n, 0, n, 2n, \cdots) \\ 0 & (otherwise) \end{cases}",
        )
        z_sum.scale(0.9).next_to(z_equation, DOWN, 0.7, LEFT)

        self.play(Write(z_sum), run_time=0.7)
        self.wait(0.1)
        self.next_slide()

        self.play(
            AnimationGroup(
                FadeOut(z_equation, z_sum),
                z.animate.restore(),
                FadeIn(polynomial, sum),
                lag_ratio=0.5,
            )
        )
        self.wait(0.1)
        self.next_slide()

        self.play(VGroup(polynomial, sum, z).animate.shift(LEFT * 3.2), run_time=0.9)
        self.wait(0.1)
        self.next_slide()

        # m = 0
        sum_0 = VGroup(
            MathTex(
                r"c_0 = ",
                r"{1 \over n} \sum_{k=0}^{n-1}",
                r"(z^k)^{-0}",
                r"f(z^k)",
            ),
            MathTex(
                r"= ",
                r"{1 \over n}",
                r"\sum_{k=0}^{n-1}",
                r"\sum_{j=0}^{n-1}",
                r"c_j",
                r"(z^k)^j",
            ),
            MathTex(
                r"= ",
                r"{1 \over n}",
                r"\sum_{k=0}^{n-1}",
                r"\sum_{j=0}^{n-1}",
                r"c_j",
                r"(z^k)^j",
            ),
        )
        sum_0.scale(0.9).arrange(DOWN)
        sum_0.shift(RIGHT * 3)
        target_x = sum_0[0][0].get_right()
        for i in sum_0:
            x_diff = target_x - i[0].get_right()
            i.shift(x_diff * RIGHT)

        self.play(Write(sum_0[0]), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        sum_0[0].generate_target()
        sum_0[0].target = MathTex(
            r"c_0 = ",
            r"{1 \over n} \sum_{k=0}^{n-1}",
            r"f(z^k)",
        )
        sum_0[0].target.scale(0.9).align_to(sum_0[0], UL)

        self.play(
            TransformMatchingTex(sum_0[0], sum_0[0].target, shift=LEFT * 0.3, scale=0.4)
        )
        sum_0[0] = sum_0[0].target
        self.wait(0.1)
        self.next_slide()

        underline = Underline(sum_0[0][2], color=YELLOW, stroke_width=3)
        self.play(Create(underline), run_time=0.5)
        self.play(Indicate(polynomial))
        self.wait(0.1)
        self.next_slide()

        self.play(Uncreate(underline), run_time=0.5)
        self.play(Write(sum_0[1]), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        sum_0[2].save_state()
        sum_0[2].move_to(sum_0[1])
        self.play(Restore(sum_0[2]))
        self.wait(0.1)
        self.next_slide()

        sum_0[2].generate_target()
        sum_0[2].target = MathTex(
            r"= ",
            r"{1 \over n}",
            r"\sum_{j=0}^{n-1}",
            r"\sum_{k=0}^{n-1}",
            r"c_j",
            r"(z^k)^j",
        )
        sum_0[2].target.scale(0.9).move_to(sum_0[2], aligned_edge=LEFT)
        self.play(TransformMatchingTex(sum_0[2], sum_0[2].target))
        sum_0[2] = sum_0[2].target
        self.wait(0.1)
        self.next_slide()

        sum_0[2].target = MathTex(
            r"= ",
            r"{1 \over n}",
            r"\sum_{j=0}^{n-1}",
            r"c_j",
            r"\sum_{k=0}^{n-1}",
            r"(z^k)^j",
        )
        sum_0[2].target.scale(0.9).move_to(sum_0[2], aligned_edge=LEFT)
        self.play(TransformMatchingTex(sum_0[2], sum_0[2].target))
        sum_0[2] = sum_0[2].target
        self.wait(0.1)
        self.next_slide()

        sum_0[2].target = MathTex(
            r"= ",
            r"\sum_{j=0}^{n-1}",
            r"c_j",
            r"{1 \over n}",
            r"\sum_{k=0}^{n-1}",
            r"(z^k)^j",
        )
        sum_0[2].target.scale(0.9).move_to(sum_0[2], aligned_edge=LEFT)
        self.play(TransformMatchingTex(sum_0[2], sum_0[2].target))
        sum_0[2] = sum_0[2].target
        self.wait(0.1)
        self.next_slide()

        self.play(Indicate(sum_0[2][3:]))
        self.wait(0.1)
        self.next_slide()

        self.play(FadeOut(sum_0), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        # m = 1
        sum_1 = VGroup(
            MathTex(
                r"c_1 = ",
                r"{1 \over n} \sum_{k=0}^{n-1}",
                r"(z^k)^{-1}",
                r"f(z^k)",
            ),
            MathTex(
                r"= ",
                r"{1 \over n}",
                r"\sum_{k=0}^{n-1}",
                r"\sum_{j=0}^{n-1}",
                r"c_j",
                r"(z^k)^{j-1}",
            ),
            MathTex(
                r"= ",
                r"\sum_{j=0}^{n-1}",
                r"c_j",
                r"{1 \over n}",
                r"\sum_{k=0}^{n-1}",
                r"(z^k)^{j-1}",
            ),
        )
        sum_1.scale(0.9).arrange(DOWN)
        sum_1.shift(RIGHT * 3)
        target_x = sum_1[0][0].get_right()
        for i in sum_1:
            x_diff = target_x - i[0].get_right()
            i.shift(x_diff * RIGHT)

        self.play(Write(sum_1[0]), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        polynomial.generate_target()
        polynomial.target = MathTex(
            r"x", r"^{-1}", r"f(x) = \sum_{k=0}^{n-1} c_k x", r"^{k-1}"
        )
        polynomial_x = polynomial[0].get_left()
        polynomial.target.shift(polynomial_x - polynomial.target[2].get_left())
        self.play(TransformMatchingTex(polynomial, polynomial.target, shift=ORIGIN))
        polynomial = polynomial.target
        self.wait(0.1)
        self.next_slide()

        self.play(Write(sum_1[1]), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        self.play(Write(sum_1[2]), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        self.play(Indicate(sum_1[2][3:]))
        self.wait(0.1)
        self.next_slide()

        self.play(Circumscribe(sum_1[2][5][4:]))
        self.wait(0.1)
        self.next_slide()

        self.play(FadeOut(sum_1), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        # m = m
        sum_m = VGroup(
            MathTex(
                r"c_m = ",
                r"{1 \over n} \sum_{k=0}^{n-1}",
                r"(z^k)^{-m}",
                r"f(z^k)",
            ),
            MathTex(
                r"= ",
                r"{1 \over n}",
                r"\sum_{k=0}^{n-1}",
                r"\sum_{j=0}^{n-1}",
                r"c_j",
                r"(z^k)^{j-m}",
            ),
            MathTex(
                r"= ",
                r"\sum_{j=0}^{n-1}",
                r"c_j",
                r"{1 \over n}",
                r"\sum_{k=0}^{n-1}",
                r"(z^k)^{j-m}",
            ),
        )
        sum_m.scale(0.9).arrange(DOWN)
        sum_m.shift(RIGHT * 3)
        target_x = sum_m[0][0].get_right()
        for i in sum_m:
            x_diff = target_x - i[0].get_right()
            i.shift(x_diff * RIGHT)

        self.play(Write(sum_m[0]), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        polynomial.target = MathTex(
            r"x", r"^{-m}", r"f(x) = \sum_{k=0}^{n-1} c_k x", r"^{k-m}"
        )
        polynomial.target.shift(polynomial_x - polynomial.target[2].get_left())
        self.play(TransformMatchingTex(polynomial, polynomial.target))
        polynomial = polynomial.target
        self.wait(0.1)
        self.next_slide()

        self.play(Write(sum_m[1]), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        self.play(Write(sum_m[2]), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        self.play(Indicate(sum_m[2][3:]))
        self.wait(0.1)
        self.next_slide()

        self.play(FadeOut(*self.mobjects), run_time=0.5)
        self.wait(0.1)
        self.next_slide()


class ApplyValueToCoeff(Slide):
    def construct():
        # TODO Calculate c_8
        pass


class Integral(Slide):
    """
    적분식 표현, 삼각함수 거듭제곱 적분, 최종 계산 결과
    """

    def construct(self):
        integral = MathTex(r"\int^1_0 \cos^n{2 \pi x} \> dx").scale(1.2)
        integral_calc = MathTex(
            r"I_n &= ",
            r"\int^1_0 \cos^n {2 \pi x} \> dx \\ ",
            r"&= \int^1_0 \{ 1 - \sin^2 {2 \pi x} \} \, \cos^{n-2} {2 \pi x} \> dx \\ ",
            r"&= I_{n-2} - \int^1_0 \cos^{n-2} {2 \pi x} \, \sin^2 {2 \pi x} \> dx \\",
            r"&= I_{n-2} - \bigl[ \sin {2 \pi x} \cdot \{ - {1 \over 2 \pi (n-1)} \, \cos^{n-1} {2 \pi x} \} \bigr]^1_0 \\",
            r"& + \int^1_0 2 \pi \, \cos {2 \pi x} \, \{ - {1 \over 2 \pi (n-1)} \, \cos^{n-1} {2 \pi x} \} \> dx",
        )
        integral_calc.scale(0.8).shift(LEFT * 1.5)
        integral.match_y(integral_calc[0])

        self.play(Write(integral), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        integral_1 = MathTex(
            r"I_1 = & \int^1_0 \cos {2 \pi x} \> dx \\ ",
            r"= & \bigl[ {1 \over 2 \pi} \sin {2 \pi x} \bigr] ^1 _0 \\ ",
            r"= & 0",
        )
        integral_1.shift(RIGHT * 2.2)

        integral_2 = MathTex(
            r"I_2 = & \int^1_0 \cos^2 {2 \pi x} \> dx \\ ",
            r"= & \int^1_0 {\cos {4 \pi x} + 1 \over 2 } \> dx \\ ",
            r"= & \bigl[ {1 \over 8 \pi} \sin( 4 \pi x) + {1 \over 2} x \bigr] ^1 _0 \\ ",
            r"= & 1 \over 2",
        )
        integral_2.align_to(integral_1, LEFT)

        integral_1_2 = MathTex(r"I_1 = & 0 \\ ", r"I_2 = & 1 \over 2")
        integral_1_2.scale(0.7).shift(UP * 2.6 + RIGHT * 4.5)

        self.play(TransformMatchingShapes(integral, integral_calc[:2]))
        self.wait(0.1)
        self.next_slide()

        self.play(Write(integral_1), run_time=0.5)
        self.wait(0.1)
        self.next_slide()

        self.play(ReplacementTransform(integral_1, integral_1_2[0]), run_time=0.6)
        self.wait(0.2)
        self.play(Write(integral_2), run_time=1)
        self.wait(0.1)
        self.next_slide()

        self.play(ReplacementTransform(integral_2, integral_1_2[1]), run_time=0.6)
        self.wait(0.1)
        self.next_slide()

        self.play(integral_calc[:2].animate.shift(UP * 0.5), run_time=0.5)
        integral_calc[2:].shift(UP * 0.5)
        self.play(Write(integral_calc[2]), run_time=0.7)
        self.wait(0.1)
        self.next_slide()

        self.play(
            Group(*integral_calc[2][1:4], integral_calc[2][5], *integral_calc[2][15:])
            .animate(lag_ratio=1, run_time=0.5)
            .set_color(BLUE)
        )
        self.wait(0.1)
        self.next_slide()

        integral_calc[3][1:5].set_color(BLUE)
        self.play(Write(integral_calc[3]), run_time=0.7)
        self.wait(0.1)
        self.next_slide()

        substitution = MathTex(
            r"u = \sin {2 \pi x}, & \quad v' = \sin {2 \pi x} \cos ^{n-2} {2 \pi x} \\ ",
            r"u' = 2 \pi \cos {2 \pi x}, & \quad v = -{1 \over 2 \pi (n-1)} \cos ^{n-1} {2 \pi x}",
        )
        substitution.scale(0.8).next_to(integral_calc[3], DOWN, 1).set_x(0)
        self.play(Write(substitution[0]), run_time=0.7)
        self.wait(0.1)
        self.next_slide()

        self.play(Write(substitution[1]), run_time=0.7)
        self.wait(0.1)
        self.next_slide()

        substitution_applied = MathTex(
            r"= I_{n-2} - \bigl[ u v \bigr]^1_0 + \int^1_0 u' v \> dx",
        )
        (
            substitution_applied.scale(0.8)
            .next_to(integral_calc[3], DOWN)
            .align_to(integral_calc[4], LEFT)
        )

        substitution.save_state()
        substitution.scale(0.5).shift(RIGHT * 3 + DOWN * 1.2)
        substitution_box = SurroundingRectangle(substitution, GOLD, stroke_width=1)
        substitution.restore()

        self.play(
            AnimationGroup(
                substitution.animate.scale(0.5).shift(RIGHT * 3 + DOWN * 1.2),
                Create(substitution_box),
                lag_ratio=0.7,
                run_time=1,
            )
        )
        self.play(Create(substitution_applied), run_time=0.7)
        self.wait(0.1)
        self.next_slide()

        self.play(
            TransformMatchingShapes(substitution_applied, integral_calc[4:6]),
            run_time=0.7,
        )
        self.wait(0.1)
        self.next_slide()

        self.play(Circumscribe(integral_calc[4][7:35]))
        self.wait(0.1)
        self.next_slide()

        zero = MathTex("0")
        zero.scale(0.8).next_to(integral_calc[4][5])
        integral_results = [
            MathTex(
                r"&= I_{n-2} + \int^1_0 2 \pi ",
                r"\, ",
                r"\cos {2 \pi x} \, ",
                r"\{ - {1 \over 2 \pi (n-1)} ",
                r"\cos^{n-1} {2 \pi x} ",
                r"\} ",
                r"\> dx",
            ),
            MathTex(
                r"&= I_{n-2} ",
                r"+ ",
                r"\int^1_0 ",
                r"2 \pi ",
                r"\{ - {1 \over 2 \pi (n-1)} ",
                r"\} ",
                r"\, ",
                r"\cos {2 \pi x} \, ",
                r"\cos^{n-1} {2 \pi x} ",
                r"\> dx",
            ),
            MathTex(
                r"&= I_{n-2} ",
                r"+ ",
                r"\int^1_0 ",
                r"\{ ",
                r"- ",
                r"{1 \over n-1} ",
                r"\} ",
                r"\, ",
                r"\cos {2 \pi x} \, ",
                r"\cos^{n-1} {2 \pi x} ",
                r"\> dx",
            ),
            MathTex(
                r"&= I_{n-2} ",
                r"- ",
                r"{1 \over n-1} ",
                r"\int^1_0 ",
                r"\cos {2 \pi x} \, ",
                r"\cos^{n-1} {2 \pi x} ",
                r"\> dx",
            ),
            MathTex(
                r"&= I_{n-2} ",
                r"- ",
                r"{1 \over n-1} ",
                r"\int^1_0 ",
                r"\cos^n {2 \pi x} ",
                r"\> dx",
            ),
            MathTex(
                r"&= I_{n-2} ",
                r"- ",
                r"{1 \over n-1} ",
                r"I_n",
            ),
        ]
        for i in integral_results:
            i.scale(0.8).next_to(integral_calc[3], DOWN, aligned_edge=LEFT)

        self.play(ReplacementTransform(integral_calc[4][6:], zero))
        self.wait(0.2)
        self.play(FadeOut(integral_calc[4][5:], zero), run_time=0.4)
        self.wait(0.3)
        # BUG Incorrect brackets transform
        self.play(
            TransformMatchingShapes(
                VGroup(integral_calc[4][:5], integral_calc[5]),
                integral_results[0],
            ),
            run_time=0.6,
        )
        self.wait(0.1)
        self.next_slide()

        self.play(
            TransformMatchingTex(integral_results[0], integral_results[1]),
            run_time=0.8,
        )
        self.wait(0.1)
        self.next_slide()

        self.play(
            TransformMatchingTex(integral_results[1], integral_results[2]),
            run_time=0.8,
        )
        self.wait(0.1)
        self.next_slide()

        shift = (
            integral_results[3][3].get_center() - integral_results[2][5].get_center()
        )
        self.play(
            TransformMatchingTex(integral_results[2], integral_results[3], shift=shift),
            run_time=0.7,
        )
        self.wait(0.1)
        self.next_slide()

        self.play(
            TransformMatchingShapes(integral_results[3], integral_results[4]),
            run_time=0.7,
        )
        self.wait(0.1)
        self.next_slide()

        self.play(Indicate(integral_results[4][3:]))
        self.wait(0.1)
        self.next_slide()

        self.play(Indicate(integral_calc[1]))
        self.wait(0.1)
        self.next_slide()

        self.play(
            ReplacementTransform(integral_results[4][:3], integral_results[5][:3]),
            TransformMatchingShapes(integral_results[4][3:], integral_results[5][3]),
            run_time=0.5,
        )
        self.wait(0.1)
        self.next_slide()

        result_old = integral_results[-1]
        integral_results = [
            MathTex(r"I_n &= I_{n-2} - {1 \over n-1} I_n", substrings_to_isolate=" "),
            MathTex(r"I_n + {1 \over n-1} I_n &= I_{n-2}", substrings_to_isolate=" "),
            MathTex(r"{n \over n-1} I_n &= I_{n-2}", substrings_to_isolate=" "),
            MathTex(r"I_n &= {n-1 \over n} I_{n-2}", substrings_to_isolate=" "),
        ]

        integral_results[0].scale(0.8).align_to(integral_calc, LEFT).match_y(
            integral_calc[0]
        )
        pos = integral_results[0].get_center()

        self.remove(result_old)
        self.play(
            AnimationGroup(
                FadeOut(
                    integral_calc[1:4],
                    integral_calc[0][2],
                    substitution,
                    substitution_box,
                ),
                AnimationGroup(
                    result_old.animate.match_y(integral_results[0]),
                    integral_calc[0][:2].animate.match_y(integral_results[0][:2]),
                ),
                lag_ratio=0.7,
                run_time=0.8,
            ),
        )
        self.wait(0.4)
        self.remove(integral_calc[0][0], integral_calc[0][1], result_old)
        self.play(integral_results[0].animate.scale(1.25).center())
        self.wait(0.1)
        self.next_slide()

        self.play(
            TransformMatchingTex(integral_results[0], integral_results[1]),
            run_time=0.7,
        )
        self.wait(0.1)
        self.next_slide()

        self.play(
            TransformMatchingTex(integral_results[1], integral_results[2]),
            run_time=0.7,
        )
        self.wait(0.1)
        self.next_slide()

        self.play(
            TransformMatchingTex(integral_results[2], integral_results[3]),
            run_time=0.7,
        )
        self.wait(0.1)
        self.next_slide()

        self.play(integral_results[3].animate.scale(0.8).move_to(pos))
        integral_1_2.generate_target()
        integral_1_2.target.scale(1.25)

        I_3 = MathTex(r"I_3 = 0")
        I_4 = MathTex(r"I_4 = {3 \cdot 1 \over 4 \cdot 2}")
        I_5 = MathTex(r"I_5 = 0")
        I_6 = MathTex(r"I_6 = {5 \cdot 3 \cdot 1 \over 6 \cdot 4 \cdot 2}")
        I_7 = MathTex(r"I_7 = 0")
        I_8 = MathTex(
            r"I_8 = {7 \cdot 5 \cdot 3 \cdot 1 \over 8 \cdot 6 \cdot 4 \cdot 2}"
        )

        VGroup(
            integral_1_2.target[0], I_3, I_5, I_7, integral_1_2.target[1], I_4, I_6, I_8
        ).arrange_in_grid(
            rows=2, col_widths=[2.5] * 4, buff=(0.5, 0.8), cell_alignment=ORIGIN
        ).center().shift(
            DOWN * 0.5
        )
        I_4.shift(LEFT * 0.3)
        I_6.shift(LEFT * 0.2)
        I_8.shift(RIGHT * 0.3)

        self.play(MoveToTarget(integral_1_2))
        self.wait(0.1)
        self.next_slide()

        self.play(
            AnimationGroup(
                Write(I_3), Write(I_5), Write(I_7), lag_ratio=0.8, run_time=1.5
            )
        )
        self.wait(0.1)
        self.next_slide()
        self.play(
            AnimationGroup(
                Write(I_4), Write(I_6), Write(I_8), lag_ratio=0.8, run_time=1.8
            )
        )
        self.wait(0.1)
        self.next_slide()

        self.play(FadeOut(*self.mobjects))
        self.wait(0.1)
        self.next_slide()

        # TODO Results


# TODO Outro
class Outro(Slide):
    def construct(self):
        self.play(FadeOut(*self.mobjects))
        self.wait(0.1)
        self.next_slide()
